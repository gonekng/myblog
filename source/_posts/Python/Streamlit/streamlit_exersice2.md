---
title: "Streamlit & Sqlite3 연동 예제"
categories:
  - python
  - streamlit
tag:
  - python
  - streamlit
  - sqlite
  - pandas
author: "Jiwon Kang"
date: 2023-04-06 22:29:04
---

- Streamlit 기반 웹 대시보드를 Sqlite DB와 연동하는 작업
    - `Sqlite`  : 별도의 프로그램 설치 없이 Python 코드로 손쉽게 DB를 구성할 수 있음

## 0 :: 필요한 라이브러리 임포트

```python
import time, sys, os
import numpy as np
import pandas as pd

import sqlite3
import streamlit as st
```

## 1 :: 새로운 데이터베이스 생성 및 연동

```python
def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)

    return conn

def create_database():

    st.write("# PAGE1 : 데이터베이스 만들기")
    st.write("---")

    db_filename = st.text_input("데이터베이스 이름을 입력하세요.")
    create_db = st.button('데이터베이스 생성')

    if create_db:
        if db_filename.endswith('.db'):
            if db_filename not in [file for file in os.listdir(os.getcwd())]:
                conn = create_connection(db_filename)
                st.success('데이터베이스 생성 완료.')
            else:
                st.error('이미 존재하는 데이터베이스입니다. 다시 입력하세요.')
        else: 
            st.error('파일이름은 .db로 끝나야 합니다. 다시 입력하세요.')
```

- `sqlite3`  라이브러리의 `connect`  함수를 통해 db_file을 연동
- ‘데이터베이스 생성’ 버튼을 클릭하면 텍스트로 입력받은 이름의 .db 파일을 생성
    - 파일이름은 .db로 끝나야 하며, 이미 존재하는 이름인 경우 에러 발생

## 2 :: CSV 파일 업로드 및 DB 저장

```python
def upload_data():

    st.write("# PAGE2 : 파일 업로드하기")
    st.write("---")

    sqlite_dbs = [file for file in os.listdir('.') if file.endswith('.db')]
    db_filename = st.selectbox('데이터베이스를 선택하세요.', sqlite_dbs)
    if db_filename is not None:
        conn = create_connection(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        tables = [table[0] for table in tables]
        table_name = st.text_input('테이블 이름을 입력하세요.')
        if len(table_name) > 0:
            if table_name not in tables:
                uploaded_file = st.file_uploader('업로드할 파일을 첨부하세요.')
                if uploaded_file is not None:
                    try:
                        df = pd.read_csv(uploaded_file, encoding='cp949')
                        st.write('**Data loaded successfully. These are the first 3 rows.**')
                        st.dataframe(df.head(3), use_container_width=True)
                    
                        col1, col2 = st.columns([8,1])
                        is_apply = col2.button('Upload', use_container_width=True)
                        if is_apply:
                            pg_bar = col1.progress(0, text="⏩Progress")
                            for percent_complete in range(100):
                                time.sleep(0.01)
                                pg_bar.progress(percent_complete + 1, text="Progress")
                                df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)
                            time.sleep(0.1)
                            st.success("업로드가 완료되었습니다.")
                    except Exception as e:
                        st.write(e)
            else:
                st.error("이미 존재하는 테이블입니다. 다시 입력하세요.")
    else:
        st.error('DB 파일이 존재하지 않습니다. DB 파일을 먼저 생성하세요.')
```

- 현재 경로의 .db 파일 중 하나를 선택하고, CSV 파일을 불러온 후 테이블에 저장
    - 텍스트로 입력받은 테이블 이름이 이미 존재하는 경우 에러 발생
    - CSV 파일을 불러온 후 첫 3행 출력 내용을 확인한 후 업로드하도록 설정
    - 업로드 버튼 클릭 시 바로 테이블에 저장이 됨 → Progress Bar는 보여주기용

## 3 :: SQL 쿼리로 데이터 조작 및 CSV 파일로 저장

```python
def run_query():

    st.write("# PAGE3 : SQL 쿼리로 데이터 조작하기")
    st.write("---")

    sqlite_dbs = [file for file in os.listdir('.') if file.endswith('.db')]
    db_filename = st.selectbox('DB Filename', sqlite_dbs)
    query = st.text_area('SQL Query', height=150)
    if db_filename is not None:
        if len(query) == 0:
            is_disabled = True
        else:
            is_disabled = False
        submitted = st.button('Run Query', disabled=is_disabled)

        if submitted:
            conn = create_connection(db_filename)
            query = conn.execute(query)
            cols = [column[0] for column in query.description]
            results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )
            st.dataframe(results_df)
            if st.button('Download'):
                convert_df(results_df)

    else:
        st.error('DB 파일이 존재하지 않습니다. DB 파일을 먼저 생성하세요.')

def convert_df(df):
    return df.to_csv(index=False).encode('cp949')
```

- 현재 경로의 .db 파일 중 하나를 선택하고, SQL 쿼리를 입력하여 해당 DB의 데이터를 조작(CRUD)
    - SQL 쿼리를 입력해야 Run Query 버튼이 활성화되도록 설정
- `convert_df` : 쿼리 실행 후의 데이터 테이블을 CSV 파일로 저장하는 함수

## 4 :: 기본 화면 구성 및 사이드바 설정

```python
def main():

  # Page Configuration
    st.set_page_config(
        page_title="Sqlite3 DB Connect with Streamlit",
        page_icon="⚒️",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'Get Help': 'mailto:donumm64@gmail.com',
            'About': "*Made by gonekng*"
        }
    )

  # 사이드바 설정
    st.sidebar.subheader("🎈Streamlit으로 Sqlite3 DB 연동하기")
    st.sidebar.write("---")
    
    page_names_to_funcs = {
        "Create Database": create_database,
        "Upload Data": upload_data,
        "Run Query": run_query,
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys(), label_visibility='collapsed')
    page_names_to_funcs[selected_page]()

if __name__ == "__main__":

    main()
```

- `st.set_page_config` : 기본 페이지 설정
- `page_names_to_funcs` : 각 페이지를 구성하는 함수 매칭

# Reference

- Streamlit Documentation : [https://docs.streamlit.io/](https://docs.streamlit.io/)
- 참고블로그 : [https://blog.naver.com/v-world/222009887650](https://dschloe.github.io/python/2023/02/streamlite_with_sqlite/)

# 전체 코드

```python
import time, sys, os
import numpy as np
import pandas as pd

import sqlite3
import streamlit as st

# DB 연동
def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)

    return conn

# DB 생성
def create_database():

    st.write("# PAGE1 : 데이터베이스 만들기")
    st.write("---")

    db_filename = st.text_input("데이터베이스 이름을 입력하세요.")
    create_db = st.button('데이터베이스 생성')

    if create_db:
        if db_filename.endswith('.db'):
            if db_filename not in [file for file in os.listdir(os.getcwd())]:
                conn = create_connection(db_filename)
                st.success('데이터베이스 생성 완료.')
            else:
                st.error('이미 존재하는 데이터베이스입니다. 다시 입력하세요.')
        else: 
            st.error('파일이름은 .db로 끝나야 합니다. 다시 입력하세요.')

# 데이터 업로드
def upload_data():

    st.write("# PAGE2 : 파일 업로드하기")
    st.write("---")

    sqlite_dbs = [file for file in os.listdir('.') if file.endswith('.db')]
    db_filename = st.selectbox('데이터베이스를 선택하세요.', sqlite_dbs)
    if db_filename is not None:
        conn = create_connection(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        tables = [table[0] for table in tables]
        table_name = st.text_input('테이블 이름을 입력하세요.')
        if len(table_name) > 0:
            if table_name not in tables:
                uploaded_file = st.file_uploader('업로드할 파일을 첨부하세요.')
                if uploaded_file is not None:
                    try:
                        df = pd.read_csv(uploaded_file, encoding='cp949')
                        st.write('**Data loaded successfully. These are the first 3 rows.**')
                        st.dataframe(df.head(3), use_container_width=True)
                    
                        col1, col2 = st.columns([8,1])
                        is_apply = col2.button('Upload', use_container_width=True)
                        if is_apply:
                            pg_bar = col1.progress(0, text="⏩Progress")
                            for percent_complete in range(100):
                                time.sleep(0.01)
                                pg_bar.progress(percent_complete + 1, text="Progress")
                                df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)
                            time.sleep(0.1)
                            st.success("업로드가 완료되었습니다.")
                    except Exception as e:
                        st.write(e)
            else:
                st.error("이미 존재하는 테이블입니다. 다시 입력하세요.")
    else:
        st.error('DB 파일이 존재하지 않습니다. DB 파일을 먼저 생성하세요.')

# 쿼리 실행
def run_query():

    st.write("# PAGE3 : SQL 쿼리로 데이터 조작하기")
    st.write("---")

    sqlite_dbs = [file for file in os.listdir('.') if file.endswith('.db')]
    db_filename = st.selectbox('DB Filename', sqlite_dbs)
    query = st.text_area('SQL Query', height=150)
    if db_filename is not None:
        if len(query) == 0:
            is_disabled = True
        else:
            is_disabled = False
        submitted = st.button('Run Query', disabled=is_disabled)

        if submitted:
            conn = create_connection(db_filename)
            query = conn.execute(query)
            cols = [column[0] for column in query.description]
            results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )
            st.dataframe(results_df)
            if st.button('Download'):
                convert_df(results_df)

    else:
        st.error('DB 파일이 존재하지 않습니다. DB 파일을 먼저 생성하세요.')

def convert_df(df):
    return df.to_csv(index=False).encode('cp949')

# --------------------- 메인 함수 --------------------- #

def main():

  # Page Configuration
    st.set_page_config(
        page_title="Sqlite3 DB Connect with Streamlit",
        page_icon="⚒️",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'Get Help': 'mailto:donumm64@gmail.com',
            'About': "*Made by gonekng*"
        }
    )

  # 사이드바 설정
    st.sidebar.subheader("🎈Streamlit으로 Sqlite3 DB 연동하기")
    st.sidebar.write("---")
    
    page_names_to_funcs = {
        "Create Database": create_database,
        "Upload Data": upload_data,
        "Run Query": run_query,
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys(), label_visibility='collapsed')
    page_names_to_funcs[selected_page]()

if __name__ == "__main__":

    main()
```