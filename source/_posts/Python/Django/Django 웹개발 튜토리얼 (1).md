---
title: "Django 웹개발 튜토리얼 (1)"
categories:
  - python
  - django
tag:
  - python
  - django
  - development
author: "Jiwon Kang"
date: 2024-02-16 22:59:22
---

## Django란?

- 파이썬으로 작성된 무료 오픈 소스 웹 프레임워크
- 웹 개발을 보다 쉽게 구현할 수 있으며, 보안, 확장성, 빠른 개발을 위한 다양한 기능 제공
- Model-View-Template (MVT) 아키텍처 기반으로 이루어짐
    - 데이터베이스 구조(Model), 사용자 인터페이스(Template), 애플리케이션 로직(View)
        
        → 일반적인 MVC 패턴과 용어의 차이가 있으나 원리는 동일함
        

## Django 설치 및 서버 구동

1. python 인터프리터에서 django 설치
    - `pip install django` 입력
        
        ![](/images/Python/Django/1/Untitled.png)
        
2. 원하는 경로에 새로운 프로젝트 생성
    - `django-admin startproject mysite` 입력
        
        ![](/images/Python/Django/1/Untitled1.png)
        
3. 개발 서버 구동
    - `cd mysite` > `python manage.py makemigrations` > `python manage.py migrate` > `python manage.py runserver`
        
        ![](/images/Python/Django/1/Untitled2.png)
        
    - 이후 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)에 접속하면 다음과 같은 화면이 뜬다.
        
        ![](/images/Python/Django/1/Untitled3.png)
        

## 투표 Application 개발

> Django는 Application 단위로 웹페이지를 개발하도록 되어 있으며, Application은 프로젝트 폴더에 넣었다 뺐다 할 수 있음
> 
1. 새로운 application 생성
    - `python manage.py startapp polls` 입력
        
        ![](/images/Python/Django/1/Untitled4.png)
        
2. polls 폴더 안에 생성된 views.py 코드 작성
    
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse
    
    def index(request):
        return HttpResponse("Hello, World. You're at the polls index.")
    ```
    
    - `index()` : http 리퀘스트를 받아서 response 메시지 출력하는 함수
3. polls 폴더 안에 urls.py 생성
    
    ```python
    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
    
4. mysite 폴더 안에 있는 urls.py 코드 작성
    - 프로젝트에 application을 넣고 빼는 작업은 url 연결로 가능함
    
    ```python
    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
    ]
    ```
    
5. [http://127.0.0.1:8000/polls](http://127.0.0.1:8000/polls)에 접속하면 다음과 같은 화면 출력
    
    ![](/images/Python/Django/1/Untitled5.png)
    

## Reference

- django Documentation : [https://docs.djangoproject.com/en/3.2/intro/tutorial01/](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- 참고 블로그 : [https://lucky516.tistory.com/52](https://lucky516.tistory.com/52), [https://lucky516.tistory.com/53](https://lucky516.tistory.com/53)