---
title: "Python Basic 4"
categories:
  - python
  - basic
tag:
  - python
  - google colab
author: "Jiwon Kang"
date: 2022-03-22 17:31:40
---

# 클래스(Class)
- 목적 : 코드의 간결화, 코드의 재사용, 유지보수 용이
- 여러 클래스가 모여서 하나의 라이브러리가 됨
  + 장고 / 웹개발 / 머신러닝 / 시각화 / 전처리
- 클래스명은 대문자로 시작해야 함



```python
class Person:

  # class attribute (선택)
  country = "korean"

  # instance attribute (필수)
  def __init__(self, name, age):
    self.name = name
    self.age = age

if __name__ == "__main__":
  kim = Person("Kim", 30)
  lee = Person("Lee", 28)
  
  # access class attribute
  print("Kim은 {}".format(kim.__class__.country))
  print("Lee는 {}".format(lee.__class__.country))
```

    Kim은 korean
    Lee는 korean
    

## 인스턴스 메서드 생성
- list.append(), list.extend()




```python
class Person:

  # class attribute (선택)
  country = "korean"

  # instance attribute (필수)
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # instance method 정의
  def singing(self, songtitle):
    return "{}: '{}' 노래를 부릅니다.".format(self.name, songtitle)

if __name__ == "__main__":
  kim = Person("Kim", 30)
  lee = Person("Lee", 28)
  
  # call instance method
  print(kim.singing("creep"))
  print(lee.singing("peaches"))
```

    Kim: 'creep' 노래를 부릅니다.
    Lee: 'peaches' 노래를 부릅니다.
    

## 클래스 상속


```python
class Parent:
  
  # init constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # instance method
  def whoAmI(self):
    print("I am Parent!")
  
  def singing(self, songtitle):
    return "{}: '{}' 노래를 부릅니다.".format(self.name, songtitle)
  
  def dancing(self):
    return "{}: 춤을 춥니다.".format(self.name)

class Child(Parent):

  # instance attribute
  def __init__(self, name, age):
    super().__init__(name, age) # 부모 클래스의 생성자 그대로 가져오기
    print("Child Class On.")
  
  # instance method
  def whoAmI(self):
    print("I am Child!")
  
  def studying(self, subject):
    return "{} : {} 공부를 합니다.".format(self.name, subject)

if __name__ == "__main__":
  child_kim = Child("kim", 13)
  parent_kim = Parent("kim", 49)
  child_kim.whoAmI()
  parent_kim.whoAmI()
  print(parent_kim.dancing())
  # print(parent_kim.studying()) -> AttributeError 발생
  print(child_kim.singing("fake love"))
  print(child_kim.studying("math"))
```

    Child Class On.
    I am Child!
    I am Parent!
    kim: 춤을 춥니다.
    kim: 'fake love' 노래를 부릅니다.
    kim : math 공부를 합니다.
    


```python
class TV:
  def __init__(self):
    # private variable (외부 접근 불가능)
    self.__maxprice = 500
  
  def sell(self):
    print("Selling Price: {}".format(self.__maxprice))
  
  # set method, get method
  def setMaxPrice(self, price):
    self.__maxprice = price
    print("Price Updated")

  def getMaxPrice(self):
    return self.__maxprice
  
if __name__=="__main__":
  tv = TV()
  tv.sell()

  # 강제로 값을 변경할 수 없음
  tv.__maxprice = 100
  tv.sell()

  # 별도의 method를 통해 변경 가능
  tv.setMaxPrice(400)
  tv.sell()
```

    Selling Price: 500
    Selling Price: 500
    Price Updated
    Selling Price: 400
    

## 클래스 내부 조건문
- init constructor


```python
class Employee:

  # init constructor
  def __init__(self, name, salary = 0):
    self.name = name

    # public variable (외부 접근 가능)
    if salary > 0:
      self.salary = salary
    else:
      self.salary = 0
      print("급여는 0원이 될 수 없습니다. 다시 입력하세요.")
  
  def update_salary(self, amount):
    self.salary += amount
  
  def weekly_salary(self):
    return int(self.salary / 7)

if __name__=="__main__":
  emp1 = Employee("David", -50000)
  print("{}의 급여는 {}원입니다.".format(emp1.name, emp1.salary))

  emp1.salary = emp1.salary + 1500
  print("{}의 급여는 {}원입니다.".format(emp1.name, emp1.salary))

  emp1.update_salary(3000)
  print("{}의 급여는 {}원입니다.".format(emp1.name, emp1.salary))

  week_salary = emp1.weekly_salary()
  print("{}의 주 급여는 {}원입니다.".format(emp1.name, week_salary))

```

    급여는 0원이 될 수 없습니다. 다시 입력하세요.
    David의 급여는 0원입니다.
    David의 급여는 1500원입니다.
    David의 급여는 4500원입니다.
    David의 주 급여는 642원입니다.
    

## 클래스 Docstring


```python
class Person:
  """
  사람을 표현하는 클래스

  ***
  Attributes
  ----------
  name: str
    Name of the person
  age: int
    Age of the person

  Methods
  -------

  info(additional=""): 
    Prints the person's name and age

  """

  def __init__(self, name, age):
    """
    Constructs all the neccessary attributes for the person object

    Parameters
    ----------
      name: str
        Name of the person
      age: int
        Age of the person
    """

    self.name = name
    self.age = age
  
  def info(self, additional=None):
    """
    Prints the person's information

    Parameters
    ----------
      additional: str, optional
        more info to be diplayed (Default is None) / A, B, C
    
    Returns
    -------
      None

    """
    print(f'My name is {self.name}. I am {self.age} years old. ' + additional)

if __name__=="__main__":
  print(Person.__doc__)
  person = Person("Jiwon", age = 27)
  person.info("I wanna be a data analyst.")
```

    
      사람을 표현하는 클래스
    
      ***
      Attributes
      ----------
      name: str
        Name of the person
      age: int
        Age of the person
    
      Methods
      -------
    
      info(additional=""): 
        Prints the person's name and age
    
      
    My name is Jiwon. I am 27 years old. I wanna be a data analyst.
    
