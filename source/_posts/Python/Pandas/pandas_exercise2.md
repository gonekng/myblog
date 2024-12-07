---
title: "Pandas EX2 : 데이터프레임 구조화"
categories:
  - python
  - pandas
tag:
  - python
  - pandas
author: "Jiwon Kang"
date: 2024-12-07 16:17:30
---

Python 라이브러리 Pandas에는 데이터프레임을 구조화하는 함수들이 있다.  
각 인덱스(행)와 컬럼(열)을 통해 데이터에 접근 및 조작이 가능하다.  

![www.w3resource.com](https://blog.kakaocdn.net/dn/4XCuG/btqPsCKDKGy/p29ilnD0gSzabqgbtas95k/img.jpg)

---

## 데이터프레임 구조화 함수

- `pivot()` : 특정 열을 기준으로 데이터를 재구성하는 함수
- `pivot_table()` : `pivot()` 함수와 비슷하나, `aggfunc` 매개변수를 활용하여 다양한 집계 함수를 적용할 수 있음
- `stack()` : 특정 열을 인덱스로 변환해서 행으로 쌓아올리는 함수
- `unstack()` : `stack()` 함수의 반대 과정으로, 특정 인덱스를 열로 다시 변환하는 함수
- `melt()` : 여러 열을 하나의 열로 묶는 함수로, 이 경우 열 이름을 담는 열과 값을 담는 열로 구분됨

## 데이터프레임 구조화 예시

아래는 Pandas 데이터프레임을 생성하고, 순서대로 `pivot()`, `pivot_table()`, `stack()`, `unstack()`, `melt()` 함수를 적용하는 예시이다.

### 데이터프레임 생성

```python
import pandas as pd

# 샘플 데이터프레임 생성
data = {
    'date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02', '2024-01-01', '2024-01-02'],
    'city': ['Seoul', 'Busan', 'Incheon', 'Seoul', 'Busan', 'Incheon', 'Seoul', 'Busan'],
    'temperature': [5, 7, 6, 8, 9, 7, 6, 10],
    'humidity': [55, 60, 58, 50, 65, 70, 58, 62],
    'wind_speed': [5.0, 7.5, 6.0, 3.5, 4.0, 5.5, 6.5, 8.0]
}

df = pd.DataFrame(data)
print("원본 데이터프레임:")
print(df)
```

```python
원본 데이터프레임:
         date     city  temperature  humidity  wind_speed
0  2024-01-01   Seoul            5        55         5.0
1  2024-01-01   Busan            7        60         7.5
2  2024-01-01  Incheon           6        58         6.0
3  2024-01-02   Seoul            8        50         3.5
4  2024-01-02   Busan            9        65         4.0
5  2024-01-02  Incheon           7        70         5.5
6  2024-01-01   Seoul            6        58         6.5
7  2024-01-02   Busan           10        62         8.0
```

### 1. `pivot()`

```python
try:
    pivoted = df.pivot(index='date', columns='city', values='temperature')
except ValueError as e:
    print("pivot() 오류 발생")
```

```python
pivot() 오류 발생
```

- temperature의 값이 중복되므로 `pivot()` 함수는 오류를 발생시킨다. 이를 해결하기 위해 `pivot_table()` 함수를 사용할 수 있다.

### 2. `pivot_table()`

```python
pivot_table = df.pivot_table(index='date', columns='city', values='temperature', aggfunc='mean')
print("pivot_table() 결과:")
print(pivot_table)
```

```python
pivot_table() 결과:
city         Busan  Incheon  Seoul
date                                
2024-01-01      7.0      6.0    5.5
2024-01-02      9.5      7.0    8.0
```

### 3. `stack()`

```python
stacked = pivot_table.stack()
print("stack() 결과:")
print(stacked)
```

```python
stack() 결과:
date        city  
2024-01-01  Busan    7.0
            Incheon  6.0
            Seoul    5.5
2024-01-02  Busan    9.5
            Incheon  7.0
            Seoul    8.0
dtype: float64
```

### 4. `unstack()`

```python
unstacked = stacked.unstack()
print("unstack() 결과:")
print(unstacked)
```

```python
unstack() 결과:
city         Busan  Incheon  Seoul
date                                
2024-01-01      7.0      6.0    5.5
2024-01-02      9.5      7.0    8.0
```

### 5. `melt()`

```python
melted = pd.melt(df, id_vars=['date', 'city'], value_vars=['temperature', 'humidity', 'wind_speed'])
print("melt() 결과:")
print(melted)
```

```python
melt() 결과:
         date     city      variable  value
0  2024-01-01   Seoul  temperature    5.0
1  2024-01-01   Busan  temperature    7.0
2  2024-01-01  Incheon  temperature    6.0
3  2024-01-02   Seoul  temperature    8.0
4  2024-01-02   Busan  temperature    9.0
5  2024-01-02  Incheon  temperature    7.0
6  2024-01-01   Seoul      humidity   55.0
7  2024-01-01   Busan      humidity   60.0
8  2024-01-01  Incheon      humidity   58.0
9  2024-01-02   Seoul      humidity   50.0
10 2024-01-02   Busan      humidity   65.0
11 2024-01-02  Incheon      humidity   70.0
12 2024-01-01   Seoul     wind_speed    5.0
13 2024-01-01   Busan     wind_speed    7.5
14 2024-01-01  Incheon     wind_speed    6.0
15 2024-01-02   Seoul     wind_speed    3.5
16 2024-01-02   Busan     wind_speed    4.0
17 2024-01-02  Incheon     wind_speed    5.5
```

---

## Reference

[API reference — pandas 2.2.3 documentation](https://pandas.pydata.org/docs/reference/index.html)  
[[Pandas] 데이터프레임 재구조화하기(Stack,Unstack)](https://seong6496.tistory.com/241)  