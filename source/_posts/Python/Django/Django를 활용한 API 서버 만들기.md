---
title: "Django를 활용한 API 서버 만들기"
categories:
  - python
  - django
tag:
  - python
  - django
  - development
  - api
author: "Jiwon Kang"
date: 2024-09-03 19:06:20
---

### 0. Django란?

Django는 파이썬으로 작성된 웹 프레임워크로, 신속한 웹 애플리케이션 개발을 가능하게 하며, 다음과 같은 특징이 있음

- MTV 아키텍처
    - 모델(Model), 템플릿(Template), 뷰(View) 구조로, 코드의 재사용성과 유지보수성이 향상됨
- ORM(Object-Relational Mapping)
    - 데이터베이스와의 상호작용을 객체 지향적으로 처리하기 때문에 SQL 쿼리 없이도 데이터베이스 작업 가능
- 관리자 인터페이스
    - 기본적으로 제공하는 관리 패널을 통해 데이터베이스 관리 및 CRUD(Create, Read, Update, Delete) 작업을 보다 쉽게 수행 가능

---

### 1. Django 설치

- 파이썬 가상 환경 설정
    
    ```bash
    python -m venv venv
    source venv\Scripts\activate
    ```
    
    - 가상 환경을 사용하면 프로젝트마다 독립된 패키지 설치 가능
- Django 설치
    
    ```bash
    pip install django
    pip install djangorestframework
    ```
    

---

### 2. Django 프로젝트 생성

Django 프로젝트를 생성하여 웹 애플리케이션의 최상위 구조 정의

- Django 프로젝트 생성:
    
    ```bash
    django-admin startproject myproject
    cd myproject
    ```
    
    - `myproject`라는 새 Django 프로젝트 생성 → 기본적인 설정 파일 및 디렉토리 구조 포함

---

### 3. 앱 생성 및 등록

앱(App) : Django 프로젝트 내에서 기능별로 구분된 모듈

- Django 앱 생성
    
    ```bash
    python manage.py startapp myapp
    ```
    
    - `myapp`이라는 새 앱 생성 → 각 앱은 독립적인 기능을 가지며, 모델, 뷰, 템플릿 등 포함

- [`settings.py`](http://settings.py)
    
    ```python
    INSTALLED_APPS = [
        ...
        'myapp',
    ]
    ```
    
    - 앱을 Django 프로젝트에 등록하여 Django가 myapp에 있는 모델 및 뷰를 인식하도록 함

---

### 4. 모델 정의 및 적용

Django의 모델을 정의하여 데이터베이스 테이블을 앱 내에서 구현

- `myapp/models.py`
    
    ```python
    from django.db import models
    
    class YourModel(models.Model):
        category = models.CharField(max_length=100)
        value1 = models.IntegerField()
        value2 = models.FloatField()
    ```
    
    - `YourModel` 클래스는 데이터베이스 테이블을, 각 필드는 데이터베이스의 컬럼을 정의
    - `CharField`, `IntegerField`, `FloatField`는 각각 문자열, 정수형, 실수형 데이터 필드
- 마이그레이션 생성 및 적용
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
    - 모델 변경 사항을 감지하는 마이그레이션 파일 생성 후 데이터베이스에 변경 사항 적용
    - `YourModel`에 대한 테이블이 데이터베이스에 생성됨

<aside>
※ 마이그레이션(Migration)

- Django에서 데이터베이스의 스키마를 관리하는 방법
    1. 모델 변경 관리
        
        : Django 모델을 수정하면 변경 사항을 데이터베이스에 반영
        
    2. 버전 관리
        
        : 각 마이그레이션은 고유한 번호를 가지며, 데이터베이스를 이전 버전으로 되돌리거나 특정 버전으로 이동 가능
        
    3. 파일 자동 생성
        
        : Django는 모델의 변경 사항을 감지하여 마이그레이션 파일을 자동 생성하므로, 수동으로 SQL 쿼리를 작성할 필요 없음
        
</aside>

---

### 5. CSV 데이터 로드

CSV 파일에서 데이터를 읽어 데이터베이스에 저장

- `myapp/load_data.py`
    
    ```python
    import pandas as pd
    from myapp.models import YourModel
    
    def load_data_from_csv(file_path):
        data = pd.read_csv(file_path)
        for index, row in data.iterrows():
            YourModel.objects.create(
                category = row['COLUMN1'],
                value1 = row['COLUMN2'],
                value2 = row['COLUMN3'],
            )
    ```
    
- Django Shell 스크립트 실행
    
    ```bash
    python manage.py shell
    ```
    
    ```python
    from myapp.load_data import load_data_from_csv
    load_data_from_csv('path/to/your/data.csv')
    ```
    

---

### 6. API 시리얼라이저 및 뷰 정의

API 개발을 위하여 시리얼라이저(Serializer) 및 뷰(View) 생성

- `myapp/serializers.py`
    
    ```python
    from rest_framework import serializers
    from .models import YourModel
    
    class YourModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = YourModel
            fields = '__all__'
    ```
    
- `myapp/views.py`
    
    ```python
    from rest_framework import viewsets
    from .models import YourModel
    from .serializers import YourModelSerializer
    
    class YourModelViewSet(viewsets.ModelViewSet):
        queryset = YourModel.objects.all()
        serializer_class = YourModelSerializer
    
        def get_queryset(self):
            queryset = super().get_queryset()
            field1 = self.request.query
    ```
    
    - `get_queryset(self)` : field1 컬럼을 키값으로 하여 데이터를 조회하는 쿼리 함수

<aside>
※ 시리얼라이저(Serializer)

- Django REST Framework(DRF)에서 데이터 변환을 담당하는 구성요소
    1. 데이터 직렬화(Serialization)
        
        : Python 객체(Django 모델 인스턴스 등)을 JSON, XML 등의 직렬화된 형태로 변환하여 웹 API를 통하여 데이터를 전송 및 수신할 수 있게 함
        
    2. 유효성 검사
        
        : 사용자가 API를 통해 보낸 데이터가 올바른 형식인지, 필요한 필드가 포함되었는지 확인
        
    3. 데이터 구조화
        
        : 포함할 필드, 제외할 필드 등 데이터 구조 정의
        
    4. CRUD 작업 지원
        
        : 데이터베이스와의 CRUD(Create, Read, Update, Delete) 작업을 지원
        
</aside>

---

### 7. CSV 파일 다운로드

URL 파라미터를 사용하여 데이터를 CSV 파일로 다운로드하는 기능 구현

- `myapp/view.py`
    
    ```python
    def export_to_csv(request):
        category= request.GET.get('category', None)
        
        if category:
            data = YourModel.objects.filter(category = category)
        else:
            data = YourModel.objects.all()
        
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        response.write(u'\ufeff'.encode('utf-8'))
        
        writer = csv.writer(response)
        writer.writerow(['category', 'value1', 'value2'])
        
        for item in data:
            writer.writerow([item.category, item.value1, item.value2])
        
        return response
    ```
    
    - `category` 컬럼을 키값으로 하는 필터링 기능 구현
    - 받아온 데이터를 `data.csv` 파일에 저장하며, BOM을 추가하여 UTF-8 인코딩 설정

---

### 8. URL 설정

API를 호출할 수 있도록 앱의 URLconf 설정

- `myapp/urls.py`
    
    ```python
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import YourModelViewSet
    
    router = DefaultRouter()
    router.register(r'your-model', YourModelViewSet)
    
    urlpatterns = [
        path('', include(router.urls)),
        path('export/csv/', export_to_csv, name='export_to_csv'),
    ]
    ```
    
- `myproject/urls.py`
    
    ```python
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('myapp.urls')),
    ]
    ```
    
    - `include()` 함수를 사용하여 myapp의 URL 패턴을 프로젝트의 URL 패턴에 추가
    - `api/your-model`, `api/export/csv` 등으로 접근 가능

---

### 9. Host 설정

Django의 `ALLOWED_HOSTS` 설정을 통해 웹 서버가 받아들일 수 있는 호스트 지정

- `settings.py`
    
    ```python
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost',
        '192.168.0.39',
    ]
    ```
    

---

### 10. 최종 서버 실행

- Django 서버 실행
    
    ```bash
    python manage.py runserver 192.168.0.39:8000
    ```
    
- 실행화면(예시)
    
    ![](/images/Python/Django/image.png)