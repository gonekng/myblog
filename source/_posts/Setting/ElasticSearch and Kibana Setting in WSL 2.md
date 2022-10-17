---
title: "ElasticSearch and Kibana Setting in WSL 2"
categories:
  - setting
tag:
  - setting
  - data engineering
  - wsl2
  - elasticsearch
  - kibana
author: "Jiwon Kang"
date: 2022-04-15 17:43:10
---

## Step 1. Install Package

- Update the system package and install a package related to HTTPS.

```
$ sudo apt update
$ sudo apt install apt-transport-https
```

- Install Java and check the version of Java.

```
$ sudo apt install openjdk-11-jdk
$ java -version
openjdk 11.0.14.1 2022-02-08
OpenJDK Runtime Environment (build 11.0.14.1+1-Ubuntu-0ubuntu1.20.04)
OpenJDK 64-Bit Server VM (build 11.0.14.1+1-Ubuntu-0ubuntu1.20.04, mixed mode, sharing)
```

- Open the vi editor to set the java environment variable.

```
$ sudo vi /etc/environment
```

- Insert the following sentence in vi editor.
    
    `JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"`
    

- Update the environment variables and check the contents.

```
$ source /etc/environment
$ echo $JAVA_HOME

/usr/lib/jvm/java-11-openjdk-amd64
```

---

## Step 2. Install ElasticSearch

- Check the GPG keys.

```
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add

OK
```

- Add a library and install ElasticSearch.

```
$ sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
$ sudo apt-get update

$ sudo apt-get install elasticsearch
```

---

## Step 3. Start ElasticSearch

- Start EleasticSearch

```
$ sudo systemctl start elasticsearch

System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

- If the above error is printed, add the following command.

```
$ sudo -b unshare --pid --fork --mount-proc /lib/systemd/systemd --system-unit=basic.target
$ sudo -E nsenter --all -t $(pgrep -xo systemd) runuser -P -l $USER -c "exec $SHELL"
```

- Enable the ElasticSearch and start the service.

```
$ sudo systemctl enable elasticsearch

Synchronizing state of elasticsearch.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable elasticsearch

$ sudo systemctl start elasticsearch
```

- Ensure that the service is actually operational.

```
$ curl -X GET "localhost:9200/"

{
  "name" : "DESKTOP-JM1I3QF",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "ma7ulQQ_RL-Y3ZNsjz0ZVw",
  "version" : {
    "number" : "7.17.2",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "de7261de50d90919ae53b0eff9413fd7e5307301",
    "build_date" : "2022-03-28T15:12:21.446567561Z",
    "build_snapshot" : false,
    "lucene_version" : "8.11.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

- Check whether it is printed well on the window screen.
    
    ![](/images/Setting/elasticsearch_kibana/1.png)
    

---

## Step 4. Install and Start Kibana

- Install and enable Kibana service

```
$ sudo apt-get install kibana
$ sudo systemctl enable kibana

Synchronizing state of kibana.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable kibana
```

- Start Kibana service and check the status

```
$ sudo systemctl start kibana
$ sudo systemctl status kibana

● kibana.service - Kibana
     Loaded: loaded (/etc/systemd/system/kibana.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2022-04-14 11:53:07 KST; 21min ago
       Docs: https://www.elastic.co
   Main PID: 303 (node)
      Tasks: 11 (limit: 4646)
     Memory: 599.0M
     CGroup: /system.slice/kibana.service
             └─303 /usr/share/kibana/bin/../node/bin/node /usr/share/kibana/bin/../src/cli/dis>

Apr 14 11:53:07 DESKTOP-JM1I3QF systemd[1]: Started Kibana.
```

---

## ****Step 5. Check Kibana WebUI****

- Make sure it connects to ElasticSearch well
    - URL : **[http://localhost:5601/](http://localhost:5601/)**
        
        ![](/images/Setting/elasticsearch_kibana/2.png)
        

---

## Reference

- [https://dschloe.github.io/settings/elasticsearch_kibana_wsl2/](https://dschloe.github.io/settings/elasticsearch_kibana_wsl2/)
- [https://www.how2shout.com/how-to/install-uninstall-elasticsearch-ubuntu-19-04-18-04-16-04.html](https://www.how2shout.com/how-to/install-uninstall-elasticsearch-ubuntu-19-04-18-04-16-04.html)