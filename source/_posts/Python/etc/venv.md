---
title: "파이썬 가상환경 설정하기 (Git Bash)"
categories:
  - python
  - etc
tag:
  - python
  - git
author: "Jiwon Kang"
date: 2023-02-06 23:47:10
---

## 가상환경(virtual environment)이란?

- 현재 설치된 파이썬 환경과 별개로 존재하는 독립적인 환경을 의미
- 다수의 프로그램을 개발할때 패키지 간의 버전이 달라서 발생하는 문제를 해결
- 표준 라이브러리 : `venv`
- 비표준 라이브러리 : `virtualvenv`, `pyenv`, `pipenv` 등등

<br>

## 가상환경 설정

1. Git Bash에서 프로젝트 폴더로 이동한 후 가상환경 디렉토리를 생성한다.
    
    ```bash
    python -m venv 가상환경이름
    ```
    
2. 생성한 가성환경을 활성화한다.
    
    ```bash
    # 활성화(Windows)
    source 가상환경이름/Scripts/activate
    
    # 활성화(Mac)
    source 가상환경이름/bin/activate
    ```
    
    - 비활성화 : `deactivate`

<br>

## 패키지 관리

1. 패키지 추가
    - 패키지의 특정 버전을 지정하여 설치할 수 있음
    
    ```bash
    python -m pip install 패키지이름
    ```
    
2. 패키지 업데이트
    
    ```bash
    python -m pip install --upgrade 패키지이름
    ```
    
3. 패키지 조회
    
    ```bash
    # 가상환경에 설치된 패키지명 및 버전 조회
    pip list
    
    # 가상환경에 설치된 패키지명 및 버전을 txt 파일로 저장
    pip freeze > requirements.txt
    ```
    

## Reference

- [https://potato-potahto.tistory.com/entry/GIT파이썬-가상환경가상환경-설정](https://potato-potahto.tistory.com/entry/GIT%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95)