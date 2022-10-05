---
title: "Pipeline Tutorial"
categories:
  - python
  - tutorial
tag:
  - python
  - machine learning
  - pipeline
  - google colab
author: "Jiwon Kang"
date: 2022-04-06 10:05:01
---

#### Pipeline : 데이터 누수(Data Leakge) 방지를 위한 모델링 기법
- Pycaret, MLOps (Pipeline 형태로 구축)
  + 머신러닝 코드의 자동화 및 운영 가능
- 기존 방식
  + 데이터 불러오기 -> 데이터 전처리 -> 특성 공학 -> 데이터셋 분리 -> 모델링 -> 평가
- 파이프라인 방식
  + 데이터 불러오기 -> 데이터 전처리 -> 데이터셋 분리 -> 파이프라인 구축(피처공학, 모델링) -> 평가

# 데이터 불러오기


```python
import pandas as pd
import numpy as np
data = pd.read_csv('https://raw.githubusercontent.com/MicrosoftDocs/ml-basics/master/data/daily-bike-share.csv')
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 731 entries, 0 to 730
    Data columns (total 14 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   instant     731 non-null    int64  
     1   dteday      731 non-null    object 
     2   season      731 non-null    int64  
     3   yr          731 non-null    int64  
     4   mnth        731 non-null    int64  
     5   holiday     731 non-null    int64  
     6   weekday     731 non-null    int64  
     7   workingday  731 non-null    int64  
     8   weathersit  731 non-null    int64  
     9   temp        731 non-null    float64
     10  atemp       731 non-null    float64
     11  hum         731 non-null    float64
     12  windspeed   731 non-null    float64
     13  rentals     731 non-null    int64  
    dtypes: float64(4), int64(9), object(1)
    memory usage: 80.1+ KB
    


```python
from sklearn.model_selection import train_test_split
X = data.drop('rentals',axis=1)
y = data['rentals']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=123)
```

# Pipeline 구축

## 데이터 전처리 파이프라인


```python
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 수치형 데이터
numeric_transformer = Pipeline(steps=[
       ('imputer', SimpleImputer(strategy='mean'))
      ,('scaler', StandardScaler())
])

# 서열형 데이터
ordinal_transformer = Pipeline(steps=[
       ('imputer', SimpleImputer(strategy='constant'))
      ,('ordEncoder', OrdinalEncoder())
])

# 명목형 데이터
onehot_transformer = Pipeline(steps=[
       ('imputer', SimpleImputer(strategy='constant'))
      ,('oheEncoder', OneHotEncoder())                                   
])

# 수치형 데이터 및 Categorical 데이터 컬럼 분리
numeric_features = ['temp', 'atemp', 'hum', 'windspeed']
ordinal_features = ['holiday', 'weekday', 'workingday', 'weathersit']
onehot_features  = ['season', 'mnth']

# numeric_features = data.select_dtypes(include=['int64', 'float64']).columns
# categorical_features = data.select_dtypes(include=['object']).drop(['Loan_Status'], axis=1).columns

preprocessor = ColumnTransformer(
   transformers=[
     ('numeric', numeric_transformer, numeric_features)
   , ('ord_categorical', ordinal_transformer, ordinal_features)
   , ('ohe_categorical', onehot_transformer, onehot_features)
])
```

## 모델 적용 파이프라인


```python
from sklearn.ensemble import RandomForestRegressor

pipeline = Pipeline(steps = [
               ('preprocessor', preprocessor) # 전처리 파이프라인
              ,('regressor', RandomForestRegressor()) # 모델 연결
           ])

rf_model = pipeline.fit(X_train, y_train)
print(rf_model)
```

    Pipeline(steps=[('preprocessor',
                     ColumnTransformer(transformers=[('numeric',
                                                      Pipeline(steps=[('imputer',
                                                                       SimpleImputer()),
                                                                      ('scaler',
                                                                       StandardScaler())]),
                                                      ['temp', 'atemp', 'hum',
                                                       'windspeed']),
                                                     ('ord_categorical',
                                                      Pipeline(steps=[('imputer',
                                                                       SimpleImputer(strategy='constant')),
                                                                      ('ordEncoder',
                                                                       OrdinalEncoder())]),
                                                      ['holiday', 'weekday',
                                                       'workingday',
                                                       'weathersit']),
                                                     ('ohe_categorical',
                                                      Pipeline(steps=[('imputer',
                                                                       SimpleImputer(strategy='constant')),
                                                                      ('oheEncoder',
                                                                       OneHotEncoder())]),
                                                      ['season', 'mnth'])])),
                    ('regressor', RandomForestRegressor())])
    

# 모델 평가


```python
from sklearn.metrics import r2_score
predictions = rf_model.predict(X_val)
print (r2_score(y_val, predictions))
```

    0.7654903256614782
    

# 다중 모형 개발


```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

regressors = [
    RandomForestRegressor(),
    DecisionTreeRegressor(),
    LinearRegression()
]

# regressors = [pipe_rf, pipe_dt]
for regressor in regressors:
    pipeline = Pipeline(steps = [
               ('preprocessor', preprocessor)
              ,('regressor',regressor)
           ])
    model = pipeline.fit(X_train, y_train)
    predictions = model.predict(X_val)
    print(regressor)
    print(f'Model r2 score:{r2_score(predictions, y_val)}')
```

    RandomForestRegressor()
    Model r2 score:0.7447806201844671
    DecisionTreeRegressor()
    Model r2 score:0.5885371412997458
    LinearRegression()
    Model r2 score:0.5703227526319388
    
