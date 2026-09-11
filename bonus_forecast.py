# -*- coding: utf-8 -*-
"""
보너스 과제 A-2: 간단 예측 (베이스라인)
방법: 과거 4년(2021~2024) 같은 '월-일'의 평균값을 사용해 2025년 12월(마지막 30일)을 예측
      (계절성 기반 naive baseline, 정확도보다 가정/한계 설명에 집중)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

_font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fm.fontManager.addfont(_font_path)
mpl.rcParams['font.family'] = fm.FontProperties(fname=_font_path).get_name()
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('data/seoul_2021_2025_processed.csv', parse_dates=['날짜'])
df['월일'] = df['날짜'].dt.strftime('%m-%d')

# 검증 구간: 2025-12-02 ~ 2025-12-31 (30일)
test_start = pd.Timestamp('2025-12-02')
test_end = pd.Timestamp('2025-12-31')
train = df[df['날짜'] < test_start]
test = df[(df['날짜'] >= test_start) & (df['날짜'] <= test_end)].copy()

# 베이스라인: 학습 구간(2021~2025-12-01)의 같은 월-일 평균으로 예측
baseline = train.groupby('월일')['평균기온'].mean()
test['예측_평균기온'] = test['월일'].map(baseline)

mae = (test['평균기온'] - test['예측_평균기온']).abs().mean()
rmse = np.sqrt(((test['평균기온'] - test['예측_평균기온']) ** 2).mean())

print(f"검증 구간: {test_start.date()} ~ {test_end.date()} ({len(test)}일)")
print(f"MAE: {mae:.2f}℃, RMSE: {rmse:.2f}℃")

plt.figure(figsize=(12, 5))
plt.plot(test['날짜'], test['평균기온'], marker='o', label='실제값', color='steelblue')
plt.plot(test['날짜'], test['예측_평균기온'], marker='x', label='베이스라인 예측(과거 동일 월-일 평균)',
          color='crimson', linestyle='--')
plt.title(f'2025년 12월 평균기온 베이스라인 예측 vs 실제 (MAE={mae:.2f}℃)')
plt.xlabel('날짜'); plt.ylabel('평균기온(℃)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/08_베이스라인예측.png', dpi=150)
plt.close()
print("예측 그래프 저장 완료 -> images/08_베이스라인예측.png")
