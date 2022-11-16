---
title: "Hexo 블로그 생성"
categories:
  - hexo
tag:
  - hexo
  - github
author: "Jiwon Kang"
date: 2022-03-17 11:14:21
---

# Hexo 설치

- node.js 설치
    - 옵션 - Chocolatey도 함께 설치
- 바탕화면 git bash에 입력
    - `node -v` : 버전 확인
    - `npm install -g hexo-cli` : hexo command line 설치
    - `hexo init myblog` : 바탕화면에 myblog 폴더 생성
- myblog 폴더 위치에서 Git Bash 열고 `hexo server` 입력
    - 출력되는 링크로 이동하여 hexo 서버가 잘 열리는지 확인

# 깃허브 레포지토리 생성

- 깃허브 로그인 후 profile - new repositories - new 클릭
    - Repository 이름은 myblog로 지정 (로컬에 생성한 폴더 이름으로 지정해야함)
    - 별도의 옵션 없이 Creating repository 클릭
- myblog 폴더 위치에서 Git Bash 열고 아래 코드 한 줄씩 입력
    
    ```bash
    1 echo "# myblog" >> README.md
    2 git init
    3 git add README.md
    4 git commit -m "first commit"
    5 git branch -M main
    6 git remote add origin https://github.com/[깃허브아이디]/myblog.git
    7 git push -u origin main
    ```
    
    1. 해당 레포지토리에 README.md 파일 생성
    2. 새로운 git 저장소를 해당 로컬 폴더에 초기화
    3. README.md 파일을 git에 추가
    4. git에 추가된 모든 내용 커밋 (커밋 메시지는 자유롭게 지정 가능)
        - 사용자 에러 발생 시 아래 코드 입력
            
            ```bash
            git config --global user.email “[이메일주소]”
            git config --global user.name “[깃허브아이디]”
            ```
            
    5. git 브랜치를 main으로 변경
        - git 초기화 시 기본값은 master이나, 대부분의 프로젝트에서 main을 사용하기 때문에 초기에 변경해주는 것이 좋음
    6. 해당 로컬 폴더에 깃허브 레포지토리를 연결
    7. 커밋한 내용 푸시
        - 초기 세팅 이후에는 add, commit, push 명령어만 입력
- 깃허브에서 새로고침 후 업로드된 README.md 파일 확인

# Hexo 블로그 생성

- 깃허브에서 새로운 Repository 생성 (이름 : `[깃허브아이디].github.io`)
- myblog 폴더 위치에서 Git Bash 열고 아래 코드 입력

```bash
$ npm install
$ npm install hexo-server --save
$ npm install hexo-deployer-git --save
```

- 블로그 폴더 안에 잇는 `_config.yml` 파일 내용 수정
    - `title`, `subtitle`, `author` 등 세부사항 입력
    - 깃허브 블로그 연결 : `url`에 깃허브 블로그 주소 입력 (ex. `https://[깃허브아이디].github.io`)
    - 배포 관련 설정 : 맨 아래 `deploy`에 다음과 같이 입력
        
        ```bash
        deploy:
          type: git
          repo: https://github.com/[깃허브아이디]/[깃허브아이디].github.io.git
          branch: main
        ```
        
- myblog 폴더 위치에서 Git Bash 열고 `hexo generate --deploy` 입력
    - `Deploy done`이라는 메시지가 출력되면 배포 완료된 것
    - 게시글 추가 또는 수정할 때마다 위의 코드 입력

# 블로그 테마 변경

- [https://hexo.io/themes/](https://hexo.io/themes/) 에서 테마 정해서 해당 테마의 Github으로 이동
    - TIP : 최근에도 지속적으로 업데이트 되고 있는지 확인
- `npm install hexo-theme-[테마명]` 입력
- `hexo config theme [테마명]` 입력
- `hexo server` 입력
    - 이때 에러가 발생하는 경우 `npm install --save bulma-stylus@0.8.0 hexo-renderer-inferno@^0.1.3` 입력
- `hexo clean` 을 통해 정리한 후 `hexo generate --deploy` 로 블로그에 배포

# R 마크다운 업로드

1. R 마크다운 소스에서 개요 부분 수정
    
    ```r
    output:
        html_document:
            keep_md: true
    ```
    
2. R에서 Knit 버튼 클릭하면 해당 디렉토리에 md 파일 생성됨
3. myblog/source/_posts 경로에 해당 파일 복사 후 내용 수정
    - R 디렉토리에 있는 blog_files 폴더를 myblog/source/images 경로에 복사 후 md 파일에 있는 이미지 링크 수정 및 배포

# Google Colab 업로드

1. google colab > 파일 > 다운로드 > .ipynb 다운로드
2. Jupiter Lab에서 다운로드한 파일 열고 File > Save and Export Notebook As > Markdown
3. 생성된 md 파일 및 이미지를 블로그 폴더로 복사 후 배포