---
title: "# [Git] .gitignore 다루기"
categories:
  - etc
tag:
  - git
author: "Jiwon Kang"
date: 2024-12-16 21:31:11
---

## .gitignore란?

Git으로 프로젝트를 관리할 때, 특정 파일이나 디렉토리를 Git이 추적하지 않도록 설정하는 파일로,  일반적으로 다음과 같은 파일들을 Git 추적 대상에서 제외한다:

- 빌드 결과물 (build/, dist/ 등)
- 의존성 파일 (node_modules/, vendor/ 등)
- IDE 설정 파일 (.idea/, .vscode/ 등)
- 환경 설정 파일 (.env, config.json 등)
- 로그 파일 (*.log)

### .gitignore 파일 생성

다음의 명령어를 실행하여 .gitignore 파일을 생성하며, 편집기에서 파일의 내용을 작성한 다음 add, commit, push의 순서로 실행하여 적용할 수 있다.

```bash
$ touch .gitignore
```

- `touch` 명령어는 파일의 생성 및 날짜/시간을 수정하는 명령어
- 해당 파일이 없을 경우 크기가 0인 파일을 생성하며, 이미 존재할 경우 수정 시간이 업데이트된다. (파일 내용 수정 X)

### (TIP) .gitignore 파일을 생성해주는 사이트

[gitignore.io](https://www.toptal.com/developers/gitignore)

---

## .gitignore 작성 방법

프로젝트의 루트 디렉토리에 `.gitignore` 파일을 생성하고 다음과 같은 패턴을 활용하여 작성한다.

- `#` : 주석 표기
- `*` : 모든 문자와 매칭
- `?` : 한 개의 문자와 매칭
- `**` : 모든 디렉토리 검색
- `/` : 디렉토리 구분
    - `/`로 시작하면 하위 디렉토리에 적용되지 않음
    - `/`로 끝나면 해당 디렉토리 전체로 간주
- `!` : 무시하지 않음 (예외 처리)

### 예시

```bash
# ignore all .a files
*.a

# exclude lib.class from "*.a", meaning all lib.a are still tracked
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all json files whose name begin with 'temp-'
temp-*.json

# only ignore the build.log file in current directory, not those in its subdirectories
/build.log

# specify a folder with slash in the end
# ignore all files in the build/ directory
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory
# /** matches 0 or more directories
doc/**/*.pdf
```

### 적용 시 주의사항

- .gitignore 파일은 Git이 추적을 시작하기 전에 설정하는 것이 좋다.
- 이미 Git이 추적 중인 파일은 .gitignore에 추가해도 즉시 적용되지 않으며, 추가로 적용하려면 다음의 명령어를 실행해야 한다.
    
    ```bash
    # Git의 캐시를 삭제
    git rm -r --cached .
    
    # 모든 파일을 다시 추가
    git add .
    
    # 변경사항을 커밋
    git commit -m "Apply .gitignore"
    ```
    

---

## Reference

[[Git] .gitignore 이해 및 적용하기](https://yuevelyne.tistory.com/entry/Git-gitignore-%EC%9D%B4%ED%95%B4-%EB%B0%8F-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)

[[Git] Xcode 프로젝트에 .gitignore 파일 생성하기](https://gun-oo.tistory.com/m/14)