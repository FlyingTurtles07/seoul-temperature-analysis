# -*- coding: utf-8 -*-
"""
서울(108) 일별 기온 데이터를 활용한 계절성 및 이상기온 트렌드 분석
기간: 2021-01-01 ~ 2025-12-31 (기상청 ASOS)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import platform
import os

# OS별 한글 폰트 자동 설정
system = platform.system()

if system == "Windows":
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif system == "Darwin":  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    _font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
    if os.path.exists(_font_path):
        fm.fontManager.addfont(_font_path)
        plt.rcParams['font.family'] = 'Noto Sans CJK KR'

plt.rcParams['axes.unicode_minus'] = False
# ============================================================
# STEP A. 데이터 로드 + 전처리
# ============================================================
raw = pd.read_csv('data/seoul_2021_2025.csv', encoding='cp949')

# 컬럼명 정리 (기상청 원본 컬럼명 -> 분석용 짧은 이름)
raw = raw.rename(columns={
    '일시': '날짜',
    '평균기온(°C)': '평균기온',
    '최저기온(°C)': '최저기온',
    '최저기온 시각(hhmi)': '최저기온시각',
    '최고기온(°C)': '최고기온',
    '최고기온 시각(hhmi)': '최고기온시각',
    '강수 계속시간(hr)': '강수계속시간',
    '10분 최다 강수량(mm)': '10분최다강수량',
    '1시간 최다강수량(mm)': '1시간최다강수량',
})
df = raw.copy()
df['날짜'] = pd.to_datetime(df['날짜'])
df = df.sort_values('날짜').reset_index(drop=True)

log = []  # REPORT.md에 넣을 처리 로그
log.append(f"데이터 기간: {df['날짜'].min().date()} ~ {df['날짜'].max().date()}")
log.append(f"전체 행 수: {len(df)}")

na_before = df[['평균기온', '최저기온', '최고기온', '강수계속시간',
                '10분최다강수량', '1시간최다강수량']].isnull().sum()
log.append("컬럼별 결측치(처리 전):\n" + na_before.to_string())

# 1차 필터: 물리적 오류 제거
before = len(df)
df = df[(df['평균기온'].between(-30, 40)) | (df['평균기온'].isnull())]
df = df[~(df['최고기온'] < df['최저기온'])]
df = df[(df['강수계속시간'] >= 0) | (df['강수계속시간'].isnull())]
after = len(df)
log.append(f"1차 필터(물리적 오류) 제거 건수: {before - after}건")

# 기온 결측: 연속 2일 이하만 선형보간
temp_na_before = df['평균기온'].isnull().sum()
df['평균기온'] = df['평균기온'].interpolate(method='linear', limit=2)
temp_na_after = df['평균기온'].isnull().sum()
log.append(f"평균기온 결측 {temp_na_before}건 중 보간 처리: {temp_na_before - temp_na_after}건, "
           f"3일 이상 연속 결측으로 남은 건수(제외 대상): {temp_na_after}건")

df = df.dropna(subset=['평균기온']).reset_index(drop=True)

# 강수 관련 컬럼: 결측 = 무강수(0)로 처리
rain_cols = ['강수계속시간', '10분최다강수량', '1시간최다강수량']
rain_na_counts = df[rain_cols].isnull().sum()
log.append("강수 관련 컬럼 결측 -> 0(무강수)으로 대체한 건수:\n" + rain_na_counts.to_string())
df[rain_cols] = df[rain_cols].fillna(0)

log.append(f"전처리 후 최종 행 수: {len(df)}")

with open('preprocessing_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(log))
print('\n\n'.join(log))
print("\n" + "=" * 60 + "\n")

# ============================================================
# STEP B. 4가지 분석기법 계산
# ============================================================
df['이동평균_7일'] = df['평균기온'].rolling(7).mean()

df['월'] = df['날짜'].dt.month
df['연도'] = df['날짜'].dt.year

def get_season(month):
    if month in [12, 1, 2]:
        return '겨울'
    elif month in [3, 4, 5]:
        return '봄'
    elif month in [6, 7, 8]:
        return '여름'
    else:
        return '가을'

df['계절'] = df['월'].apply(get_season)

# 이상기온 탐지: 월별 평균 ± 2표준편차
monthly_stats = df.groupby('월')['평균기온'].agg(['mean', 'std']).rename(
    columns={'mean': '월평균', 'std': '월표준편차'})
df = df.merge(monthly_stats, on='월', how='left')
df['이상기온여부'] = (df['평균기온'] - df['월평균']).abs() > 2 * df['월표준편차']

# 일교차
df['일교차'] = df['최고기온'] - df['최저기온']

df.to_csv('data/seoul_2021_2025_processed.csv', index=False, encoding='utf-8-sig')

stepB_summary = f"""
[STEP B 계산 결과 요약]
이상기온 발생일 수: {df['이상기온여부'].sum()}일 (전체의 {df['이상기온여부'].mean()*100:.1f}%)
계절별 평균기온:
{df.groupby('계절')['평균기온'].mean().round(1).to_string()}
계절별 일교차 평균:
{df.groupby('계절')['일교차'].mean().round(1).to_string()}
"""
print(stepB_summary)

# ============================================================
# 기존 계획된 시각화 6개 실행
# ============================================================

# 01. 일별 평균기온 (전체기간)
plt.figure(figsize=(14, 5))
plt.plot(df['날짜'], df['평균기온'], color='steelblue', linewidth=0.8)
plt.title('일별 평균기온 (2021.01~2025.12, 서울)')
plt.xlabel('날짜'); plt.ylabel('평균기온(℃)')
plt.tight_layout()
plt.savefig('images/01_일별평균기온.png', dpi=150)
plt.close()

# 02. 평균기온 + 7일 이동평균
plt.figure(figsize=(14, 5))
plt.plot(df['날짜'], df['평균기온'], alpha=0.3, color='gray', label='일별 평균기온')
plt.plot(df['날짜'], df['이동평균_7일'], color='crimson', linewidth=1.5, label='7일 이동평균')
plt.title('평균기온 및 7일 이동평균 (추세)')
plt.xlabel('날짜'); plt.ylabel('평균기온(℃)')
plt.legend()
plt.tight_layout()
plt.savefig('images/02_이동평균.png', dpi=150)
plt.close()

# 03. 월별 평균기온 (계절성)
monthly_avg = df.groupby('월')['평균기온'].mean()
plt.figure(figsize=(10, 5))
monthly_avg.plot(kind='bar', color='orange')
plt.title('월별 평균기온 (5년 평균)')
plt.xlabel('월'); plt.ylabel('평균기온(℃)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('images/03_월별평균기온.png', dpi=150)
plt.close()

# 04. 이상기온 탐지
plt.figure(figsize=(14, 5))
plt.plot(df['날짜'], df['평균기온'], color='gray', alpha=0.4, label='평균기온')
plt.scatter(df.loc[df['이상기온여부'], '날짜'], df.loc[df['이상기온여부'], '평균기온'],
            color='red', s=15, label='이상기온(±2σ)')
plt.title('이상기온 탐지 (월별 평균±2표준편차 기준)')
plt.xlabel('날짜'); plt.ylabel('평균기온(℃)')
plt.legend()
plt.tight_layout()
plt.savefig('images/04_이상기온탐지.png', dpi=150)
plt.close()

# 05. 계절별 일교차 분포 (박스플롯, 봄/여름/가을/겨울 순서)
season_order = ['봄', '여름', '가을', '겨울']
plt.figure(figsize=(9, 5))
box_data = [df.loc[df['계절'] == s, '일교차'].dropna() for s in season_order]
plt.boxplot(box_data, tick_labels=season_order)
plt.title('계절별 일교차 분포')
plt.xlabel('계절'); plt.ylabel('일교차(℃)')
plt.tight_layout()
plt.savefig('images/05_계절별일교차.png', dpi=150)
plt.close()

# 06. 이상기온일 vs 평상일 강수 패턴 (3개 지표로 세분화)
df['강수여부'] = df['강수계속시간'] > 0
rain_rate = df.groupby('이상기온여부')['강수여부'].mean() * 100
rain_rate.index = ['평상일', '이상기온일']

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

rain_rate.plot(kind='bar', ax=axes[0], color=['skyblue', 'salmon'])
axes[0].set_title('강수 발생 비율(%)')
axes[0].set_xticklabels(['평상일', '이상기온일'], rotation=0)

dur = df.groupby('이상기온여부')['강수계속시간'].mean()
dur.index = ['평상일', '이상기온일']
dur.plot(kind='bar', ax=axes[1], color=['skyblue', 'salmon'])
axes[1].set_title('평균 강수계속시간(hr)')
axes[1].set_xticklabels(['평상일', '이상기온일'], rotation=0)

heavy = df.groupby('이상기온여부')['10분최다강수량'].mean()
heavy.index = ['평상일', '이상기온일']
heavy.plot(kind='bar', ax=axes[2], color=['skyblue', 'salmon'])
axes[2].set_title('평균 10분최다강수량(mm)')
axes[2].set_xticklabels(['평상일', '이상기온일'], rotation=0)

plt.suptitle('이상기온일 vs 평상일 강수 패턴 비교')
plt.tight_layout()
plt.savefig('images/06_이상기온_강수관계.png', dpi=150)
plt.close()

print("6개 시각화 저장 완료 -> images/")

# ============================================================
# STEP C. 인사이트용 숫자 추출
# ============================================================
insight_numbers = {
    '여름_평균기온': round(df.loc[df['계절'] == '여름', '평균기온'].mean(), 1),
    '겨울_평균기온': round(df.loc[df['계절'] == '겨울', '평균기온'].mean(), 1),
    '이상기온_발생일수': int(df['이상기온여부'].sum()),
    '이상기온_비율(%)': round(df['이상기온여부'].mean() * 100, 1),
    '계절별_일교차': df.groupby('계절')['일교차'].mean().round(1).to_dict(),
    '평상일_강수비율(%)': round(rain_rate['평상일'], 1),
    '이상기온일_강수비율(%)': round(rain_rate['이상기온일'], 1),
    '연도별_이상기온일수': df.groupby('연도')['이상기온여부'].sum().to_dict(),
}
import json
with open('insight_numbers.json', 'w', encoding='utf-8') as f:
    json.dump(insight_numbers, f, ensure_ascii=False, indent=2)

print("\n[STEP C용 숫자]")
print(json.dumps(insight_numbers, ensure_ascii=False, indent=2))
