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
    
    ![](/images/sql/Oracle/1.png)
    
    ![](/images/sql/Oracle/2.png)
    
    ![](/images/sql/Oracle/3.png)
    
    ![](/images/sql/Oracle/4.png)
    

- If the following error occurs, go back to the beginning and change to 'Software Only Settings'.
    - ***Creating and configuring a single instance database*** : Installing myoracle and database
    - ***Software Only Settings*** : Installing myoracle only
    
    ![](/images/sql/Oracle/5.png)
    
    ![](/images/sql/Oracle/6.png)
    
    ![](/images/sql/Oracle/7.png)
    
    ![](/images/sql/Oracle/8.png)
    
- Run a cmd as administrator and enter the code below. *(if you changed to ‘Software Only Settings’.)*
    - C:\sql_lecture\WINDOWS.X64_193000_db_home>`**dbca**`
    
    ![](/images/sql/Oracle/9.png)
    
    ![](/images/sql/Oracle/10.png)
    
    ![](/images/sql/Oracle/11.png)
    

- If the error above occurs again, proceed as follows.
    
    ![](/images/sql/Oracle/12.png)
    
    ![](/images/sql/Oracle/13.png)
    
    ![](/images/sql/Oracle/14.png)
    
    ![](/images/sql/Oracle/15.png)
    

## Step 2. Create Tablespace by SQL Plus

- Run SQL Plus as administrator and enter the username and password.
    
    ![](/images/sql/Oracle/16.png)
    
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
    
    ![](/images/sql/Oracle/17.png)
    
    - Click ***No*** if the warning below occurs.
    
    ![](/images/sql/Oracle/18.png)
    
    ![](/images/sql/Oracle/19.png)
    

- Run a CMD as administrator and enter the code below.
    - C:\WINDOWS\system32>`lsnrctl status`
    
    ![](/images/sql/Oracle/20.png)
    

- If an ***Unknown error*** occurs as described above, run the ***Net Configuration Assistant***.
    
    ![](/images/sql/Oracle/21.png)
    
    ![](/images/sql/Oracle/22.png)
    
    ![](/images/sql/Oracle/23.png)
    

- If you input the code at the CMD again, the listener information is printed normally.
    
    ![](/images/sql/Oracle/24.png)
    
- Create a new Database Access.
    
    ![](/images/sql/Oracle/25.png)
    
    ![](/images/sql/Oracle/26.png)
    
- Tool > Setting > Database > NLS
    
    ![](/images/sql/Oracle/27.png)
    
- Enter `YYYY/MM/DD HH24:MI:SS` in ***'Time Record Format'***.
    
    ![](/images/sql/Oracle/28.png)
    

- Write the query below and check the result.
    
    ```sql
    SELECT user from DUAL;
    ```
    
    ![](/images/sql/Oracle/29.png)
    
- Create a ***backup*** folder under the C drive and download `expall.dmp` and `expcust.dmp`
    - URL : [https://github.com/gilbutITbook/006696/tree/master/01장 환경설정](https://github.com/gilbutITbook/006696/tree/master/01%EC%9E%A5%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95)

- Run a CMD as administrator and enter the code below at the ***backup*** folder.
    
    ```sql
    imp ora_user/evan file=expall.dmp log=empall.log ignore=y grants=y rows=y indexes=y full=y
    ```
    
    ![](/images/sql/Oracle/30.png)
    
    ```sql
    imp ora_user/evan file=expcust.dmp log=expcust.log ignore=y grants=y rows=y indexes=y full=y
    ```
    
    ![](/images/sql/Oracle/31.png)
    

- Write the query below and check the result.
    
    ```sql
    SELECT table_name FROM user_tables;
    ```
    
    ![](/images/sql/Oracle/32.png)
    

- In SQL Plus, make sure that the user is created correctly.
    
    ![](/images/sql/Oracle/33.png)
