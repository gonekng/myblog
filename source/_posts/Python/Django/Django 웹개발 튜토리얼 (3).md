---
title: "Django 웹개발 튜토리얼 (3)"
categories:
  - python
  - django
tag:
  - python
  - django
  - development
author: "Jiwon Kang"
date: 2024-02-19 22:43:23
---

## Model 데이터 추가

> Model에 데이터를 추가하는 방법
> 
> 1. 서버 개발자가 admin 페이지에서 직접 데이터 추가하기
> 2. 서버 개발자가 django shell에서 직접 데이터 추가하기
> 3. 웹페이지 view에서 model에 DB추가하도록 요청하는 기능 구현하기

### Admin 페이지에서 직접 추가

> admin 페이지 : 사이트 운영자가 사용하는 페이지 → django에서는 기본 제공됨
> 
1. 운영자 계정(*superuser*) 생성
    - `python manage.py createsuperuser` → 이름, 이메일, 비밀번호 등 설정
        
        ![](/images/Python/Django/3/Untitled.png)
        
    - 이때, 비밀번호는 8글자 이상의 숫자와 문자를 조합하여 작성하도록 되어있음
        - Bypass 안내문에 y를 입력할 경우 그대로 진행되나, 권장하지 않음
            
            ![](/images/Python/Django/3/Untitled1.png)
            
        - 비밀번호 설정 후 *superuser* 계정 생성 완료
            
            ![](/images/Python/Django/3/Untitled2.png)
            
2. 서버 실행 후 admin 페이지 접속
    - 앞서 생성한 운영자 계정으로 로그인
        
        ![](/images/Python/Django/3/Untitled3.png)
        
    - admin 페이지에서 모델에 데이터를 직접 추가 가능
        
        → 앞서 polls에서 만든 모델을 admin 페이지에도 따로 추가해야 가능
        
        ![](/images/Python/Django/3/Untitled4.png)
        
3. admin 페이지에 모델 및 데이터 추가
    - polls/admin.py → 다음 코드 입력하여 admin 페이지에 모델 추가
        
        ```python
        from django.contrib import admin
        from .models import Question, Choice
        
        admin.site.register(Question)
        admin.site.register(Choice)
        ```
        
        ![](/images/Python/Django/3/Untitled5.png)
        
    - 각 모델(Question, Choices)에 직접 데이터 추가
        
        ![](/images/Python/Django/3/Untitled6.png)
        
        ![](/images/Python/Django/3/Untitled7.png)
        

### Django Shell에서 직접 추가

1. `python manage.py shell` 입력 (django shell 실행)
2. 다음 커맨드를 순차적으로 입력하여 Question 모델에 데이터 추가
    
    ```python
    >>> from polls.models import Choice, Question
    >>> from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())
    >>> q.save()
    ```
    
    - 앞서 저장한 데이터의 id 및 내용 확인
        
        ![](/images/Python/Django/3/Untitled8.png)
        
    - 데이터 수정 및 업데이트 가능
        
        ![](/images/Python/Django/3/Untitled9.png)
        
    - admin 페이지에서도 업데이트된 데이터 확인 가능
        
        ![](/images/Python/Django/3/Untitled10.png)
        

## Reference

- django Documentation : [https://docs.djangoproject.com/en/3.2/intro/tutorial01/](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- 참고 블로그 : [https://lucky516.tistory.com/55](https://lucky516.tistory.com/55)