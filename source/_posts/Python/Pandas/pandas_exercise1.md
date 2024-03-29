---
title: "Pandas EX1 : split()을 이용한 텍스트 컬럼 생성"
categories:
  - python
  - pandas
tag:
  - python
  - pandas
author: "Jiwon Kang"
date: 2024-02-13 22:51:00
---

- 연도별 전국읍면동_인구통계 데이터를 Pandas를 활용하여 통합정리하는 코드
    - 텍스트 컬럼에 `split()` 함수를 적용하여 새로운 컬럼을 생성함

## 0 :: 필요한 라이브러리 임포트

```python
import os
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
```

## 1 :: 파일 불러오기

```python
file_list = [file for file in os.listdir("전국읍면동_인구통계") if file.endswith('csv')]
for i, file in enumerate(file_list):
    df = pd.read_csv("전국읍면동_인구통계" + file, encoding='cp949')
    df = df.iloc[:,[0,1,5,9,13,17,21,25,29,33,37,41,45]]
    df['행정구역'] = df['행정구역'].str[:-12].apply(lambda x: x.strip())
    df.columns = ['행정구역', '1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
```

- ‘전국읍면동_인구통계’ 폴더 하의 CSV 파일을 차례대로 불러오는 코드
    - `인구수_전국_2010.csv`
        
        ![](/images/Python/Pandas/Untitled.png)
        

## 2 :: 텍스트 컬럼 SPLIT

```python
df['토큰_개수'] = df['행정구역'].apply(lambda x: len(str(x).split()))
for tokens in range(1, df['토큰_개수'].max() + 1):
    df.loc[df['토큰_개수'] == tokens, [f'토큰_{i+1}' for i in range(tokens)]] = df.loc[df['토큰_개수'] == tokens, '행정구역'].str.split().tolist()
df1 = df[df['토큰_개수'] == 1]
df2 = df[df['토큰_개수'] == 2]
df3 = df[df['토큰_개수'] == 3]
df4 = df[df['토큰_개수'] == 4]
```

- 행정구역 컬럼 값이 단일값으로 되어있음 (ex. 서울특별시 종로구 삼청동)
    - 따라서 `split()` 함수를 사용하여 공백을 기준으로 시도, 시군구, 행정동 컬럼을 구분함
        
        → 텍스트 분할의 결과 토큰은 1~4개로 나타나며, 각 케이스의 특징을 데이터를 통해 확인하였음
        

```python
df1['시도'] = df1['토큰_1']
df1['시군구'] = '전체'
df1['행정동'] = '전체'
```

- 토큰이 1개인 경우
    - `시도` → `시도` `전체` `전체`
        
        ex. `서울특별시` → `서울특별시` `전체` `전체`
        

```python
df2.loc[df2['토큰_1'] != '세종특별자치시', '시도'] = df2.loc[df2['토큰_1'] != '세종특별자치시', '토큰_1']
df2.loc[df2['토큰_1'] != '세종특별자치시', '시군구'] = df2.loc[df2['토큰_2'] != '세종특별자치시', '토큰_2']
df2.loc[df2['토큰_1'] != '세종특별자치시', '행정동'] = '전체'

df2.loc[df2['토큰_1'] == '세종특별자치시', '시도'] = df2.loc[df2['토큰_1'] == '세종특별자치시', '토큰_1']
df2.loc[df2['토큰_1'] == '세종특별자치시', '시군구'] = df2.loc[df2['토큰_1'] == '세종특별자치시', '토큰_1']
df2.loc[df2['토큰_1'] == '세종특별자치시', '행정동'] = df2.loc[df2['토큰_1'] == '세종특별자치시', '토큰_2']
```

- 토큰이 2개인 경우
    - `시도 시군구` → `시도` `시군구` `전체`
        
        ex. `서울특별시 종로구` → `서울특별시` `종로구` `전체`
        
    - `세종특별자치시 행정동` → `세종특별자치시` `세종특별자치시` `행정동`
        
        ex. `세종특별자치시 한솔동` → `세종특별자치시` `세종특별자치시` `한솔동`
        

```python
df3.loc[df3['토큰_1'] != df3['토큰_2'], '시도'] = df3.loc[df3['토큰_1'] != df3['토큰_2'], '토큰_1']
df3.loc[df3['토큰_1'] != df3['토큰_2'], '시군구'] = df3.loc[df3['토큰_1'] != df3['토큰_2'], '토큰_2']
df3.loc[df3['토큰_1'] != df3['토큰_2'], '행정동'] = df3.loc[df3['토큰_1'] != df3['토큰_2'], '토큰_3']

df3.loc[df3['토큰_1'] == df3['토큰_2'], '시도'] = df3.loc[df3['토큰_1'] == df3['토큰_2'], '토큰_1']
df3.loc[df3['토큰_1'] == df3['토큰_2'], '시군구'] = df3.loc[df3['토큰_1'] == df3['토큰_2'], '토큰_3']
df3.loc[df3['토큰_1'] == df3['토큰_2'], '행정동'] = '전체'
```

- 토큰이 3개인 경우
    - `시도 시군구 행정동` → `시도` `시군구` `행정동`
        
        ex. `서울특별시 종로구 삼청동` → `서울특별시` `종로구` `삼청동`
        
    - `시도 시도 시군구` → `시도` `시군구` `전체`
        
        ex. `서울특별시 서울특별시 종로구` → `서울특별시` `종로구` `전체`
        

```python
df4.loc[df4['토큰_1'] != df4['토큰_2'], '시도'] = df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_1']
df4.loc[df4['토큰_1'] != df4['토큰_2'], '시군구'] = df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_2'] + " " + df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_3']
df4.loc[df4['토큰_1'] != df4['토큰_2'], '행정동'] = df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_4']

df4.loc[df4['토큰_1'] == df4['토큰_2'], '시도'] = df4.loc[df4['토큰_1'] == df4['토큰_2'], '토큰_1']
df4.loc[df4['토큰_1'] == df4['토큰_2'], '시군구'] = df4.loc[df4['토큰_1'] == df4['토큰_2'], '토큰_3'] + " " + df4.loc[df4['토큰_1'] == df4['토큰_2'], '토큰_4']
df4.loc[df4['토큰_1'] == df4['토큰_2'], '행정동'] = '전체'
```

- 토큰이 4개인 경우
    - `시도 시군구1 시군구2 행정동` → `시도` `시군구1+2` `행정동`
        
        ex. `경기도 용인시 수지구 죽전동` → `경기도` `용인시 수지구` `죽전동`
        
    - `시도 시도 시군구1 시군구2` → `시도` `시군구1+2` `전체`
        
        ex. `경기도 경기도 용인시 수지구` → `경기도` `용인시 수지구` `전체`
        

## 3 :: 테이블 취합 및 가공

```python
df = pd.concat([df1,df2,df3,df4], sort=True)
df = df[['시도', '시군구', '행정동', '1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']]
df['연도'] = file[-8:-4]
df = pd.melt(df, id_vars=['시도', '시군구', '행정동', '연도'], var_name='월', value_name='인구수')
df['월'] = df['월'].str[:-1]
df.drop_duplicates(inplace=True)
df['인구수'] = pd.to_numeric(df['인구수'].str.replace(',', ''), errors='coerce')
df = df[df['인구수'] > 0]
```

- `concat()` 함수로 각각의 데이터프레임을 행을 기준으로 병합함
    - 1월부터 12월까지의 데이터가 각 컬럼으로 구분되어있어, `melt()` 함수로 각각의 행으로 나누어 데이터 형태를 변환함

## 4 :: CSV 파일 통합저장

```python
if i==0:
    df.to_csv("인구수_전체데이터.csv", mode='w', index=False, encoding='cp949')
else:
    df.to_csv("인구수_전체데이터.csv", mode='a', index=False, header=False, encoding='cp949')
```

- for문의 첫번째 루프에서는 `to_csv()` 함수의 덮어쓰기(write) 모드를, 이후의 루프에서는 이어쓰기(append) 모드를 적용함

# 전체 코드

```python
import os
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

file_list = [file for file in os.listdir("전국읍면동_인구통계") if file.endswith('csv')]
for i, file in enumerate(file_list):
    
  # CSV 파일 세팅
    df = pd.read_csv("전국읍면동_인구통계" + file, encoding='cp949')
    df = df.iloc[:,[0,1,5,9,13,17,21,25,29,33,37,41,45]]
    df['행정구역'] = df['행정구역'].str[:-12].apply(lambda x: x.strip())
    df.columns = ['행정구역', '1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
    
  # -- 행정구역 컬럼 값이 단일값으로 되어있음 (ex. 서울특별시 종로구 삼청동)
  # -- 따라서 split 함수를 사용하여 공백을 기준으로 시도, 시군구, 행정동 컬럼을 구분함
  # 토큰개수 1~4
    df['토큰_개수'] = df['행정구역'].apply(lambda x: len(str(x).split()))
    for tokens in range(1, df['토큰_개수'].max() + 1):
        df.loc[df['토큰_개수'] == tokens, [f'토큰_{i+1}' for i in range(tokens)]] = df.loc[df['토큰_개수'] == tokens, '행정구역'].str.split().tolist()
    df1 = df[df['토큰_개수'] == 1]
    df2 = df[df['토큰_개수'] == 2]
    df3 = df[df['토큰_개수'] == 3]
    df4 = df[df['토큰_개수'] == 4]

  # --- 토큰이 1개인 경우 ---
  # 시도 -> 시도 / 전체 / 전체
  # ex. 서울특별시 -> 서울특별시 / 전체 / 전체
    df1['시도'] = df1['토큰_1']
    df1['시군구'] = '전체'
    df1['행정동'] = '전체'

  # --- 토큰이 2개인 경우 ---
  # 시도 시군구 -> 시도 / 시군구 / 전체
  # ex. 서울특별시 종로구 -> 서울특별시 / 종로구 / 전체
    df2.loc[df2['토큰_1'] != '세종특별자치시', '시도'] = df2.loc[df2['토큰_1'] != '세종특별자치시', '토큰_1']
    df2.loc[df2['토큰_1'] != '세종특별자치시', '시군구'] = df2.loc[df2['토큰_2'] != '세종특별자치시', '토큰_2']
    df2.loc[df2['토큰_1'] != '세종특별자치시', '행정동'] = '전체'

  # 세종특별자치시 행정동 -> 세종특별자치시 / 세종특별자치시 / 행정동
  # ex. 세종특별자치시 한솔동 -> 세종특별자치시 / 세종특별자치시 / 한솔동
    df2.loc[df2['토큰_1'] == '세종특별자치시', '시도'] = df2.loc[df2['토큰_1'] == '세종특별자치시', '토큰_1']
    df2.loc[df2['토큰_1'] == '세종특별자치시', '시군구'] = df2.loc[df2['토큰_1'] == '세종특별자치시', '토큰_1']
    df2.loc[df2['토큰_1'] == '세종특별자치시', '행정동'] = df2.loc[df2['토큰_1'] == '세종특별자치시', '토큰_2']

  # --- 토큰이 3개인 경우 ---
  # 시도 시군구 행정동 -> 시도 / 시군구 / 행정동
  # ex. 서울특별시 종로구 삼청동 -> 서울특별시 / 종로구 / 삼청동
    df3.loc[df3['토큰_1'] != df3['토큰_2'], '시도'] = df3.loc[df3['토큰_1'] != df3['토큰_2'], '토큰_1']
    df3.loc[df3['토큰_1'] != df3['토큰_2'], '시군구'] = df3.loc[df3['토큰_1'] != df3['토큰_2'], '토큰_2']
    df3.loc[df3['토큰_1'] != df3['토큰_2'], '행정동'] = df3.loc[df3['토큰_1'] != df3['토큰_2'], '토큰_3']

  # 시도 시도 시군구 -> 시도 / 시군구 / 전체
  # ex. 서울특별시 서울특별시 종로구 -> 서울특별시 / 종로구 / 전체
    df3.loc[df3['토큰_1'] == df3['토큰_2'], '시도'] = df3.loc[df3['토큰_1'] == df3['토큰_2'], '토큰_1']
    df3.loc[df3['토큰_1'] == df3['토큰_2'], '시군구'] = df3.loc[df3['토큰_1'] == df3['토큰_2'], '토큰_3']
    df3.loc[df3['토큰_1'] == df3['토큰_2'], '행정동'] = '전체'

  # --- 토큰이 4개인 경우 ---
  # 시도 시군구1 시군구2 행정동 -> 시도 / 시군구1+2 / 행정동
  # ex. 경기도 용인시 수지구 죽전동 -> 경기도 / 용인시 수지구 / 죽전동
    df4.loc[df4['토큰_1'] != df4['토큰_2'], '시도'] = df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_1']
    df4.loc[df4['토큰_1'] != df4['토큰_2'], '시군구'] = df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_2'] + " " + df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_3']
    df4.loc[df4['토큰_1'] != df4['토큰_2'], '행정동'] = df4.loc[df4['토큰_1'] != df4['토큰_2'], '토큰_4']

  # 시도 시도 시군구1 시군구2 -> 시도 / 시군구1+2 / 전체
  # ex. 경기도 경기도 용인시 수지구 -> 경기도 / 용인시 수지구 / 전체
    df4.loc[df4['토큰_1'] == df4['토큰_2'], '시도'] = df4.loc[df4['토큰_1'] == df4['토큰_2'], '토큰_1']
    df4.loc[df4['토큰_1'] == df4['토큰_2'], '시군구'] = df4.loc[df4['토큰_1'] == df4['토큰_2'], '토큰_3'] + " " + df4.loc[df4['토큰_1'] == df4['토큰_2'], '토큰_4']
    df4.loc[df4['토큰_1'] == df4['토큰_2'], '행정동'] = '전체'

  # 테이블 취합 및 가공
    df = pd.concat([df1,df2,df3,df4], sort=True)
    df = df[['시도', '시군구', '행정동', '1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']]
    df['연도'] = file[-8:-4]
    df = pd.melt(df, id_vars=['시도', '시군구', '행정동', '연도'], var_name='월', value_name='인구수')
    df['월'] = df['월'].str[:-1]
    df.drop_duplicates(inplace=True)
    df['인구수'] = pd.to_numeric(df['인구수'].str.replace(',', ''), errors='coerce')
    df = df[df['인구수'] > 0]

  # CSV 파일 통합저장
    if i==0:
        df.to_csv("인구수_전체데이터.csv", mode='w', index=False, encoding='cp949')
    else:
        df.to_csv("인구수_전체데이터.csv", mode='a', index=False, header=False, encoding='cp949')
```