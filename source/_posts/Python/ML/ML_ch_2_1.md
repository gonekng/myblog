---
title: "ML Practice 2_1"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-03-28 17:31:35
---

# ML Algorithm

## Supervised Learning(지도 학습)
- Input(입력; independent variable) & Target(타깃; dependent variable)
- Question with a correct answer
  + Type 1: Classification(분류)
  + Type 2: Regression(예측)
- Feature(특성) = independent variable(column)

## Unspervised Learning(비지도 학습)
- only Input, not Target
- Question without an answer
- algorithm automatically categorizes

# Data set


```python
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
```


```python
fish_data = [[l,w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14 # 1: bream, 0: smelt
```

# KNN 1

## Create KNN


```python
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
```

## Data Split
- train set & test set


```python
train_input = fish_data[:35]
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]
```

## Model fitting


```python
kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target) # Sampling bias
```




    0.0



# KNN 2

## Numpy array


```python
import numpy as np

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

input_arr.shape, target_arr.shape
```




    ((49, 2), (49,))



## Data Shuffle and Split


```python
np.random.seed(42)
index = np.arange(49)
print(index)
np.random.shuffle(index)
print(index)
```

    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
     24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
     48]
    [13 45 47 44 17 27 26 25 31 19 12  4 34  8  3  6 40 41 46 15  9 16 24 33
     30  0 43 32  5 29 11 36  1 21  2 37 35 23 39 10 22 18 48 20  7 42 14 28
     38]
    


```python
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]
```

## Scatter Plot


```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(train_input[:,0],train_input[:,1])
ax.scatter(test_input[:,0],test_input[:,1])
ax.set_xlabel('length')
ax.set_ylabel('weight')
plt.show()
```


    
![](/images/Python/ML/ML_ch_2_1.png)
    


## Model fitting


```python
kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target)
```




    1.0




```python
print(kn.predict(test_input) == test_target)
```

    [ True  True  True  True  True  True  True  True  True  True  True  True
      True  True]
    

*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*