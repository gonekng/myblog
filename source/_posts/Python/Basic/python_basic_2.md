---
title: "Python Basic 2"
categories:
  - python
  - tutorial
tag:
  - python
  - google colab
author: "Jiwon Kang"
date: 2022-03-22 17:30:50
---

# 리스트
- 시퀀스 데이터 타입
- 데이터에 순서가 존재하며, 인덱싱 및 슬라이싱 가능
- 대괄호('[값1, 값2, 값3]')를 사용하여 표현



```python
a = [] # 빈 리스트
a_func = list() # 함수를 통해 생성
b = [1]
c = ['apple']
d = [1,2,['apple']] # 리스트 안에 리스트

print(a)
print(a_func)
print(b)
print(c)
print(d)

print(type(d))
```

    []
    []
    [1]
    ['apple']
    [1, 2, ['apple']]
    <class 'list'>
    

## 리스트 Indexing, Slicing


```python
a = [1,2,3,4,5,6,7,8,9,10]
print(a)

print(a[0])
print(a[5])
print(a[:5])
print(a[8:])
print(a[3:9:2])
print(a[:-3:3])
print(a[::-1])
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    1
    6
    [1, 2, 3, 4, 5]
    [9, 10]
    [4, 6, 8]
    [1, 4, 7]
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    


```python
a = [["apple", "banana", "cherry"], 10]
print(a[0])
print(a[0][1])
print(a[0][2][2])
```

    ['apple', 'banana', 'cherry']
    banana
    e
    

## 리스트 연산자 사용


```python
a = ["john", "evan"]
b = ["alice", "eva"]

c = a + b # 리스트가 하나로 합쳐짐
print(c)
```

    ['john', 'evan', 'alice', 'eva']
    


```python
c = a * 3
d = b * 0
print("a * 3 =", c) # 숫자만큼 반복
print("b * 0 =", d) # 빈 리스트 출력
```

    a * 3 = ['john', 'evan', 'john', 'evan', 'john', 'evan']
    b * 0 = []
    

## 리스트 수정 및 삭제


```python
a = [0, 1, 2]
a[1] = 'b'
print(a)
```

    [0, 'b', 2]
    

### 리스트 값 추가


```python
a = [100,200,300]
a.append(400)
print(a)

a.append([500,600]) # 리스트 자체를 요소로 추가
print(a)
```

    [100, 200, 300, 400]
    [100, 200, 300, 400, [500, 600]]
    


```python
a = [100,200,300]
a.append(400)
print(a)

a.extend([500,600]) # 리스트의 값들을 요소로 추가
print(a)
```

    [100, 200, 300, 400]
    [100, 200, 300, 400, 500, 600]
    


```python
a = [0,1,2]
a.insert(1, 100) # 원하는 위치에 원하는 값 추가
print(a)
```

    [0, 100, 1, 2]
    

### 리스트 값 삭제


```python
a = [4,3,2,1,"A"]
a.remove(1) # 해당되는 값 제거 
a.remove("A")
print(a)
```

    [4, 3, 2]
    


```python
a = [1,2,3,4,5,6,7,8,9,10]
del a[1] # 인덱스 번호를 이용하여 제거
print(a)

del a[1:5]
print(a)
```

    [1, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 7, 8, 9, 10]
    


```python
b = ["a", "b", "c", "d", "e"]
x = b.pop(2)
print(x)
print(b)
y = b.pop() # 인덱스를 지정하지 않으면 마지막 요소 추출 및 제거
print(y)
print(b)
```

    c
    ['a', 'b', 'd', 'e']
    e
    ['a', 'b', 'd']
    

### 그 외 메서드


```python
a = [0,1,2,3]
print(a)

a.clear()
print(a)
```

    [0, 1, 2, 3]
    []
    


```python
a = ["a","a","b","b"]
print(a.index("b")) # 해당 요소가 처음으로 등장하는 위치
```

    2
    


```python
a = [1,4,5,2,3]
b = [1,4,5,2,3]

a.sort() # 오름차순
print(a)

b.sort(reverse=True) # 내림차순
print(b)
```

    [1, 2, 3, 4, 5]
    [5, 4, 3, 2, 1]
    


```python
c = ['d','bye','five','a']
d = ['d','bye','five','a']

c.sort()
print(c)

d.sort(reverse=True)
print(d)
```

    ['a', 'bye', 'd', 'five']
    ['five', 'd', 'bye', 'a']
    

# 튜플
- 리스트와 비슷한 형태로 Indexing, Slicing 가능
- 리스트와 달리 수정 및 삭제가 안 됨
- 소괄호('(값1, 값2, 값3)')를 사용하여 표현


```python
tuple1 = (0) # 끝에 comma(,)를 붙이지 않으면 int 자료형
tuple2 = (0,) # 끝에 comma(,)를 붙여야 tuple 자료형
tuple3 = 0, 1, 2
print(tuple1)
print(type(tuple1))
print(tuple2)
print(type(tuple2))
print(tuple3)
print(type(tuple3))
```

    0
    <class 'int'>
    (0,)
    <class 'tuple'>
    (0, 1, 2)
    <class 'tuple'>
    


```python
a = (0,1,2,3,'a')
print(type(a))

# del a[4] : 튜플에서는 수정, 삭제 안 됨
b = list(a)
print(b)
b[1] = 'b'
a = tuple(b)
print(a)
```

    <class 'tuple'>
    [0, 1, 2, 3, 'a']
    (0, 'b', 2, 3, 'a')
    

## 튜플 Indexing, Slicing


```python
a = (0,1,2,3,'a')
print(type(a))

print(a[1])
print(a[-2])
print(a[1:3])
print(a[::2])
```

    <class 'tuple'>
    1
    3
    (1, 2)
    (0, 2, 'a')
    

## 튜플 연산자 사용


```python
t1 = (0,1,2)
t2 = ("a", "b", "c")

print(t1 + t2)
print(t1 * 3)
print(t1 * 0)
```

    (0, 1, 2, 'a', 'b', 'c')
    (0, 1, 2, 0, 1, 2, 0, 1, 2)
    ()
    

# 딕셔너리
- Key와 Value로 구분됨
- 중괄호({'키1':'값1', '키2':'값2'})를 사용하여 표현


```python
dict_01 = {'teacher' : 'evan',
           'class' : '601호',
           'open' : '2022-03-10',
           'students' : 24,
           'names' : ['A', 'B', 'R', 'Z']}
print(dict_01['teacher'])
print(dict_01['open'])
print(dict_01['names'])
```

    evan
    2022-03-10
    ['A', 'B', 'R', 'Z']
    


```python
print(dict_01.keys())
print(type(dict_01.keys()))
print(list(dict_01.keys())) # 다양한 연산과 메서드를 적용할 수 있는 리스트형으로 변환
```

    dict_keys(['teacher', 'class', 'open', 'students', 'names'])
    <class 'dict_keys'>
    ['teacher', 'class', 'open', 'students', 'names']
    


```python
print(dict_01.values())
print(type(dict_01.values()))
print(list(dict_01.values())) # 다양한 연산과 메서드를 적용할 수 있는 리스트형으로 변환
```

    dict_values(['evan', '601호', '2022-03-10', 24, ['A', 'B', 'R', 'Z']])
    <class 'dict_values'>
    ['evan', '601호', '2022-03-10', 24, ['A', 'B', 'R', 'Z']]
    


```python
dict_01.items() # 각 key와 value가 튜플 형태로 출력됨
```




    dict_items([('teacher', 'evan'), ('class', '601호'), ('open', '2022-03-10'), ('students', 24), ('names', ['A', 'B', 'R', 'Z'])])




```python
print(dict_01.get("teacher"))
# print(dict_01['선생님'])
print(dict_01.get("선생님")) # key가 없으면 None을 반환
print(dict_01.get("선생님", "없음")) # key가 없을 때 대체값 지정 가능
print(dict_01.get("class"))

# 그냥 값을 출력해도 되지만, get 메서드를 사용하면 key가 없더라도 에러 없이 출력 가능
```

    evan
    None
    없음
    601호
    

# 조건문 & 반복문

## 조건문


```python
weather = '맑음'
if weather == "비":
  print("우산을 가져간다.")
else:
  print("우산을 가져가지 않는다.")
```

    우산을 가져가지 않는다.
    


```python
# 60점 이상 합격
score = int(input("점수를 입력하시오. : "))

if score >= 60:
  print("합격입니다.")
else:
  print("불합격입니다.")
```

    점수를 입력하시오. : 50
    불합격입니다.
    


```python
# 90점 이상은 A, 80점 이상은 B, 70점 이상은 C, 나머지는 F
score = int(input("점수를 입력하시오. : "))
grade = ""

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"
  
print(grade)
```

    점수를 입력하시오. : 68
    D
    

## 반복문


```python
for i in range(4):
  print(i+1, "안녕하세요!")
```

    1 안녕하세요!
    2 안녕하세요!
    3 안녕하세요!
    4 안녕하세요!
    


```python
count = range(5)
print(count)

for n in count:
  print(str(n+1) + "번째")
  if (n+1) == 3:
    print("stop!")
    break
  print("shoot!")
```

    range(0, 5)
    1번째
    shoot!
    2번째
    shoot!
    3번째
    stop!
    


```python
a = "hello"

for x in a:
  if x=='l':
    break
  
  print(x)
```

    h
    e
    

- 반복문 작성 방식 : zip, range, enumerate, len, etc


```python
alphabets = ['A', 'B', 'C']

# enumerate는 인덱스와 값을 튜플 형태로 묶어주는 객체
for i, value in enumerate(alphabets):
  print(i, value)
```

    0 A
    1 B
    2 C
    
