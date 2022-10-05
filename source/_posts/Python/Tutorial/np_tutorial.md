---
title: "Numpy tutorial"
categories:
  - python
  - tutorial
tag:
  - python
  - numpy
  - google colab
author: "Jiwon Kang"
date: 2022-03-24 11:51:00
---
  
# 파이썬 라이브러리 설치
in R (코드에서 실행)
  - install.package("패키지명")
  - library(패키지명)

in Python (터미널에서 실행)
  - 방법1. conda 설치 (주 사용목적: 데이터 과학)
    + 아나콘다 설치 후에 conda 설치 가능
  - 방법2. pip 설치 (개발, 데이터 과학, 그 외)
    + 아나콘다 없이도 python만 설치하면 됨

# NumPy 라이브러리
- 파이썬의 대표적인 배열 라이브러리
- 파이썬 수치 연산과 관련된 모든 라이브러리의 기본
  + scikit learn, TensorFlow, PyTorch 등등
- .array, .reshape, .matlib 등등 다양한 메서드 활용

## Numpy 라이브러리 불러오기


```python
import numpy as np
print(np.__version__)
```

    1.21.5
    

# NumPy 배열 생성

## 리스트를 배열로 변환
- NumPy 배열로 변환하여 저장


```python
temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(temp)
print(type(temp))

arr = np.array(temp)
print(arr)
print(type(arr))
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    <class 'list'>
    [ 1  2  3  4  5  6  7  8  9 10]
    <class 'numpy.ndarray'>
    

- NumPy 배열에도 인덱싱, 슬라이싱 동일하게 적용


```python
print(arr[4])
print(arr[3:7])
print(arr[::2])
```

    5
    [4 5 6 7]
    [1 3 5 7 9]
    

- NumPy를 통한 기초 통계 함수 사용


```python
print("sum:", np.sum(arr))
print("mean:", np.mean(arr))
print("median:", np.median(arr))
print("min:", np.min(arr))
print("max:", np.max(arr))
print("std:", np.std(arr))
```

    sum: 55
    mean: 5.5
    median: 5.5
    min: 1
    max: 10
    std: 2.8722813232690143
    

## 사칙연산


```python
math_scores = [90, 80, 88]
english_scores = [80, 70, 90]
total_scores = math_scores + english_scores # 단순한 리스트 연결 수행
print(total_scores)

math_arr = np.array(math_scores)
english_arr = np.array(english_scores)
total_arr = math_arr + english_arr # 각 요소의 덧셈 수행
print(total_arr)
```

    [90, 80, 88, 80, 70, 90]
    [170 150 178]
    


```python
arr1 = np.array([2, 5, 4])
arr2 = np.array([4, 2, 3])

# 사칙연산
print("덧셈:", np.add(arr1, arr2))
print("뺄셈:", np.subtract(arr1, arr2))
print("곱셈:", np.multiply(arr1, arr2))
print("나눗셈:", np.divide(arr1, arr2))
print("거듭제곱:", np.power(arr1, arr2))
```

    덧셈: [6 7 7]
    뺄셈: [-2  3  1]
    곱셈: [ 8 10 12]
    나눗셈: [0.5        2.5        1.33333333]
    거듭제곱: [16 25 64]
    

## 소수점 처리


```python
# 소수점 절삭
temp_arr = np.trunc([-1.23, 1.23])
print(temp_arr)

temp_arr = np.fix([-1.23, 1.23])
print(temp_arr)
```

    [-1.  1.]
    [-1.  1.]
    


```python
# 올림
temp_arr = np.ceil([-1.23789, 1.23789])
print(temp_arr)

# 내림
temp_arr = np.floor([-1.23789, 1.23789])
print(temp_arr)

# 반올림
temp_arr = np.around([-1.23789, 1.23789], 2)
print(temp_arr)

temp_arr = np.around([-1.23789, 1.23789], 4)
print(temp_arr)
```

    [-1.  2.]
    [-2.  1.]
    [-1.24  1.24]
    [-1.2379  1.2379]
    

## 배열의 형태 및 차원
- 0차원부터 3차원까지 생성하는 방법
- .shape : axis 축 기준으로 배열의 형태 반환


```python
# 0차원 배열
temp_arr = np.array(20)
print(temp_arr)
print(type(temp_arr))
print("배열의 형태:", temp_arr.shape)
print("배열의 차원:", temp_arr.ndim)
```

    20
    <class 'numpy.ndarray'>
    배열의 형태: ()
    배열의 차원: 0
    


```python
# 1차원 배열
temp_arr = np.array([1,2,3,5])
print(temp_arr)
print(type(temp_arr))
print("배열의 형태:", temp_arr.shape)
print("배열의 차원:", temp_arr.ndim)
```

    [1 2 3 5]
    <class 'numpy.ndarray'>
    배열의 형태: (4,)
    배열의 차원: 1
    


```python
# 2차원 배열
temp_arr = np.array([[1,2,3,5],[4,5,1,6],[9,0,2,3]])
print(temp_arr)
print(type(temp_arr))
print("배열의 형태:", temp_arr.shape)
print("배열의 차원:", temp_arr.ndim)
```

    [[1 2 3 5]
     [4 5 1 6]
     [9 0 2 3]]
    <class 'numpy.ndarray'>
    배열의 형태: (3, 4)
    배열의 차원: 2
    


```python
# 3차원 배열
temp_arr = np.array([[[1,2,3,5],[4,5,1,6],[9,0,2,3]],
                     [[1,1,2,3],[2,3,1,7],[4,9,5,6]]])
print(temp_arr)
print(type(temp_arr))
print("배열의 형태:", temp_arr.shape)
print("배열의 차원:", temp_arr.ndim)
```

    [[[1 2 3 5]
      [4 5 1 6]
      [9 0 2 3]]
    
     [[1 1 2 3]
      [2 3 1 7]
      [4 9 5 6]]]
    <class 'numpy.ndarray'>
    배열의 형태: (2, 3, 4)
    배열의 차원: 3
    


```python
# parameter를 활용한 배열의 최소 차원 명시
temp_arr = np.array([1,2,3,4], ndmin=2)
print(temp_arr)
print(type(temp_arr))
print("배열의 형태:", temp_arr.shape)
print("배열의 차원:", temp_arr.ndim)
```

    [[1 2 3 4]]
    <class 'numpy.ndarray'>
    배열의 형태: (1, 4)
    배열의 차원: 2
    

## 배열을 생성하는 다양한 방법


```python
temp_arr = np.arange(5) # [0:4]
print(temp_arr)

temp_arr = np.arange(1,11,3) # [1:11:3]
print(temp_arr)
```

    [0 1 2 3 4]
    [ 1  4  7 10]
    


```python
zero_arr = np.zeros((2,3)) # 0으로만 이루어진 배열
print(zero_arr)
print(type(zero_arr))
print("데이터 타입:", zero_arr.dtype)
```

    [[0. 0. 0.]
     [0. 0. 0.]]
    <class 'numpy.ndarray'>
    데이터 타입: float64
    


```python
temp_arr = np.ones((2,3)) # 1로만 이루어진 배열
print(temp_arr)
print(type(temp_arr))
print("데이터 타입:", temp_arr.dtype)

temp_arr = np.ones((2,3), dtype="int32") # 자체적인 데이터 형변환
print(temp_arr)
print(type(temp_arr))
print("데이터 타입:", temp_arr.dtype)
```

    [[1. 1. 1.]
     [1. 1. 1.]]
    <class 'numpy.ndarray'>
    데이터 타입: float64
    [[1 1 1]
     [1 1 1]]
    <class 'numpy.ndarray'>
    데이터 타입: int32
    


```python
temp_arr = np.ones((2,6))
print(temp_arr)
print("배열의 형태:", temp_arr.shape)
print("배열의 차원:", temp_arr.ndim)
print("\n")

temp_res = temp_arr.reshape(3,4)
print(temp_res)
print("배열의 형태:", temp_res.shape)
print("배열의 차원:", temp_res.ndim)
print("\n")

temp_res2 = temp_arr.reshape(2,2,3)
print(temp_res2)
print("배열의 형태:", temp_res2.shape)
print("배열의 차원:", temp_res2.ndim)
```

    [[1 1 1 1 1 1]
     [1 1 1 1 1 1]]
    배열의 형태: (2, 6)
    배열의 차원: 2
    
    
    [[1 1 1 1]
     [1 1 1 1]
     [1 1 1 1]]
    배열의 형태: (3, 4)
    배열의 차원: 2
    
    
    [[[1 1 1]
      [1 1 1]]
    
     [[1 1 1]
      [1 1 1]]]
    배열의 형태: (2, 2, 3)
    배열의 차원: 3
    


```python
temp_arr = np.ones((12,6))
temp_res = temp_arr.reshape(3,-1)
print(temp_res)
print("배열의 형태:", temp_res.shape)
print("배열의 차원:", temp_res.ndim)

# temp_res2 = temp_arr.reshape(5,-1)
# ValueError: cannot reshape array of size 72 into shape (5,newaxis)
```

    [[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
     [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
     [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]]
    배열의 형태: (3, 24)
    배열의 차원: 2
    

# NumPy 조건식
- 조건식이 하나일 때: np.where


```python
temp_arr = np.arange(10)
print(temp_arr)

# 5보다 큰 값은 기존 값 * 10
print(np.where(temp_arr > 5, temp_arr * 10, temp_arr))
```

    [0 1 2 3 4 5 6 7 8 9]
    [ 0  1  2  3  4  5 60 70 80 90]
    


```python
temp_arr = np.arange(21)
print(temp_arr)

# 10보다 작은 값은 기존 값 * 10
print(np.where(temp_arr < 10, temp_arr * 10, temp_arr))
```

    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
    [ 0 10 20 30 40 50 60 70 80 90 10 11 12 13 14 15 16 17 18 19 20]
    

- 조건식이 2개 이상일 때: np.select


```python
temp_arr = np.arange(10)
print(temp_arr)

# 5보다 큰 값은 기존 값 * 2, 2보다 작은 값은 기존 값 + 100
condlist = [temp_arr > 5, temp_arr < 2] # The list of conditions
choicelist = [temp_arr * 2, temp_arr + 100] # The list of outputs
np.select(condlist, choicelist, default = temp_arr)
```

    [0 1 2 3 4 5 6 7 8 9]
    




    array([100, 101,   2,   3,   4,   5,  12,  14,  16,  18])



# NumPy Broadcasting
- 서로 다른 크기의 배열을 계산할 때의 기본적인 규칙
- url : https://numpy.org/doc/stable/user/basics.broadcasting.html?highlight=broadcasting


```python

```
