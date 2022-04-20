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
date: 2022-04-20 14:41:33
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
    
    ![](/images/Setting/Spark_WSL2/Untitled.png)
    

- Run the code below in the CMD and check the result printed.

```bash
>>> rd = sc.textFile("README.md")
>>> rd.count()

109
```