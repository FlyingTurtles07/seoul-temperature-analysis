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
