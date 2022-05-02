---
title: "Conneting SQL Developer with Github"
categories:
  - sql
  - Oracle
tag:
  - sql
  - Oracle
author: "Jiwon Kang"
date: 2022-04-26 16:02:41
---

## Step 1. Preliminary work

- Register in github and install git.
- Create a new public repository. (my repository name : ***Sql_edu***)
    
    ![](/images/sql/SQLdeveloper/1.jpg)
    

## Step 2. SQL Developer Setting

- SQL Developer > 팀 > Git > 복제
    
    ![](/images/sql/SQLdeveloper/2.jpg)
    

- Click the ***Next*** button.
    
    ![](/images/sql/SQLdeveloper/3.jpg)
    

- Enter the URL of the repository and Username, Password.
    - Repository must be ***Public*** so that there is no authentication error.
    
    ![](/images/sql/SQLdeveloper/4.jpg)
    

- Select ***main*** and move on.
    
    ![](/images/sql/SQLdeveloper/5.jpg)
    

- Check the information for the git and move on.
    
    ![](/images/sql/SQLdeveloper/6.jpg)
    

- The process of replication is done.
    
    ![](/images/sql/SQLdeveloper/7.jpg)
    

## Step 3. Git Push Test

- SQL Developer > 파일 > 새로 만들기 > 모든 항목
    
    ![](/images/sql/SQLdeveloper/8.jpg)
    

- Create a new SQL file(`temp.sql`) and set a directory linked to github.
    
    ![](/images/sql/SQLdeveloper/9.jpg)
    

- Create and run a simple query, save it, and click ***'commit all'*** in Git.
    
    ![](/images/sql/SQLdeveloper/10.jpg)
    

- Enter your name in 'Author' and 'Commiters' and click ***OK***.
    
    ![](/images/sql/SQLdeveloper/11.jpg)
    

- Click ***‘push’*** in Git.
    
    ![](/images/sql/SQLdeveloper/12.jpg)
    

- Proceed with the push operation in order.
    
    ![](/images/sql/SQLdeveloper/13.jpg)
    
    ![](/images/sql/SQLdeveloper/14.jpg)
    
- If the error below occurs, an authentication token must be issued from Github.
    
    ![](/images/sql/SQLdeveloper/15.jpg)
    

- Github > Profile > Settings > Developer Settings > Personal Access Tokens > Generate new token
    - Enter the repository name and select the repo in Select scopes.
    - The generated token number will not be shown again, so you must copy it immediately and remember it separately.
    
    ![](/images/sql/SQLdeveloper/16.jpg)
    

- Perform the push operation again and check that it is uploaded normally.
    
    ![](/images/sql/SQLdeveloper/17.jpg)
- 