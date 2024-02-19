---
title: "Django 웹개발 튜토리얼 (2)"
categories:
  - python
  - django
tag:
  - python
  - django
  - development
author: "Jiwon Kang"
date: 2024-02-16 23:23:08
---

## Model 생성

- polls/model.py 작성
    
    ```python
    from django.db import models
    
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
    
    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
    ```
    
- Question : 질문내용, 발행일자 모델
- Choice : 질문내용, 선택내용, 투표번호 모델
- Question과 Choice는 외래키로 연결되며, Question이 삭제되면 Choice도 함께 삭제되도록 설정
    - `CharField` : 문자열 데이터 필드
    - `DateTimeField` : 날짜 및 시간 데이터 필드
    - `IntegerField` : 정수형 숫자 데이터 필드

## Model 활성화

> 프로젝트에 Application을 넣을 때, url 연결 외에도 Application의 모델을 프로젝트 모델 스키마에 연결해야 하는 작업 필요
> 
1. mysite/settings.py에 있는 `INSTALLED_APPS` 리스트에 투표 Application 등록
    - 투표 Application의 클래스 이름은 polls/apps.py에서 확인가능 → `PollsConfig`
        
        ![](/images/Python/Django/2/Untitled.png)
        
        ![](/images/Python/Django/2/Untitled1.png)
        
2. **Migration** : 기존 프로젝트의 모델에 Application 모델을 이식시키는 과정
    - **makemigrations** : `python manage.py makemigrations polls` 입력
        
        ![](/images/Python/Django/2/Untitled2.png)
        
    - polls 폴더 안에 migrations 폴더와 0001_initial.py가 생성됨
        
        ![](/images/Python/Django/2/Untitled3.png)
        
    - **migrate** : `python manage.py migrate` 입력
        
        ![](/images/Python/Django/2/Untitled4.png)
        

### makemigrations와 migrate의 차이

- **migration**은 sql로 진행됨 → 0001_initial.py와 같이 파이썬으로 표현한 다음(**makemigrations**), 이를 바탕으로 다시 sql로 변환하여 프로젝트에 반영함(**migrate**)
    - **makemigrations** : application의 모델에 대한 변화를 기록
    - **migrate** : makemigrations의 변화 기록을 보고 실제로 프로젝트 모델 스키마에 application의 모델에 대한 변화를 반영
- 이후 모델링을 수정하고 migration 작업을 실시하면 0002, 0003… 등의 파이썬 파일이 쌓이게 됨
- 실제 이행되는 sql 쿼리 확인 : `python manage.py sqlmigrate polls 변경기록번호`
    
    ![](/images/Python/Django/2/Untitled5.png)


## Reference

- django Documentation : [https://docs.djangoproject.com/en/3.2/intro/tutorial01/](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- 참고 블로그 : [https://lucky516.tistory.com/54](https://lucky516.tistory.com/54)