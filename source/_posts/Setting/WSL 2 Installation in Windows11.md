---
title: "WSL 2 Installation in Windows11"
categories:
  - setting
tag:
  - setting
  - data engineering
  - wsl2
author: "Jiwon Kang"
date: 2022-04-15 11:43:19
---

## Step 1. Enable WSL-related features by DISM

- Run Windows Terminal as administrator
    
    ![](/images/Setting/wsl2/Untitled.png)
    

- Enable Microsoft-Windows-Subsystem-Linux Features

```
$ dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

- Enable the VirtualMachinePlatform feature
    - Reboot if the operation is completed successfully.

```
$ dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

## Step 2. **WSL2 Kernel Update**

- Install the update file from the link below.
    - URL : [https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

- Open Windows terminal and change WSL version to 2.

```
$ wsl --set-default-version 2
```

- Install Ubuntu, the most popular Linux distribution, and run as administrator.
    
    ![](/images/Setting/wsl2/Untitled 1.png)
    

- In Ubuntu, Set the username and password.
- Check the currently installed version with wsl -l -v

```
$ wsl -l -v
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

- If it says version 1, execute the following command.

```
$ wsl --set-version Ubuntu 2

변환이 진행 중입니다. 몇 분 정도 걸릴 수 있습니다...
WSL 2와의 주요 차이점에 대한 자세한 내용은 [https://aka.ms/wsl2를](https://aka.ms/wsl2%EB%A5%BC) 참조하세요
변환이 완료되었습니다.
```

- Make sure that it says version 2.

```
$ wsl -l -v
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

## Reference

- [https://www.lainyzine.com/ko/article/how-to-install-wsl2-and-use-linux-on-windows-10/#google_vignette](https://www.lainyzine.com/ko/article/how-to-install-wsl2-and-use-linux-on-windows-10/#google_vignette)