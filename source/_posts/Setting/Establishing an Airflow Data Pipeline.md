---
title: "Establishing an Airflow Data Pipeline"
categories:
  - setting
  - data engineering
tag:
  - setting
  - data engineering
  - wsl2
  - apache
  - airflow
author: "Jiwon Kang"
date: 2022-04-15 15:38:19
---

## ****Step 01. Create a Virtual Data****

- Create ***dags*** foler below ***(venv) airflow-test*** folder.

```
$ mkdir dags
$ ls

airflow-webserver.pid  airflow.cfg  airflow.db  dags  logs  venv  webserver_config.py
```

- Install the necessary libraries.

```
$ pip3 install faker pandas
```

- Create ***data*** folder and write python file in the folder to create a virtual data.
    - filename : ***step01_writecsv.py***

```
$ mkdir data
$ cd data
$ vi step01_writecsv.py
```

```python
***# step01_writecsv.py***

from faker import Faker
import csv
output = open('data.csv','w')
fake = Faker()

header = ['name','age','street','city','state','zip','lng','lat']
mywriter = csv.writer(output)
mywriter.writerow(header)

for r in range(1000):
	mywriter.writerow([[fake.name](http://fake.name/)(),
										 fake.random_int(min=18, max=80, step=1),
										 fake.street_address(),
										 fake.city(),
										 fake.state(),
										 fake.zipcode(),
										 fake.longitude(),
										 fake.latitude()])
output.close()
```

- Run the file above and make sure that the data is well generated.

```
$ python3 step01_writecsv.py
$ ls

data.csv  step01_writecsv.py
```

## Step 2. Establish csv2join file

- Write code to build CSV and JSON transform files in ***dags*** folder.
    - filename : ***csv2join.py***

```python
$ vi csv2json.py
```

```python
***# csv2join.py***

import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd

def csvToJson():
    df=pd.read_csv('data/data.csv')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.json',orient='records')

default_args = {
    'owner': 'evan',
    'start_date': dt.datetime(2020, 3, 18),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),      # '0 * * * *',
         ) as dag:

    print_starting = BashOperator(task_id='starting',
                               bash_command='echo "I am reading the CSV now....."')

    csvJson = PythonOperator(task_id='convertCSVtoJson',
                                 python_callable=csvToJson)

print_starting >> csvJson
```

- Run the csv2json.py above.

```python
$ python3 csv2json.py
```

## ****Step 04. Run Webserver and Scheduler Simultaneously****

- Open a separate terminal and run the webserver and scheduler.

```
$ airflow webserver -p 8080
$ airflow scheduler
```

- Check if it works normally in the Web UI.

## Reference

- [https://dschloe.github.io/python/data_engineering/ch03_reading_writing_file/airflow_csv2json_sample/](https://dschloe.github.io/python/data_engineering/ch03_reading_writing_file/airflow_csv2json_sample/)