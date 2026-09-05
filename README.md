# 서울 일별 기온 데이터 시계열 분석

서울(108) 지점의 2021~2025년 일별 기온 데이터를 활용한 계절성 및 이상기온 트렌드 분석 프로젝트.

## 폴더 구조

```
seoul-temperature-analysis/
├── data/
│   ├── seoul_2021_2025.csv            # 원본 데이터 (기상청 ASOS)
│   └── seoul_2021_2025_processed.csv  # 전처리 완료 데이터
├── images/                            # 시각화 결과 6개
├── analysis.py                        # 전체 분석 코드
├── REPORT.md                          # 분석 리포트
├── requirements.txt
└── README.md
```

## 실행 방법

```bash
pip install -r requirements.txt
python3 analysis.py
```

실행하면 `data/seoul_2021_2025_processed.csv`(전처리 완료 데이터)와
`images/` 폴더에 6개의 시각화 PNG 파일이 생성됩니다.

## 데이터 출처

- 기상청 기상자료개방포털(https://data.kma.go.kr) 종관기상관측(ASOS)
- 지점: 서울(108)
- 기간: 2021-01-01 ~ 2025-12-31
- 라이선스: 공공데이터포털 이용약관에 따름 (출처 표시 시 자유 이용 가능)


pip install -r requirements.txt 결과
```
PS C:\Users\swedu18\Desktop\seoul-temperature-analysis> pip install -r requirements.txt
Collecting pandas>=2.0 (from -r requirements.txt (line 1))
  Downloading pandas-3.0.5-cp314-cp314-win_amd64.whl.metadata (19 kB)
Collecting numpy>=1.24 (from -r requirements.txt (line 2))
  Downloading numpy-2.5.2-cp314-cp314-win_amd64.whl.metadata (6.6 kB)
Collecting matplotlib>=3.7 (from -r requirements.txt (line 3))
  Downloading matplotlib-3.11.1-cp314-cp314-win_amd64.whl.metadata (80 kB)
Collecting python-dateutil>=2.8.2 (from pandas>=2.0->-r requirements.txt (line 1))
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting tzdata (from pandas>=2.0->-r requirements.txt (line 1))
  Downloading tzdata-2026.3-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting contourpy>=1.0.1 (from matplotlib>=3.7->-r requirements.txt (line 3))
  Downloading contourpy-1.3.3-cp314-cp314-win_amd64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib>=3.7->-r requirements.txt (line 3))
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.28.2 (from matplotlib>=3.7->-r requirements.txt (line 3))
  Downloading fonttools-4.64.0-cp314-cp314-win_amd64.whl.metadata (126 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib>=3.7->-r requirements.txt (line 3))
  Downloading kiwisolver-1.5.1-cp314-cp314-win_amd64.whl.metadata (5.2 kB)
Collecting packaging>=20.0 (from matplotlib>=3.7->-r requirements.txt (line 3))
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pillow>=9 (from matplotlib>=3.7->-r requirements.txt (line 3))
  Downloading pillow-12.3.0-cp314-cp314-win_amd64.whl.metadata (9.3 kB)
Collecting pyparsing>=3 (from matplotlib>=3.7->-r requirements.txt (line 3))
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas>=2.0->-r requirements.txt (line 1))
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pandas-3.0.5-cp314-cp314-win_amd64.whl (10.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.0/10.0 MB 9.5 MB/s  0:00:01
Downloading numpy-2.5.2-cp314-cp314-win_amd64.whl (12.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.6/12.6 MB 10.9 MB/s  0:00:01
Downloading matplotlib-3.11.1-cp314-cp314-win_amd64.whl (9.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.5/9.5 MB 10.6 MB/s  0:00:00
Downloading contourpy-1.3.3-cp314-cp314-win_amd64.whl (232 kB)
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.64.0-cp314-cp314-win_amd64.whl (2.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 10.1 MB/s  0:00:00
Downloading kiwisolver-1.5.1-cp314-cp314-win_amd64.whl (72 kB)
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading pillow-12.3.0-cp314-cp314-win_amd64.whl (7.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 10.8 MB/s  0:00:00
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading tzdata-2026.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata, six, pyparsing, pillow, packaging, numpy, kiwisolver, fonttools, cycler, python-dateutil, contourpy, pandas, matplotlib
   ━━━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━━━━━  5/13 [numpy]  WARNING: The scripts f2py.exe and numpy-config.exe are installed in 'C:\Users\swedu18\AppData\Local\Python\pythoncore-3.14-64\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━━  7/13 [fonttools]  WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in 'C:\Users\swedu18\AppData\Local\Python\pythoncore-3.14-64\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed contourpy-1.3.3 cycler-0.12.1 fonttools-4.64.0 kiwisolver-1.5.1 matplotlib-3.11.1 numpy-2.5.2 packaging-26.3 pandas-3.0.5 pillow-12.3.0 pyparsing-3.3.2 python-dateutil-2.9.0.post0 six-1.17.0 tzdata-2026.3
PS C:\Users\swedu18\Desktop\seoul-temperature-analysis>
```
