---
title: "Spark Installation in WSL2"
categories:
  - setting
  - data engineering
tag:
  - setting
  - data engineering
  - spark
  - wsl2
author: "Jiwon Kang"
date: 2022-04-20 16:39:12
---

## Step 1. Install required files

- Install java and spark file. (Skip if already installed.)
    
    ```bash
    $ sudo apt-get install openjdk-8-jdk
    $ sudo wget https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz
    $ sudo tar -xvzf spark-3.2.0-bin-hadoop3.2.tgz
    ```
    

## Step 2. Set environment variables

- Open `.bashrc` file and add the code below.
    
    ```bash
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export SPARK_HOME=/mnt/c/hadoop/spark-3.2.0-bin-hadoop3.2
    export PATH=$JAVA_HOME/bin:$PATH
    export PATH=$SPARK_HOME/bin:$PATH
    export PYSPARK_PYTHON=/usr/bin/python3
    ```
    

- Update the code and make sure it's actually reflected.
    
    ```bash
    source ~/.bashrc
    echo SPARK_HOME
    
    /mnt/c/hadoop/spark-3.2.0-bin-hadoop3.2
    ```
    

## Step 3. Run Pyspark

- Run `pyspark` in the path.
    
    ![](/images/Setting/Spark_WSL2/0.png)
    

- Run the code below in the CMD and check the result printed.
    
    ```bash
    >>> rd = sc.textFile("README.md")
    >>> rd.count()
    
    109
    ```
    

## Step 4. Deploy in Web browser.

- Create a new directory `temp`, and virtual environment.

```bash
$ mkdir temp && cd temp
$ virtualenv venv
```

- Connect to virtual environment and install pyspark.

```bash
$ source venv/bin/activate
$ pip install pyspark
```

- Create a new directory and `README.md` file.
    
    ```bash
    $ mkdir data && cd data
    $ vi README.md
    ```
    
    > *This program just counts the number of lines containing ‘a’ and the number containing ‘b’ in a text file. Note that you’ll need to replace YOUR_SPARK_HOME with the location where Spark is installed. As with the Scala and Java examples, we use a SparkSession to create Datasets. For applications that use custom classes or third-party libraries, we can also add code dependencies to spark-submit through its --py-files argument by packaging them into a .zip file (see spark-submit --help for details). SimpleApp is simple enough that we do not need to specify any code dependencies.
    
    We can run this application using the bin/spark-submit script:*
    > 

- Back to `temp` and create `SampleApp.py`.
    
    ```bash
    $ cd ..
    $ vi SampleApp.py
    ```
    
    ```python
    ***# SampleApp.py***
    from pyspark.sql import SparkSession
    
    logFile = "data/README.md"  # Should be some file on your system
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    logData = spark.read.text(logFile).cache()
    
    numAs = logData.filter(logData.value.contains('a')).count()
    numBs = logData.filter(logData.value.contains('b')).count()
    
    print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
    
    input("Typing....")
    
    spark.stop()
    ```
    

- Run the `SimpleApp.py`
    
    ```bash
    $SPARK_HOME/bin/spark-submit --master local[4] SimpleApp.py
    ```
    

- Check the address below and copy it.
    
    ![](/images/Setting/Spark_WSL2/1.png)
    

- Enter the corresponding address in the web browser and check the web UI.
    
    ![](/images/Setting/Spark_WSL2/2.png)
