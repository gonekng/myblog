---
title: "Link VSCode with Remote WSL"
categories:
  - setting
tag:
  - setting
  - data engineering
  - wsl2
  - vscode
author: "Jiwon Kang"
date: 2022-04-15 17:33:16
---
  

## Step 1. Install VSCode

- URL : **[https://code.visualstudio.com/download](https://code.visualstudio.com/download)**
- Download the **System Installer** for each OS.
    
    ![](/images/Setting/vscode_remotewsl2/1.png)
    

- Check ‘Add to PATH’ and reboot after installation.
    
    ![](/images/Setting/vscode_remotewsl2/2.png)
    

---

## Step 2. Link Remote WSL

- Install Remote WSL in Extension tab of VSCode.
    
    ![](/images/Setting/vscode_remotewsl2/3.png)
    

- **(File tab → Open Folder)** Select the airflow-test folder that WSL installed.
    
    ![](/images/Setting/vscode_remotewsl2/4.png)
    

- **(Terminal → New Terminal)** Open a new terminal and add a WSL terminal.
    
    ![](/images/Setting/vscode_remotewsl2/5.png)
    
    ![](/images/Setting/vscode_remotewsl2/6.png)
    

- Activate the virtual environment in WSL terminal.
    
    ![](/images/Setting/vscode_remotewsl2/7.png)
    

- Run a python code and check if it is printed well.
    - ex) main.py
    
    ![](/images/Setting/vscode_remotewsl2/8.png)
    

## Reference

- [https://dschloe.github.io/settings/vscode_wsl2/](https://dschloe.github.io/settings/vscode_wsl2/)