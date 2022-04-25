---
title: "Oracle 19c Installation in Windows11"
categories:
  - sql
  - Oracle
tag:
  - sql
  - Oracle
author: "Jiwon Kang"
date: 2022-04-25 17:27:10
---

## Step 1. Install Oracle Database

- Run the setup file as administrator and follow the procedure below.
    
    ![](/images/sql/Oracle1.png)
    
    ![](/images/sql/Oracle2.png)
    
    ![](/images/sql/Oracle3.png)
    
    ![](/images/sql/Oracle4.png)
    

- If the following error occurs, go back to the beginning and change to 'Software Only Settings'.
    - ***Creating and configuring a single instance database*** : Installing myoracle and database
    - ***Software Only Settings*** : Installing myoracle only
    
    ![](/images/sql/Oracle5.png)
    
    ![](/images/sql/Oracle6.png)
    
    ![](/images/sql/Oracle7.png)
    
    ![](/images/sql/Oracle8.png)
    
- Run a cmd as administrator and enter the code below. *(if you changed to ‘Software Only Settings’.)*
    - C:\sql_lecture\WINDOWS.X64_193000_db_home>`**dbca**`
    
    ![](/images/sql/Oracle9.png)
    
    ![](/images/sql/Oracle10.png)
    
    ![](/images/sql/Oracle11.png)
    

- If the error above occurs again, proceed as follows.
    
    ![](/images/sql/Oracle12.png)
    
    ![](/images/sql/Oracle13.png)
    
    ![](/images/sql/Oracle14.png)
    
    ![](/images/sql/Oracle15.png)
    

## Step 2. Create Tablespace by SQL Plus

- Run SQL Plus as administrator and enter the username and password.
    
    ![](/images/sql/Oracle16.png)
    
- Enter the SQL code below.
    
    ```sql
    # Create a new tablespace
    CREATE TABLESPACE myts DATAFILE 'C:\sql_lecture\oradata\MYORACLE\myts.dbf' SIZE 100M AUTOEXTEND ON NEXT 5M;
    ```
    
    ```sql
    # Create a new user
    CREATE USER ora_user IDENTIFIED BY jiwon DEFAULT TABLESPACE MYTS TEMPORARY TABLESPACE TEMP;
    ```
    
    ```sql
    # Grant a DBA role to the user
    GRANT DBA TO ora_user;
    
    권한이 부여되었습니다.
    ```
    
    ```sql
    # Connect to the database as the user
    connect ora_user/jiwon;
    
    연결되었습니다.
    ```
    
    ```sql
    # Print out the currently logged-in username
    select user from dual;
    
    USER
    --------------------------------------------------------------------------------
    ORA_USER
    ```
    

## Step 3. Install SQL Developer

- Run the setup file.
    
    ![](/images/sql/Oracle17.png)
    
    - Click ***No*** if the warning below occurs.
    
    ![](/images/sql/Oracle18.png)
    
    ![](/images/sql/Oracle19.png)
    

- Run a CMD as administrator and enter the code below.
    - C:\WINDOWS\system32>`lsnrctl status`
    
    ![](/images/sql/Oracle20.png)
    

- If an ***Unknown error*** occurs as described above, run the ***Net Configuration Assistant***.
    
    ![](/images/sql/Oracle21.png)
    
    ![](/images/sql/Oracle22.png)
    
    ![](/images/sql/Oracle23.png)
    

- If you input the code at the CMD again, the listener information is printed normally.
    
    ![](/images/sql/Oracle24.png)
    
- Create a new Database Access.
    
    ![](/images/sql/Oracle25.png)
    
    ![](/images/sql/Oracle26.png)
    
- Tool > Setting > Database > NLS
    
    ![](/images/sql/Oracle27.png)
    
- Enter `YYYY/MM/DD HH24:MI:SS` in ***'Time Record Format'***.
    
    ![](/images/sql/Oracle28.png)
    

- Write the query below and check the result.
    
    ```sql
    SELECT user from DUAL;
    ```
    
    ![](/images/sql/Oracle29.png)
    
- Create a ***backup*** folder under the C drive and download `expall.dmp` and `expcust.dmp`
    - URL : [https://github.com/gilbutITbook/006696/tree/master/01장 환경설정](https://github.com/gilbutITbook/006696/tree/master/01%EC%9E%A5%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95)

- Run a CMD as administrator and enter the code below at the ***backup*** folder.
    
    ```sql
    imp ora_user/evan file=expall.dmp log=empall.log ignore=y grants=y rows=y indexes=y full=y
    ```
    
    ![](/images/sql/Oracle30.png)
    
    ```sql
    imp ora_user/evan file=expcust.dmp log=expcust.log ignore=y grants=y rows=y indexes=y full=y
    ```
    
    ![](/images/sql/Oracle31.png)
    

- Write the query below and check the result.
    
    ```sql
    SELECT table_name FROM user_tables;
    ```
    
    ![](/images/sql/Oracle32.png)
    

- In SQL Plus, make sure that the user is created correctly.
    
    ![](/images/sql/Oracle33.png)
