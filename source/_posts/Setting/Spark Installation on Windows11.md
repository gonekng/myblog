---
title: "Spark Installation on Windows11"
categories:
  - setting
tag:
  - setting
  - data engineering
  - spark
author: "Jiwon Kang"
date: 2022-04-19 11:50:39
---

## Step 1. Install Java DK

- Download **Windows Installer.**
    - URL : [https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html](https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html)
    
    ![](/images/Setting/Spark/0.png)
    

- Run the download file as an administrator. Modify the path as shown in the picture below. (Be careful not to include spaces in the path name.)
    
    ![](/images/Setting/Spark/1.png)
    
    ![](/images/Setting/Spark/2.png)
    

## Step 2. Install Spark

- Download **Spark `.tgz` file**. (Click the link in the images below.)
    - URL : [https://www.apache.org/dyn/closer.lua/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz](https://www.apache.org/dyn/closer.lua/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz)
    
    ![](/images/Setting/Spark/3.png)
    

- Download **WinRAR** to unzip the `.tgz` compressed file, and run as an administrator.
    - URL : [https://www.rarlab.com/download.htm](https://www.rarlab.com/download.htm)
    
    ![](/images/Setting/Spark/4.png)
    

- Open the Spark file with WinRAR and extract to the folder.
    
    ![](/images/Setting/Spark/5.png)
    

- Rename the folder to ***spark***, and copy and paste under the C drive.
    
    ![](/images/Setting/Spark/6.png)
    

- Open `spark\conf\log4j.properties` file with memo pad, and change the ***log4j.rootCategory*** value from `INFO` to `ERROR`.
    
    ![](/images/Setting/Spark/7.png)
    
    ![](/images/Setting/Spark/8.png)
    

## Step 3. Install Winutils

- Download **winutils.exe**. (Check the version of Spark.)
    - URL : ‣
    
    ![](/images/Setting/Spark/9.png)
    

- Create a foler **winutils\bin**, and copy and paste **winutils.exe**.
    
    ![](/images/Setting/Spark/10.png)
    

- Run a CMD as an administrator, and write the code below.
    
    ```
    > cd c:\winutils\bin
    > winutils.exe chmod 777 \tmp\hive
    
    ****ChangeFileModeByMask error (2): ??? ??? ?? ? ????.
    ```
    
    - If the above error occurs, create the ***tmp\hive*** folder under the C drive and run it again.
        
        ![](/images/Setting/Spark/11.png)
        

## Step 4. Setting environment variables

- Create a new user variable ***SPARK_HOME***, and set the value as the path of ***spark*** folder.
    
    ![](/images/Setting/Spark/12.png)
    

- Create a new user variable ***JAVA_HOME***, and set the value as the path of ***jdk*** folder.
    
    ![](/images/Setting/Spark/13.png)
    

- Create a new user variable ***HADOOP_HOME***, and set the value as the path of ***winutils*** folder.
    
    ![](/images/Setting/Spark/14.png)
    

- Edit the Path variable
    - Insert `%SPARK_HOME%\bin` and `%JAVA_HOME%\bin`.
    
    ![](/images/Setting/Spark/15.png)
    

- Create a new user variable ***PYSPARK_PYTHON***, and set the value as ***PYTHON***.
    
    ![](/images/Setting/Spark/16.png)
    

- Run a CMD as an administrator, and run `pyspark` in the ***c:\spark*** path.
    
    ![](/images/Setting/Spark/17.png)
    

- Run the code below in the CMD and check the result printed.
    
    ```
    > rd = sc.textFile("README.md")
    > rd.count()
    
    109
    ```
    

- Create new user variables and set the value.
    - ***PYSPARK_DRIVER_PYTHON*** ; ***jupyter***
    - ***PYSPARK_DRIVER_PYTHON_OPTS*** ; ***notebook***
    
    ![](/images/Setting/Spark/18.png)
    
    ![](/images/Setting/Spark/19.png)
    

## Reference

- [https://dschloe.github.io/python/python_edu/00_settings/spark_installation_windows_10/](https://dschloe.github.io/python/python_edu/00_settings/spark_installation_windows_10/)