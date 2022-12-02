---
title: "Feature Scaling"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - scikit-learn
author: "Jiwon Kang"
date: 2022-03-26 15:38:35
---

# 정규화 vs 표준화

- 정규화 : **데이터의 범위의 차이를 왜곡하지 않고 공통 척도로 변경하는 것**
    - ML에서 모든 데이터셋이 정규화 될 필요는 없고, 피처의 범위가 다른 경우에 필요하다.
- 표준화 : **데이터가 표준정규분포의 속성을 갖도록 재조정되는 것**

| 정규화(Normalization) | 표준화(Standardization) |
| --- | --- |
| Scaling에 최대/최소값이 사용된다. | Scaling에 평균 및 표준편차가 사용된다. |
| [0,1] 또는 [-1,1] 사이의 값으로 변환된다. | 특정 범위로 제한되지 않는다. |
| Feature의 크기(범위)가 다를 때 사용한다. | 평균을 0, 표준편차를 1로 만들고자 할 때 사용한다. |
| Feature의 분포에 대해 모를 때 유용하다. | Feature가 정규분포(에 근사)인 경우 유용하다. |
| MinMaxScaler, MinAbsScaler, Normalizer | StandardScaler, RobustScaler |

<Br>


# Python Scaler 종류

### StandardScaler
    - 평균이 0, 분산이 1인 정규분포 (표준정규분포화)
    - 이상치의 영향 많이 받음
        
        ```python
        from sklearn.preprocessing import StandardScaler
        
        std = StandardScaler()
        std.fit(X_train)
        X_train_scaled = std.transform(X_train)
        X_test_scaled = std.transform(X_test)
        ```
        
### MinMaxScaler
    - 0과 1 사이의 값으로 변환
    - 이상치의 영향 많이 받음
        
        ```python
        from sklearn.preprocessing import MinMaxScaler
        
        mms = MinMaxScaler()
        mms.fit(X_train)
        X_train_scaled = mms.transform(X_train)
        X_test_scaled = mms.transform(X_test)
        ```
        
### MaxAbsScaler
    - -1과 1 사이의 값으로 변환
    - 이상치의 영향 많이 받음
        
        ```python
        from sklearn.preprocessing import MaxAbsScaler
        
        mas = MaxAbsScaler()
        mas.fit(X_train)
        X_train_scaled = mas.transform(X_train)
        X_test_scaled = mas.transform(X_test)
        ```
        
### RobustScaler
    - StandardScaler와 유사하나, 평균과 분산 대신 중간값과 사분위값을 사용
    - 이상치의 영향 최소화
        
        ```python
        from sklearn.preprocessing import StandardScaler
        
        std = StandardScaler()
        std.fit(X_train)
        X_train_scaled = std.transform(X_train)
        X_test_scaled = std.transform(X_test)
        ```
        
### Normalizer
    - 각 열이 아닌 행마다 정규화 수행
    - 한 행의 모든 피처들 사이의 유클리드 거리가 1이 되도록 함
    - 학습이 빠르고, 과대적합 가능성을 낮출 수 있음
        
        ```python
        from sklearn.preprocessing import RobustScaler
        
        rbs = RobustScaler()
        X_train_scaled = rbs.fit_transform(X_train)
        X_test_scaled = rbs.transform(X_test)
        ```
