# 서울 일별 기온 데이터 시계열 분석

서울(108) 지점의 2021~2025년 일별 기온 데이터를 활용한 계절성 및 이상기온 트렌드 분석 프로젝트.

## 폴더 구조

seoul-temperature-analysis/
├── data/
│ ├── seoul_2021_2025.csv            # 원본 데이터 (기상청 ASOS)
│ └── seoul_2021_2025_processed.csv  # 전처리 완료 데이터
├── images/                          # 시각화 결과 6개
├── analysis.py                      # 전체 분석 코드
├── bonus_decomposition.py           # 보너스: 시계열 분해(STL)
├── bonus_forecast.py                # 보너스: 베이스라인 예측
├── dashboard.html                   # 보너스: 인터랙티브 대시보드
├── REPORT.md                        # 분석 리포트
├── BONUS.md                         # 보너스 과제 정리
├── requirements.txt
└── README.md


## 실행 방법

pip install -r requirements.txt
python3 analysis.py


Windows에서는 `python3` 대신 `py`를 사용하세요:

py -m pip install -r requirements.txt
py analysis.py


실행하면 `data/seoul_2021_2025_processed.csv`(전처리 완료 데이터)와 `images/` 폴더에 6개의 시각화 PNG 파일이 생성됩니다.

한글 폰트는 OS별로 자동 설정됩니다 (Windows: 맑은 고딕, macOS: AppleGothic, Linux: Noto Sans CJK KR).

### 보너스 과제 실행

py bonus_decomposition.py # 시계열 분해(STL)
py bonus_forecast.py # 베이스라인 예측


`dashboard.html`은 별도 실행 없이 브라우저로 바로 열면 됩니다.

## 데이터 출처

- 기상청 기상자료개방포털(<https://data.kma.go.kr>) 종관기상관측(ASOS)
- 지점: 서울(108)
- 기간: 2021-01-01 ~ 2025-12-31
- 라이선스: 공공데이터포털 이용약관에 따름 (출처 표시 시 자유 이용 가능)