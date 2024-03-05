---
title: "Django 웹개발 튜토리얼 (5)"
categories:
  - python
  - django
tag:
  - python
  - django
  - development
author: "Jiwon Kang"
date: 2024-03-05 22:18:50
---

## Polls 어플리케이션 완성하기

1. 데이터베이스에 Question과 Choice 만들기 (admin 페이지)
    - 이전 데이터는 모두 삭제한 후 Question 하나 추가
        
        ![](/images/Python/Django/5/Untitled.png)
        
        ![](/images/Python/Django/5/Untitled1.png)
        
2. detail 템플릿 완성하기
    - polls/templates/polls/detail.html
        
        ```html
        <h1>{{ question.question_text }}</h1>
        
        {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
        
        <form action="{% url 'polls:vote' question.id %}" method="post">
        {% csrf_token %}
        {% for choice in question.choice_set.all %}
            <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
            <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        {% endfor %}
        <input type="submit" value="Vote">
        </form>
        ```
        
        - `form` 태그를 이용하여 투표 기능 삽입
        - `<form action="{% url 'polls:vote' question.id %}" method="post">` : form 데이터를 POST request 방식으로 vote 뷰에 전송함
        - `<input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">`
            
            → 데이터는 key, value 형태로 전달되며 이때 key는 `name="choice"`, value는 `value="{{choice.id}}"` 를 의미한다. 
            
        - `forloop.counter` : for문 반복횟수 출력
        - `csrf_token` : django에서 제공하는 보안기능
    - 서버 출력화면
        
        ![](/images/Python/Django/5/Untitled2.png)
        
3. vote 뷰 구현하기
    - polls/views.py
        
        ```python
        from .models import Question, Choice
        ...
        def vote(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice']) # key, value 값으로 데이터 받아옴
            except (KeyError, Choice.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
            else:
                selected_choice.votes += 1
                selected_choice.save()
                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        ```
        
        - `question.choice_set.get(pk=request.POST['choice'])` : key, value 형태로 전달되므로 request.POST[”key”]의 형태로 불러옴
        - `except` : 데이터 전송에 실패하면 detail 뷰로 넘어가서 에러메시지 출력
        - `else` : 데이터 전송에 성공하면 votes 변수에 1을 더한 후 저장
        - `reverse` 함수 : url의 name을 url로 거꾸로 바꿔주는 함수
            
            → `reverse('polls:results', args=(question.id,))` : polls:results를 url로 바꾼 후 url에 필요한 변수를 args에 추가함
            
4. result 뷰 구현하기
    - polls/views.py
        
        ```python
        def results(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            return render(request, 'polls/results.html', {'question': question})
        ```
        
    - polls/templates/polls/results.html
        
        ```html
        <h1>{{ question.question_text }}</h1>
        
        <ul>
        {% for choice in question.choice_set.all %}
            <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
        {% endfor %}
        </ul>
        
        <a href="{% url 'polls:detail' question.id %}">Vote again?</a>
        ```
        
        - 해당 question에서 각 choice가 몇개씩 투표되었는지 출력
        - `{{ | }}` : filter 기능 → python의 변수를 특정 형태로 바꿔주는 역할
            
            → `{{ choice.votes|pluralize }}` : choice.votes 값이 2 이상일 경우 뒤에 s를 추가
            
    - 서버 출력화면
        
        ![](/images/Python/Django/5/Untitled3.png)
        

## Reference

- django Documentation : [https://docs.djangoproject.com/en/3.2/intro/tutorial01/](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- 참고 블로그 : [https://lucky516.tistory.com/59](https://lucky516.tistory.com/59)