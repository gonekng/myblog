---
title: "Apache-Airflow Setting in Windows11 (WSL 2)"
categories:
  - setting
tag:
  - setting
  - data engineering
  - wsl2
  - apache
  - airflow
author: "Jiwon Kang"
date: 2022-04-15 12:10:08
---


## Step 1. Create a virtual environment

- Install pip and virtualenv package

```
$ sudo apt install python3-pip
$ sudo pip3 install virtualenv
```

- Create a virtual environment in **c:\airflow-test** folder

```
$ virtualenv venv

created virtual environment CPython3.8.10.final.0-64 in 29086ms
creator CPython3Posix(dest=/mnt/c/airflow-test/venv, clear=False, no_vcs_ignore=False, global=False)
seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/donumm/.local/share/virtualenv)
added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```

- Open **.bashrc** file and add the following code.

```
$ vi ~/.bashrc

*export AIRFLOW_HOME=/mnt/c/airflow-test*
```

- Update the code and make sure it's actually reflected.

```
$ source ~/.bashrc
$ echo $AIRFLOW_HOME

/mnt/c/airflow-test
```

- Connect to virtual environment.

```
$ source venv/bin/activate
```

**※ Airflow must be installed in the virtual environment and executed in the virtual environment.**

## Step 4. Install Apache Airflow

- Install PostgreSQL, Slack, and Celery packages

```
pip3 install 'apache-airflow[postgres, slack, celery]'
```

- Initialize the DB to run the airflow.

```
$ airflow db init
```

- Register an username and password of the airflow

```
***# Create a new user***
$ airflow users create --username airflow --password airflow --firstname Jiwon --lastname Kang --role Admin --email donumm64@gmail.co
```

```
***# Check the user list***
$ airflow users list

id | username | email              | first_name | last_name | roles
===+==========+====================+============+===========+======
1  | donumm   | donumm64@gmail.com | Jiwon      | Kang      | Admin
```

- Open **airflow.cfg** file, and change the value of load_examples from True to False.
    
    ![](/images/Setting/apache_airflow/1.png)
 
- Reset the db in terminal.

```
$ airflow db reset
...
Proceed? (y/n) Y
```

- Run the airflow webserver and scheduler.

```
$ airflow webserver -p 8080
$ airflow scheduler
```

- Connect the airflow webserver.
    - URL : **[http://localhost:8080/login/](http://localhost:8080/login/)**
        
        ![](/images/Setting/apache_airflow/2.png)
        
    

## Reference

- [https://dschloe.github.io/settings/apache_airflow_using_wsl2/](https://dschloe.github.io/settings/apache_airflow_using_wsl2/)