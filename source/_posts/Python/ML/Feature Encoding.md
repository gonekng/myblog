---
title: "Feature Encoding"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - scikit-learn
author: "Jiwon Kang"
date: 2022-12-22 23:21:54
---

## 데이터 인코딩

Scikit-learn 알고리즘은 수치형 변수만 입력값으로 허용하기 때문에,  
머신러닝을 위해서는 모든 문자열 데이터를 인코딩하여 수치형으로 변환해야 한다.

일반적으로 문자열 데이터는 범주형 데이터와 텍스트 데이터를 의미하는데,  
범주형 데이터는 각 범주에 대응하는 수치형 변수로 변환하는 것이 효과적이지만  
텍스트 데이터는 구분자 역할이거나 추가적인 정보를 제공하기 위한 경우가 많다.

이런 경우에는 머신러닝 수행에 있어서 불필요할 가능성이 높으므로  
형식적인 인코딩보다는 변수의 특성을 잘 살펴본 후 삭제하는 것이 좋다.

머신러닝을 위한 대표적인 인코딩 방식으로는  
**Label Encoding**(레이블 인코딩)과 **One-Hot Encoding**(원-핫 인코딩)이 있다.

<br>


## Label Encoding

레이블 인코딩은 간단하게 문자열 값을 각 범주에 해당하는 숫자로 변환하는 방식이다.

하지만 이는 단순히 구분을 위한 숫자이기 때문에  
일부 알고리즘에서는 각 숫자를 가중치로 해석하여 값을 왜곡하고  
결과적으로 모델의 예측 성능이 떨어지는 경우도 발생한다.

따라서 레이블 인코딩은 선형 회귀와 같은 알고리즘에는 적용하지 않는 것이 좋다.  
반면 트리 계열의 비선형 알고리즘은 이러한 특성을 반영하지 않으므로 적용해도 좋다.

- `Scikit-learn`의 `LabelEncoder`를 활용한다.
    
    ```python
    from sklearn.preprocessing import LabelEncoder
    
    cities = ['Seoul', 'LA', 'Paris', 'Tokyo', 'LA', 'London', 'Seoul', 'Berlin']
    encoder = LabelEncoder()
    encoder.fit(cities)
    labels = encoder.transform(cities)
    print(labels)
    
    # [4 1 3 5 1 2 4 0]
    ```
    
- `classes_` 속성을 통해 각 숫자가 가리키는 범주를 알 수 있다.
    
    ```python
    print(encoder.classes_)
    
    # ['Berlin' 'LA' 'London' 'Paris' 'Seoul' 'Tokyo']
    ```
    
- `inverse_transform` 속성을 통해 역변환 할 수 있다.
    
    ```python
    print(encoder.inverse_transform([1,4,5,0,2,3]))
    
    # ['LA' 'Seoul' 'Tokyo' 'Berlin' 'London' 'Paris']
    ```

<br>

## One-Hot Encoding

원-핫 인코딩은 각 범주에 대응되는 새로운 변수를 추가하여  
해당 범주에 대응하는 칼럼에만 1을 표시하고 나머지는 0을 표시하는 방식이다. 

![](/images/Python/ML/Feature_Encoding.png)

따라서 인코딩에 앞서 모든 문자열 값이 숫자형으로 변환되어야 하며,  
Encoder의 입력 값으로 2차원 데이터가 필요하다.

단, 범주가 많을 경우 과도하게 많은 변수가 생성될 수 있기 때문에  
상황에 맞게 레이블 인코딩과 적절하게 혼용하는 것이 좋다.

- `Scikit-learn`의 `OneHotEncoder` 클래스
    
    ```python
    from sklearn.preprocessing import OneHotEncoder
    import numpy as np
    
    cities = ['Seoul', 'LA', 'Paris', 'Tokyo', 'LA', 'London', 'Seoul', 'Berlin']
    
    #Step1: 모든 문자를 숫자형으로 변환합니다.
    encoder = LabelEncoder()
    encoder.fit(cities)
    labels = encoder.transform(cities)
    
    #Step2: 2차원 데이터로 변환합니다.
    labels = labels.reshape(-1, 1)
    
    #Step3: One-Hot Encoding 적용합니다.
    oh_encoder = OneHotEncoder()
    oh_encoder.fit(labels)
    oh_labels = oh_encoder.transform(labels)
    print(oh_labels.toarray())
    print(oh_labels.shape)
    
    # [[0. 0. 0. 0. 1. 0.]
    #  [0. 1. 0. 0. 0. 0.]
    #  [0. 0. 0. 1. 0. 0.]
    #  [0. 0. 0. 0. 0. 1.]
    #  [0. 1. 0. 0. 0. 0.]
    #  [0. 0. 1. 0. 0. 0.]
    #  [0. 0. 0. 0. 1. 0.]
    #  [1. 0. 0. 0. 0. 0.]]
    
    # (8, 6)
    ```
    
- `Pandas`의 `get_dummies` 함수
    
    ```python
    import pandas as pd
    
    cities = ['Seoul', 'LA', 'Paris', 'Tokyo', 'LA', 'London', 'Seoul', 'Berlin']
    
    df = pd.DataFrame({'item':cities})
    print(pd.get_dummies(df))
    ```
    
<br>

### Reference
[데이터 전처리하기 : 레이블 인코딩 (Label Encoding), 원-핫 인코딩(One-Hot Encoding), get_dummies()를 Pandas에서 사용하기](https://nicola-ml.tistory.com/62)