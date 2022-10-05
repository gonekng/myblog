---
title: "Creating github blog with hexo"
categories:
  - hexo
tag:
  - hexo
  - github
author: "Jiwon Kang"
date: 2022-03-17 17:18:21
---

### Repesitory 생성

- node.js 설치
    - 옵션 - Chocolatey도 같이 설치해야 함
- 바탕화면 git bash에 입력
    - node -v : 버전 확인
    - npm install -g hexo-cli : hexo 뭐시기 설치
    - hexo init myblog : 바탕화면에 myblog 폴더 생성
- myblog 폴더 오른쪽 클릭해서 open foler as pycharm
- pycharm terminal에 Git Bash 추가한 후 hexo server 입력
- github에서 profile - new repesitories - new 클릭
    - Repository 이름은 myblog로 설정
    - Creating repository 하면 생성
- pycharm terminal Git Bast에 아래 소스 한줄씩 입력
    
    ```bash
    echo "# myblog" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/gonekng/myblog.git
    git push -u origin main
    ```
    
    - 4번째 줄에서 나오는 에러를 해결해야 함
        - git config --global [user.email](http://user.email) “donumm64@gmail.com”
        - git config --global [user.name](http://user.name) “gonekng”
        - 그러고 나면 1 file changed, 1 insertion(+) 어쩌고 나옴
    - 5번째 줄 입력하면 master에서 main으로 바뀜
    - 끝까지 입력하고 Sign in 창에서 비밀번호 입력까지 완료
- github에서 새로고침하고 ReadMe 파일 확인

### 소스 코드 설명

```bash
echo "# myblog" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gonekng/myblog.git
git push -u origin main
```

- echo "# myblog" : [README.md](http://README.md) 생성
- git add 파일명 : 해당 파일명 업로드
- git add . : 모든 파일 업로드
- git commit : 커밋 메시지 ex) “UPDATE”, “First Commit”
- git remote : 로컬 폴더와 github 주소를 연동
- git push : 최종 업로드 단계
- 한번 폴더 세팅이 끝나고 나면 3,4,7번째 줄만 입력하면 됨
    - 파일명, 메시지명 바꾸기
    - 마지막 줄도 git push만 입력

### hello-world 수정

- [hello-world.md](http://hello-world.md) 파일에서 내용 수정 후 브라우저 열어서 확인
- git add . / git commit -m “updated” / git push 차례로 입력

### 블로그 생성

```
$ hexo init myblog
$ cd myblog
$ npm install
$ npm install hexo-server --save
$ npm install hexo-deployer-git --save
```

- 위의 두 줄은 경로를 지정했으면 스킵
- 아래 세 줄 그대로 pycharm Git Bash 창에 입력
- _config.yml 에서 내용 수정
    - title, subtitle, author 등 수정 후 브라우저에서 확인
    - url : `https://gonekng.github.io`
    - 맨 아래 Deployment 에 아래 소스 입력
    
    ```
    deploy:
      type: git
      repo: https://github.com/gonekng/gonekng.github.io.git
      branch: main
    ```
    
- 새로운 Repository 이름으로 [gonekng.github.io](http://gonekng.github.io) 지정하여 생성
- pycharm Git Bash에서 hexo generate 입력
    - css뭐시기 쫘르륵 나와야함
- pycharm Git Bash에서 hexo deploy 입력
    - Deploy done: git 나와야 함
    - github에서 해당 Repository 확인
- 브라우저 URL창에 [gonekng.github.io](http://gonekng.github.io) 입력하면 창 열림
- 추가/수정 할때마다 hexo generate --deploy 입력

### 새로운 포스트 발행

- pycharm Git Bash에서 hexo new “[파일명]” 입력
    - pycharm에 파일 생성된거 확인
- title 및 내용 추가/수정 후 hexo server 에서 확인
- hexo generate --hexo deploy 로 github 블로그에 배포

### 블로그 테마 변경

- ICARUS 테마
    - `npm install -S hexo-theme-icarus` 입력
    - `hexo config theme icarus` 입력
    - hexo server 에서 에러 나는 경우 `npm install --save bulma-stylus@0.8.0 hexo-renderer-inferno@^0.1.3` 입력
    - hexo clean 을 통해 정리한 후 hexo generate --hexo deploy 로 github 블로그에 배포
- [https://hexo.io/themes/](https://hexo.io/themes/) 에서 테마 정해서 해당 테마의 Github으로 이동 (중국어는 거르자)
    - 최근에도 지속적으로 업데이트 되고 있는지 확인
    - `npm install hexo-theme-[테마명]` 입력
    - `hexo config theme [테마명]` 입력
    

### R 마크다운 업로드

- R 마크다운 소스에서 개요 부분 수정
    
    ```r
    output:
        html_document:
            keep_md: true
    ```
    
- R에서 Knit 하면 해당 디렉토리에 md파일 생성됨
    - myblog > source > _posts 에 복사
    - pycharm에서 md 파일 열어서 내용 수정 및 배포
- R 디렉토리에 있는 blog_files 폴더를 myblog > source > images 에 복사
    - pycharm에서 md 파일 열어서 이미지 링크 수정 및 배포