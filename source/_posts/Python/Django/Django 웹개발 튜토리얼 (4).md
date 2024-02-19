---
title: "Django 웹개발 튜토리얼 (4)"
categories:
  - python
  - django
tag:
  - python
  - django
  - development
author: "Jiwon Kang"
date: 2024-02-19 22:45:02
---

## 새로운 View 추가하기

> django의 MTV에서 View는 웹페이지와 서버의 중간다리 (MVC 패턴의 컨트롤러 역할)
> 
- polls 어플리케이션의 구조
    - index 페이지 : Question에 대한 정보 출력
    - detail 페이지 : Question의 text를 상세히 출력 (투표형태)
    - result 페이지 : Question에 대한 결과 출력
        
        → Vote Action : 투표 기능 구현 필요
        
1. polls/views.py >> `detail`, `results`, `vote` 추가
    
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse
    
    def index(request):
        return HttpResponse("Hello, World. You're at the polls index.")
    
    def detail(request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)
    
    def results(request, question_id):
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)
    
    def vote(request, question_id):
        return HttpResponse("You're voting on question %s." % question_id)
    ```
    
2. polls/urls.py >> 새로 추가한 view를 url에 연결
    
    ```python
    from django.urls import path
    
    from . import views
    
    # root주소 http://127.0.0.1:8000//polls/
    urlpatterns = [
        # ex: /polls/
        path('', views.index, name='index'),
        # ex: /polls/5/
        path('<int:question_id>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:question_id>/results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
    ```
    

## 실제 View 기능 구현하기

1. polls/views.py >> 다음 코드 입력
    
    ```python
    from django.http import HttpResponse
    
    from .models import Question
    
    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        output = ', '.join([q.question_text for q in latest_question_list])
        return HttpResponse(output)
    
    # 나머지 view (detail, results, vote) 내용은 그대로
    ```
    
    - Question 모델에서 pub_date 기준 최신 데이터 5개를 불러와서 하나의 문자열로 출력하는 내용
2. admin 페이지에서 question 데이터 추가
    
    ![](/images/Python/Django/4/Untitled.png)
    
3. index 페이지 정상출력 여부 확인
    
    ![](/images/Python/Django/4/Untitled2.png)
    

## Template 이용하기

> Template : 사용자에게 보여지는 화면 → HTML 코드 일부를 파이썬으로 작성할 수 있음(`{% %}`)
> 
- 템플릿 파일 저장위치 : **어플리케이션폴더이름/templates/어플리케이션폴더이름/템플릿파일이름**
    - django에서는 templates 폴더 안에 있는 템플릿파일이름을 기준으로 불러오기 때문에, 다른 어플리케이션의 같은 이름을 가진 템플릿 파일과 충돌하는 경우를 방지하기 위해 templates 폴더 안에 어플리케이션폴더를 한번 더 만드는 것을 권장함 → `template namespacing`
- polls/templates/polls/index.html
    
    ```python
    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}
    ```
    
    - `{% %}` (tag) : html 내에서 파이썬 코드를 실행하는 문법
    - `{{ }}` (variable) : view에서 전달된 변수에 접근하는 문법
- polls/views.py >> index 템플릿을 view에 연동
    
    ```python
    from django.http import HttpResponse
    from django.template import loader
    
    from .models import Question
    
    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        template = loader.get_template('polls/index.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))
    
    # 나머지 view (detail, results, vote) 내용은 그대로
    ```
    
    - model의 Question 데이터를 추출하여 template에 전달
        
        ![](/images/Python/Django/4/Untitled3.png)
        
        ![](/images/Python/Django/4/Untitled4.png)
        

## wrapping 함수 사용하기

> 여러 개의 함수를 한번에 묶어서 호출하는 함수
> 
1. `render()`
    - polls/views.py 코드의 loader 및 httpreponse 작업은 `render()` 함수로 간략하게 표현 가능
    - 다음 코드는 기존의 코드와 같은 기능을 구현함
        
        ```python
        from django.shortcuts import render
        
        from .models import Question
        
        def index(request):
            latest_question_list = Question.objects.order_by('-pub_date')[:5]
            context = {'latest_question_list': latest_question_list}
            return render(request, 'polls/index.html', context)
        
        # 나머지 view (detail, results, vote) 내용은 그대로
        ```
        
2. `get_object_or_404()`
    - detail view의 템플릿 작성
        - polls/views.py
            
            ```python
            from django.http import Http404
            from .models import Question
            
            def detail(request, question_id):
                try:
                    question = Question.objects.get(pk=question_id)
                except Question.DoesNotExist:
                    raise Http404("Question does not exist")
                return render(request, 'polls/detail.html', {'question': question})
            ```
            
        - polls/templates/polls/detail.html
            
            ```python
            <h1>{{ question.question_text }}</h1>
            <ul>
            {% for choice in question.choice_set.all %}
                <li>{{ choice.choice_text }}</li>
            {% endfor %}
            </ul>
            ```
            
    - 해당 question이 있는 경우 (question 및 choice 출력)
        
        ![](/images/Python/Django/4/Untitled5.png)
        
    - 해당 question이 없는 경우 (404 에러 출력)
        
        ![](/images/Python/Django/4/Untitled6.png)
        
    - detail view의 404 에러를 일으키는 코드 → `get_object_or_404()` 함수로 간략하게 표현 가능
        - polls/view.py
            
            ```python
            from django.shortcuts import get_object_or_404
            from .models import Question
            
            def detail(request, question_id):
                question = get_object_or_404(Question, pk=question_id)
                return render(request, 'polls/detail.html', {'question': question})
            ```
            

## URL 하드코드 제거하기

- `{% url %}` 태그를 사용하면 하드코드가 아닌 유동적인 코드로 작성 가능
    
    → {% url (원하는 view의 url 이름) (url에 들어갈 입력변수) %}
    
- polls/templates/polls/index.html
    
    ```python
    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}
    ```
    
    - `"/polls/{{ question.id }}/"` : detail 뷰로 이동하는 링크 → `"{% url 'detail' question.id %}"`
    - polls/urls.py에서 detail 뷰의 name 확인
        
        ```python
        urlpatterns = [
            ...
            path('<int:question_id>/', views.detail, name='detail'),
            ...
        ]
        ```
        

## URL namespacing

> 여러 application에서 같은 url 이름을 가지고 있는 경우 충돌을 막기 위해 django에서 url namespacing 기능 제공
> 
- polls/urls.py 코드에서 app_name 지정
    
    ```python
    from django.urls import path
    from . import views
    
    app_name = 'polls'
    ...
    ```
    
- polls/templates/polls/detail.html 코드에서 url 정보 수정
    
    ```python
    ...
    <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
    ...
    ```
    

## Reference

- django Documentation : [https://docs.djangoproject.com/en/3.2/intro/tutorial01/](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- 참고 블로그 : [https://lucky516.tistory.com/58](https://lucky516.tistory.com/58)