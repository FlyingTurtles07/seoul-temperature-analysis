# -*- coding: utf-8 -*-
"""
보너스 과제 A: 시계열 분해 (추세/계절성/잔차)
STL(Seasonal-Trend decomposition using Loess) 사용
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import platform
import os
from statsmodels.tsa.seasonal import STL

system = platform.system()

if system == "Windows":
    mpl.rcParams['font.family'] = 'Malgun Gothic'
elif system == "Darwin":  # macOS
    mpl.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    _font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
    if os.path.exists(_font_path):
        fm.fontManager.addfont(_font_path)
        mpl.rcParams['font.family'] = fm.FontProperties(fname=_font_path).get_name()

mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('data/seoul_2021_2025_processed.csv', parse_dates=['날짜'])
df = df.set_index('날짜').asfreq('D')
series = df['평균기온']

# 연주기(365일) 계절성으로 STL 분해
stl = STL(series, period=365, robust=True)
result = stl.fit()

fig, axes = plt.subplots(4, 1, figsize=(14, 10), sharex=True)
axes[0].plot(series.index, series.values, color='steelblue', linewidth=0.7)
axes[0].set_title('원본 (평균기온)')
axes[1].plot(series.index, result.trend, color='crimson', linewidth=1.2)
axes[1].set_title('추세(Trend)')
axes[2].plot(series.index, result.seasonal, color='darkorange', linewidth=0.7)
axes[2].set_title('계절성(Seasonal, 연주기)')
axes[3].plot(series.index, result.resid, color='gray', linewidth=0.5)
axes[3].set_title('잔차(Residual)')
axes[3].set_xlabel('날짜')

plt.suptitle('평균기온 시계열 분해 (STL, 연주기=365일)', y=1.0)
plt.tight_layout()
plt.savefig('images/07_시계열분해.png', dpi=150)
plt.close()

trend_start = result.trend.dropna().iloc[0]
trend_end = result.trend.dropna().iloc[-1]
print(f"추세 시작값(평활): {trend_start:.2f}℃")
print(f"추세 종료값(평활): {trend_end:.2f}℃")
print(f"5년간 추세 변화량: {trend_end - trend_start:+.2f}℃")
print(f"잔차 표준편차: {result.resid.std():.2f}℃ (원본 표준편차 {series.std():.2f}℃ 대비 "
      f"{result.resid.std()/series.std()*100:.1f}%)")
print("시계열 분해 완료 -> images/07_시계열분해.png")
