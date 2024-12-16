---
title: "[Git] Windows11에서 Git 설치하기"
categories:
  - etc
tag:
  - git
  - windows11
author: "Jiwon Kang"
date: 2022-10-17 16:14:08
---


## Git 설치파일 다운로드

1. [git-scm.com](https://git-scm.com/) 에서 Downloads 클릭
    
    ![](/images/etc/git_install/0.png)  
    


1. 현재 사용 중인 운영체제(Windows) 클릭
    
    ![](/images/etc/git_install/1.png)  
    


1. 현재 사용 중인 시스템 아키텍처(64비트)에 해당하는 링크를 클릭하여 설치 파일 다운
    
    ![](/images/etc/git_install/12.png)  


<br>

## Git Setup 마법사 실행

1. 다운로드받은 Git Setup 파일을 실행
    
    ![](/images/etc/git_install/13.png)  
    


1. 설치하기 위한 경로 지정 후 Next 클릭
    
    ![](/images/etc/git_install/14.png)  
    


1. 설치할 구성요소 선택 후 Next 클릭
    
    ![](/images/etc/git_install/15.png)  
    
    - 일반적으로 기본 상태 그대로 진행해도 무관
        - Additional icons
            - On the Desktop : 바탕화면에 바로가기 아이콘 추가
        - Windows Explorer integration
            - Git Bash Here : Git Bash 연결 기능
            - Git GUI Here : Git GUI 연결 기능
        - Git LFS ( Large File Support) : 대용량 파일 지원 여부
        - Associate .git* configuration files with the default text editor : Git 구성 파일을 기본 텍스트 편집기와 연결할지 여부
        - Associate .sh files to be run with Bash : `.sh` 확장자 파일을 Bash와 연결할지 선택
        - Check daily for Git for Windows updates : Git 업데이트를 매일 체크할지 여부
        - Add a Git Bash Profile to Windows Terminal : 윈도우 터미널에 Git Bash 추가할지 여부


1. 시작 폴더 경로 지정 후 Next 클릭
    
    ![](/images/etc/git_install/16.png)  
    


1. 기본 Git 에디터 선택 후 Next 클릭
    
    ![](/images/etc/git_install/17.png)  
    
    - 기본 옵션은 Vim 편집기이며, Notepad, VSCode, Sublime 등등 선택 가능


1. Branch 이름 지정 옵션 선택 후 Next 클릭
    
    ![](/images/etc/git_install/18.png)  
    
    - Let Git decide : 기본적으로 master로 지정, 추후 변경 가능
    - Override the default branch name for new repositories : 입력한 이름으로 자동 지정
        - 현재 대부분의 경우 main으로 통용되고 있음


1. 이후 옵션들은 별도 지정이나 변경 없이 넘어가고, 마지막 Install 시 설치 진행
    
    ![](/images/etc/git_install/19.png)  
    
    ![](/images/etc/git_install/2.png)  
    
    ![](/images/etc/git_install/3.png)  
    
    ![](/images/etc/git_install/4.png)  
    
    ![](/images/etc/git_install/5.png)  
    
    ![](/images/etc/git_install/6.png)  
    
    ![](/images/etc/git_install/7.png)  
    
    ![](/images/etc/git_install/8.png)  
    
    ![](/images/etc/git_install/9.png)  
    
    ![](/images/etc/git_install/10.png)  
    


1. 모든 설치가 완료된 후 Finish 클릭

<br>

## Git Bash 사용자 정보 입력

1. Git Bash 실행 후 사용자 정보 등록
    - 사용자 정보를 등록하면 로컬에서 Git 커밋 시 항상 이 정보가 사용됨
        
        ```bash
        git config --global user.name "Name"
        git config --global user.email "Email"
        ```
        
    - .gitconfig에 저장되어 있는 설정 값 확인 : `cat ~/.gitconfig`
    ![](/images/etc/git_install/11.png)  

<br>

### Ref.

[https://iboxcomein.com/windows-git-install/](https://iboxcomein.com/windows-git-install/)