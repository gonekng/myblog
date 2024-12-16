---
title: "Python Basic 1"
categories:
  - python
  - basic
tag:
  - python
  - google colab
author: "Jiwon Kang"
date: 2022-03-22 17:30:00
---

# Hello World


```python
print("Hello, World!")
```

    Hello, World!
    

# 주석 처리
- 코드 작업 시, 특정 코드에 대해 설명
- 사용자 정의 함수 작성 시, 클래스 작성 시 중요 (도움말 작성)


```python
# 한 줄 주석 처리
"""
여러 줄 주석 처리
"""

print("Hello, World!")
```

    Hello, World!
    

# 변수 (Scalar)
- 객체(OBject)로 구현이 됨
  + 하나의 자료형(Type)을 가진다.
  + 클래스(Class)로 정의된다.
    - 다양한 함수들 존재

## int
- int 정수를 표현하는 데 사용


```python
num_int = 1
num_int2 = 3
print(num_int)
print(num_int2)
print(type(num_int))
```

    1
    3
    <class 'int'>
    

## float
- 실수를 표현하는 데 사용


```python
num_float = 0.2
print(num_float)
print(type(num_float))
```

    0.2
    <class 'float'>
    

## bool
- True와 False로 나타나는 Boolean 값을 표현하는 데 사용


```python
bool_true = True
print(bool_true)
print(type(bool_true))
```

    True
    <class 'bool'>
    

## None
- Null을 나타내는 자료형으로 None이라는 한 가지 값만 가진다.


```python
none_x = None
print(none_x)
print(type(none_x))
```

    None
    <class 'NoneType'>
    

# 사칙연산


## 정수형 사칙연산


```python
a = 15 # int
b = 2 # int
print('a + b = ', a+b) # int
print('a - b = ', a-b) # int
print('a * b = ', a*b) # int
print('a / b = ', a/b) # float
print('a // b = ', a//b) # int
print('a % b = ', a%b) # int
print('a ** b = ', a**b) # int
```

    a + b =  17
    a - b =  13
    a * b =  30
    a / b =  7.5
    a // b =  7
    a % b =  1
    a ** b =  225
    

## 실수형 사칙연산


```python
a = 15.0 # float
b = 2.0 # float
print('a + b =', a+b) # float
print('a - b =', a-b) # float
print('a * b =', a*b) # float
print('a / b =', a/b) # float
print('a // b =', a//b) # float
print('a % b =', a%b) # float
print('a ** b =', a**b) # float
```

    a + b = 17.0
    a - b = 13.0
    a * b = 30.0
    a / b = 7.5
    a // b = 7.0
    a % b = 1.0
    a ** b = 225.0
    

# 논리형 연산자
- Bool형은 True와 False 값으로 정의
- AND, OR, NOT


```python
x = 5 > 4
print('x =', x)
y = 3 > 9
print('y =', y)
print('x and x =', x and x)
print('x and y =', x and y)
print('y and x =', y and x)
print('y and y =', y and y)
print('x or x =', x or x)
print('x or y =', x or y)
print('y or x =', y or x)
print('y or y =', y or y)
```

    x = True
    y = False
    x and x = True
    x and y = False
    y and x = False
    y and y = False
    x or x = True
    x or y = True
    y or x = True
    y or y = False
    

## 비교 연산자
- 부등호를 의미
- 비교 연산자를 True와 False 값을 도출

## 논리 & 비교 연산자 응용


```python
var = input("숫자를 입력하시오. :")
print(var)
print(type(var))
```

    숫자를 입력하시오. :24
    24
    <class 'str'>
    


```python
var = int(input("숫자를 입력하시오. :"))
print(var)
print(type(var))
```

    숫자를 입력하시오. :92
    92
    <class 'int'>
    


```python
num1 = int(input("숫자를 입력하시오. :"))
num2 = int(input("숫자를 입력하시오. :"))
num3 = int(input("숫자를 입력하시오. :"))
num4 = int(input("숫자를 입력하시오. :"))

var1 = num1 >= num2 
var2 = num3 < num4
print(var1 and var2)
print(var1 or var2)
```

    숫자를 입력하시오. :29
    숫자를 입력하시오. :15
    숫자를 입력하시오. :8
    숫자를 입력하시오. :10
    True
    True
    

# 문자열

## 문자열 입력 방법
- 문자열을 입력하는 4가지 방법




```python
print("Hello, World")
print('Hello, World')
print("'Hello, World'")
print('"Hello, World"')
```

    Hello, World
    Hello, World
    'Hello, World
    "Hello, World"
    

- 문자열에 작은따옴표, 큰따옴표 포함하는 방법


```python
food = "Python's favorite food is perl"
print(food)
say = '"Python is very easy." he says.'
print(say)

food2 = 'Python\'s favorite food is perl'
print(food2)
say2 = "\"Python is very easy.\" he says."
print(say2)
```

    Python's favorite food is perl
    "Python is very easy." he says.
    Python's favorite food is perl
    "Python is very easy." he says.
    

- 변수에 여러 줄의 문자열 대입


```python
multiline = "Life is too short.\nYou need python."
print(multiline)
```

    Life is too short.
    You need python.
    


```python
multiline ='''
Life is too short.
You need python
'''
print(multiline)
```

    
    Life is too short.
    You need python
    
    

## String 연산자
- 덧셈 연산자



```python
str1 = "Hello "
str2 = "World! "

print(str1 + str2)
```

    Hello World! 
    

- 곱셈 연산자



```python
greeting = str1 + str2
print(greeting * 3)
```

    Hello World! Hello World! Hello World! 
    

## Indexing
- 문자열 인덱싱은 문자열 안에서 범위를 지정하여 특정 단일 
문자 추출


```python
greeting = "Hello Kaggle!"
print(greeting[0])
print(greeting[6])
print(greeting[len(greeting)-1])
print(greeting[-1])
```

    H
    K
    !
    !
    

## Slicing
- 문자열 슬라이싱은 문자열 안에서 범위를 지정하고 특정 문자열 추출


```python
print(greeting[:])
print(greeting[:5])
print(greeting[6:])
print(greeting[3:9])
print(greeting[0:9:2])
print(greeting[6:-1])
print(greeting[::-1])
```

    Hello Kaggle!
    Hello
    Kaggle!
    lo Kag
    HloKg
    Kaggle
    !elggaK olleH
    

## Formatting

### format 코드


```python
print("I eat %d apples." % 3) # 숫자 대입
print("I eat %s apples." % "five") # 문자열 대입

num = 10
day = "three"
say = "I ate %d apples, so I was sick for %s days." % (num, day)
print(say)
```

    I eat 3 apples.
    I eat five apples.
    I ate 10 apples, so I was sick for three days.
    


```python
print("I have %s apples" % 3)
print("rate is %s" % 3.234)
print("Error is %d%%." % 98) # fomatting 연산자와 %를 함께 쓸 때는 %%
```

    I have 3 apples
    rate is 3.234
    Error is 98%.
    


```python
print("%10s,Jane!" % "hi")
print("%-10s,Jane!" % "hi")

print("'%0.4f'" % 3.42134234)
print("'%10.4f'" % 3.42134234)
print("'%-10.4f'" % 3.42134234)
```

            hi,Jane!
    hi        ,Jane!
    '3.4213'
    '    3.4213'
    '3.4213    '
    

### format 함수


```python
print("I eat {0} apples.".format(7))
print("I eat {0} apples.".format("five"))

num = 8
day = 3
print("I ate {0} apples.".format(num))
print("I ate {0} apples, so I was sick for {1} days.".format(num, day))

print("I ate {num} apples, so I was sick for {day} days.".format(num=6,day=2))
print("I ate {0} apples, so I was sick for {day} days.".format(4,day=1))
```

    I eat 7 apples.
    I eat five apples.
    I ate 8 apples.
    I ate 8 apples, so I was sick for 3 days.
    I ate 6 apples, so I was sick for 2 days.
    I ate 4 apples, so I was sick for 1 days.
    


```python
print("'{0:<10}'".format("hi"))
print("'{0:^10}'".format("hi"))
print("'{0:>10}'".format("hi"))

print("'{0:=^10}'".format("hi"))
print("'{0:!<10}'".format("hi"))
```

    'hi        '
    '    hi    '
    '        hi'
    '====hi===='
    'hi!!!!!!!!'
    


```python
y = 3.42134234
print("'{0:0.4f}'".format(y))
print("'{0:10.4f}'".format(y))
print("'{0:^10.4f}'".format(y))
print("'{0:<10.4f}'".format(y))
```

    '3.4213'
    '    3.4213'
    '  3.4213  '
    '3.4213    '
    


```python
name1 = "John"
name2 = "Marry"
print("{0} {{and}} {1}".format(name1, name2))
```

    John {and} Marry
    

### f 문자열


```python
name = 'Sally'
age = 29
print(f"My name is {name}, and I'm {age} years old.")
print(f"Next year, I'm going to be {age+1} years old.")

d = {'name':'Sally', 'age':29}
print(f"My name is {d['name']}, and I'm {d['age']} years old.") # 딕셔너리 자료형 활용
```

    My name is Sally, and I'm 29 years old.
    Next year, I'm going to be 30 years old.
    My name is Sally, and I'm 29 years old.
    


```python
print(f'{"hi":<10}')
print(f'{"hi":^10}')
print(f'{"hi":>10}')

print(f'{"hi":=^10}')
print(f'{"hi":!<10}')
```

    hi        
        hi    
            hi
    ====hi====
    hi!!!!!!!!
    


```python
y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')
print(f'{y:^10.4f}')
print(f'{y:<10.4f}')
```

    3.4213
        3.4213
      3.4213  
    3.4213    
    


```python
name1 = "John"
name2 = "Marry"
print(f"{name1} {{and}} {name2}")
```

    John {and} Marry
    

## 문자열 함수


```python
# count
a = 'hobby'
print(a.count('b'))

# find, index
a = "Python is the best choice"
print(a.find("b"))
print(a.find("k")) # 없으면 -1 반환
print(a.index("t"))
# print(a.index("k")) # 없으면 에러
```

    2
    14
    -1
    2
    


```python
# join
print(",".join('abcdefg'))

# upper, lower
a = "Hello"
print(a.upper())
print(a.lower())

# lstrip, rstrip, strip
a = "    OK    "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
```

    a,b,c,d,e,f,g
    HELLO
    hello
    OK    
        OK
    OK
    


```python
# replace
a = "That's right!"
print(a.replace('right', 'wrong'))

# split
a = "I Love You"
print(a.split()) # 공백 기준
b = "a:b:c:d"
print(b.split(':')) # 특정 구분자 기준
```

    That's wrong!
    ['I', 'Love', 'You']
    ['a', 'b', 'c', 'd']
    
