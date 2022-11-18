---
title: "Jupyter Notebook에서 SQL 실행하기"
categories:
  - sql
tag:
  - sql
  - oracle
author: "Jiwon Kang"
date: 2022-11-18 23:37:04
---


## 라이브러리 설치

- 공통적으로 다음 라이브러리를 설치한다
    
    ```bash
    pip install ipython-sql
    ```
    
    ![Untitled](/images/sql/sql_Jupiter/0.png)
    
  
- 접속하고자 하는 DB에 맞게 라이브러리를 설치한다
    
    ```bash
    # sql server
    pip install pyodbc
    
    # PostgreSQL 
    pip install pyscopg2
    
    # MySQL
    pip install PyMySQL
    
    # Oracle
    pip install cx_Oracle
    ```
    
    ![Untitled](/images/sql/sql_Jupiter/1.png)
    

## Jupyter Notebook에서 설정하기

- Jupyter Notebook에서 매직명령어로 익스텐션을 로드한다.
    
    ```jsx
    %load_ext sql
    ```
    
  
- 다음과 같은 창이 뜨면 Install을 누른다.
    
    ![Untitled](/images/sql/sql_Jupiter/2.png)
    
  
- 설치하면 정상적으로 실행이 된다
    
    ![Untitled](/images/sql/sql_Jupiter/3.png)
    
  
- 접속하려는 DB에 맞는 코드를 입력 후 실행
    
    ```jsx
    # SQL Server
    %sql mssql+pyodbc://user_name:password@host:port_number/db
    
    # PostgreSQL
    %sql postgresql://user_name:password@host:port_number/db
                
    # MySQL
    %sql mysql://user_name:password@host:port_number/db
    
    # Oracle
    %sql oracle://user_name:password@127.0.0.1:port_number/db
    ```
    
    ![Untitled](/images/sql/sql_Jupiter/4.png)
    
  
- 연결이 되었으면 코드 앞에 `%%sql`을 붙이고 쿼리를 실행한다 (세미콜론 제외)
    
    ![Untitled](/images/sql/sql_Jupiter/5.png)
    
  
- Jupyterlab에서 잘 실행되는 것을 확인할 수 있다.
    
    ![Untitled](/images/sql/sql_Jupiter/6.png)
    

## Reference

- 참고1 : [https://95pbj.tistory.com/47](https://95pbj.tistory.com/47)
- 참고2 : [https://towardsdatascience.com/heres-how-to-run-sql-in-jupyter-notebooks-f26eb90f3259](https://towardsdatascience.com/heres-how-to-run-sql-in-jupyter-notebooks-f26eb90f3259)