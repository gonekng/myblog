---
title: "SQL Developer 깃허브 연동하기"
categories:
  - sql
tag:
  - sql
  - oracle
  - github
author: "Jiwon Kang"
date: 2022-04-26 16:02:41
---

## Step 1. Github 준비

- Github에서 SQL Developer와 연동할 새로운 Public Repository를 생성한다.
    
    ![](/images/sql/SQLdeveloper/1.jpg)

- `Settings` > `Developer settings` 에서 새로운 Personal access token을 발급받는다.
    - 새로 생성한 Repository의 이름을 입력하고 Select scopes에서 `repo`를 체크한 후 토큰을 생성한다.
    - 이때 생성된 토큰 번호는 다시 알 수 없기 때문에, 발급 즉시 복사하여 다른 곳에 저장해두어야 함
    
    ![](/images/sql/SQLdeveloper/16.jpg)
    

## Step 2. SQL Developer Git 복제

- SQL Developer에서 `팀` > `Git` > `복제` 를 클릭하여 복제 마법사를 실행한다.
    
    ![](/images/sql/SQLdeveloper/2.jpg)
    

- 다음 버튼을 클릭한다.
    
    ![](/images/sql/SQLdeveloper/3.jpg)
    

- 앞서 생성한 Repository의 URL을 입력하고 Github 사용자 이름 및 비밀번호를 입력한다.
    
    ![](/images/sql/SQLdeveloper/4.jpg)
    

- main 분기를 선택한 후 다음 버튼을 클릭한다.
    
    ![](/images/sql/SQLdeveloper/5.jpg)
    

- 로컬 Git 저장소 경로 및 이름을 지정한다.
    
    ![](/images/sql/SQLdeveloper/6.jpg)
    

- 입력한 정보를 확인한 후 완료 버튼을 클릭한다.
    
    ![](/images/sql/SQLdeveloper/7.jpg)
    

## Step 3. Git Push 테스트

- SQL Developer에서 `파일` > `새로 만들기` > `모든 항목` 을 클릭하여 SQL 파일을 생성한다.
    
    ![](/images/sql/SQLdeveloper/8.jpg)
    

- 새로운 파일의 이름을 입력한 후 디렉토리에는 Github와 연결한 로컬 폴더를 지정한다.
    
    ![](/images/sql/SQLdeveloper/9.jpg)
    

- 간단한 SQL 쿼리를 작성, 실행, 저장한 다음 팀 > Git > 모두 커밋 을 클릭한다.
    
    ![](/images/sql/SQLdeveloper/10.jpg)
    

- 작성자와 커밋한 사람에 이름을 입력한 다음 확인 버튼을 클릭한다.
    
    ![](/images/sql/SQLdeveloper/11.jpg)
    

- 팀 > Git > 푸시 를 클릭하여 푸시 마법사를 실행한다.
    
    ![](/images/sql/SQLdeveloper/12.jpg)
    

- 푸시 마법사의 안내에 따라 진행한다.
    
    ![](/images/sql/SQLdeveloper/13.jpg)
    
    ![](/images/sql/SQLdeveloper/14.jpg)
    
- 다음과 같은 에러가 발생할 경우 Step 2의 Git 복제 마법사를 다시 실행하고, Github 비밀번호에 앞서 발급받은 토큰 번호를 입력한다.
    
    ![](/images/sql/SQLdeveloper/15.jpg)

- Perform the push operation again and check that it is uploaded normally.
    
    ![](/images/sql/SQLdeveloper/17.jpg)

