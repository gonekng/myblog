---
title: "Python Basic 3"
categories:
  - python
  - basic
tag:
  - python
  - google colab
author: "Jiwon Kang"
date: 2022-03-22 17:31:10
---

# 기초 문법 리뷰

## 리스트, 튜플, 딕셔너리


```python
# 리스트
book_list = ['A', 'B', 'C']
print(book_list)
# append, extend, insert, remove, pop, etc

# 튜플
book_tuple = ('A', 'B', 'C')
print(book_tuple)
# 수정, 삭제 불가능

# 딕셔너리
book_dictionary = {"title" : ["A", "B"], "year" : [2011, 2002]}
print(book_dictionary)
# keys(), values(), items(), get()
```

    ['A', 'B', 'C']
    ('A', 'B', 'C')
    {'title': ['A', 'B'], 'year': [2011, 2002]}
    

## 조건문 & 반복문


```python
if True:
  print("코드 실행") # 들여쓰기 주의
elif True:
  print("코드 실행")
else:
  print("코드 실행")
```


```python
for i in range(3):
  print(i+1, "안녕하세요")
```

    1 안녕하세요
    2 안녕하세요
    3 안녕하세요
    


```python
book_list = ["R", "Python"]
for book in book_list:
  print(book, end=" ")
print("\n")

strings01 = "Hello"
for char in strings01:
  print(char, end=" ")

num_tuple = (1, 2, 3, 4)
for num in num_tuple:
  print(num, end=" ")
print("\n")

num_dict = {"A":1, "B":2}
for num in num_dict:
  print(num, end=" ") # key 값
  print(num_dict[num], end=" ") # value 값
```

    R Python 
    
    H e l l o 1 2 3 4 
    
    A 1 B 2 

### 반복문의 필요성


```python
name_list = ["요구르트", "우유", "콜라", "사이다", "과자"]
price_list = [1000, 1500, 1200, 1200, 1000]
quantity_list = [5, 3, 1, 2, 4]


for i in range(len(name_list)):
  name = name_list[i]
  sales = price_list[i] * quantity_list[i]
  print(name + "의 매출액 : " + str(sales) + "원")
```

    요구르트의 매출액 : 5000원
    우유의 매출액 : 4500원
    콜라의 매출액 : 1200원
    사이다의 매출액 : 2400원
    과자의 매출액 : 4000원
    

### while
- 조건식이 들어간 반복문



```python
count = 5
while count > 0:
  print(count, "안녕하세요.")
  count = count - 1
```

    5 안녕하세요.
    4 안녕하세요.
    3 안녕하세요.
    2 안녕하세요.
    1 안녕하세요.
    

# 리스트 컴프리핸션
- for-loop 반복문을 한 줄로 처리


```python
letters = []
for char in "helloworld":
  letters.append(char)
print("for-loop 반복문 사용 :")
print("\t", letters)

letters2 = [char for char in "helloworld"]
print("리스트 컴프리핸션 사용 :")
print("\t", letters2)
```

    for-loop 반복문 사용 :
    	 ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    리스트 컴프리핸션 사용 :
    	 ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    


```python
# 중첩 리스트를 단일 리스트로
my_list = [[10],[20,30]]
print(my_list)

# for-loop 중첩 반복문 사용
flattened_list1 = []
for value_list in my_list:
  for value in value_list:
    flattened_list1.append(value)
print("중첩 반복문 사용 :", flattened_list1)

# 리스트 컴프리핸션 사용
flattened_list2 = [value for value_list in my_list for value in value_list]
print("리스트 컴프리핸션 사용 :", flattened_list2)
```

    [[10], [20, 30]]
    중첩 반복문 사용 : [10, 20, 30]
    리스트 컴프리핸션 사용 : [10, 20, 30]
    

# 사용자 정의 함수


```python
def plus(a,b):
  c = a + b
  return c

def minus(a,b):
  c = a - b
  return c

def multiply(a,b):
  c = a * b
  return c

def divide(a,b):
  c = a / b
  return c

print(plus(1,5))
print(minus(10,3))
print(multiply(2,4))
print(divide(8,2))
```

    6
    7
    8
    4.0
    

- basic.py로 저장할 때 예시


```python
!which python
```

    /usr/local/bin/python
    


```python
# /usr/local/bin/python
# -*- coding: utf-8 -*-

def add(a, b):
  c = a + b
  return c

if __name__ == "__main__":
  a = 1
  b = 2
  c= add(a, b)
  print(c)

```

    3
    

## 파이썬 함수 주석 처리
- Docstring(문서화)


```python
# /usr/local/bin/python
# -*- coding: utf-8 -*-

def temp(content, letter):
  """
  content 안에 있는 문자를 세는 함수입니다.
  
  Args:
    content(str) : 탐색 문자열
    letter(str) : 찾을 문자열
  
  Returns:
    int
  """
  print("함수 테스트")

  cnt = len([char for char in content if char == letter])
  return cnt

if __name__ == "__main__":
  # help(temp)
  print(temp.__doc__)

```

    
      content 안에 있는 문자를 세는 함수입니다.
      
      Args:
        content(str) : 탐색 문자열
        letter(str) : 찾을 문자열
      
      Returns:
        int
      
    


```python
def mean_and_median(value_list):
  """
  숫자 리스트 요소들의 평균과 중간값을 구하는 함수

  Args:
    value_list (iterable of int / float) : A list of int numbers
  
  Returns:
    tuple(float, float)
  """

  # 평균
  mean = sum(value_list) / len(value_list)
  
  # 중간값
  midpoint = int(len(value_list) / 2)
  if len(value_list) % 2 == 0:
    median = (value_list[midpoint - 1] + value_list[midpoint]) / 2
  else:
    median = value_list[midpoint]

  return mean, median

if __name__ == "__main__":
  value_list = [1, 1, 2, 2, 3, 4, 5]
  avg, median = mean_and_median(value_list)
  print("avg:", avg)
  print("median:", median)
```

    avg: 2.5714285714285716
    median: 2
    


```python
def calculation(num1,num2):
  """
  두 수에 대한 사칙연산을 수행하는 함수

  Args:
    num1 : float number
    num2 : float number
  
  Returns:
    tuple(float, float, float, float)
  """

  # 덧셈
  plus_num = num1 + num2
  # 뺄셈
  minus_num = num1 - num2
  # 곱셈
  multiply_num = num1 * num2
  # 나눗셈(소수점 둘째 자리까지)
  divide_num = round(num1 / num2, 2)

  return plus_num, minus_num, multiply_num, divide_num

if __name__ == "__main__":
  num1 = 13
  num2 = 7
  plus, minus, multiply, divide = calculation(num1, num2)
  print("+ :", plus)
  print("- :", minus)
  print("* :", multiply)
  print("/ :", divide)
```

    + : 20
    - : 6
    * : 91
    / : 1.86
    

- 이터레이터, 제너레이터, 데코레이터
- 변수명 immutable or mutable, context manager
