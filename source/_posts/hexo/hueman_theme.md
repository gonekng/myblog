---
title: "Hexo 블로그 Hueman 테마 설정"
categories:
  - hexo
tag:
  - hexo
  - hueman
author: "Jiwon Kang"
date: 2022-11-16 17:01:23
---

# Install theme

1. 블로그와 연결된 루트 폴더에서 git 명령어로 `Hueman` 테마를 다운로드한다.

```bash
$ git clone [https://github.com/ppoffice/hexo-theme-hueman.git](https://github.com/ppoffice/hexo-theme-hueman.git) themes/hueman
```

2. 블로그의 `_config.yml`을 수정합니다.

```bash
theme: hueman
```

3. themes 폴더 안에 있는 `_config.yml.example`의 이름을 `_config.yml`로 수정한다.  

4. 검색 기능을 위해 `hexo-generator-json-content`를 설치한다.

```bash
$ npm install -S hexo-generator-json-content
```

<br>

# Change settings

앞에서 이름을 변경했던 `_config.yml` 파일을 수정하면 각종 설정을 변경할 수 있다.

### **메뉴**

```bash
# Menus
menu:
    Home: /
    # Delete this row if you don't want categories in your header nav bar
    Categories:
    About: https://about.me/gonekng
```

- 각 메뉴를 클릭했을 때 이동할 경로를 지정할 수 있다. 이때 카테고리는 따로 지정하지 않아도 각 게시글에서 지정한대로 자동 적용된다.
- About 메뉴는 블로그 주인에 대한 자기소개 페이지로 이동하기 위한 것으로, 필자는 [About.me](http://about.me/) 라는 사이트를 이용하여 만든 프로필 URL을 연결했다.


### 커스터마이징

```bash
# Customize
customize:
    logo:
        width: 165
        height: 60
        url: images/logo-header.png
    theme_color: '#006bde'
    highlight: androidstudio
    sidebar: right # sidebar position, options: left, right
    thumbnail: false # enable posts thumbnail, options: true, false
    favicon:  # path to favicon
    social_links: # for more icons, please see http://fontawesome.io/icons/#brand
        instagram: https://instagram.com/gone_kng
        github: https://github.com/gonekng
```

- 메뉴 위에 삽입할 로고 파일 url을 지정할 수 있다. `hueman/source/css/images` 폴더 내부에 저장된 이미지를 사용할 수도 있고, 웹 이미지 url도 가능하다.
- 테마의 색상을 지정할 수 있다.
- 게시글에 포함된 코드 블럭에서 적용되는 하이라이트를 지정할 수 있다. 기본값은 `androidstudio`이며, `hueman/source/css/_highlight` 폴더에 있는 것들 중 선택할 수 있다.
- 사이드바의 위치를 조정할 수 있다.
- 게시글의 썸네일을 표시하거나 숨길 수 있다.
    - 게시글의 썸네일은 게시글에 포함된 첫번째 사진이 기본값이며, 게시글의 front-matter 부분에서 경로를 추가하면 변경 가능하다.
        
        ```markdown
        title: Hello World
        date: 2022/11/16 16:36:10
        thumbnail: images/example.jpg
        ```
        
- 파비콘(URL 앞에 붙는 작은 아이콘)을 지정할 수 있다.
- 연결하고자 하는 SNS 링크를 추가할 수 있다. 아이콘은 [FontAwesome](http://fontawesome.io/icons/#brand)에서 선택하여 이름과 URL을 지정하면 적용된다.


### **위젯**

```bash
# Widgets
widgets:
    - recent_posts
    - category
    - archive
    - tagcloud
    - tag
    - links
```

- 사이드바에 추가되는 다양한 위젯을 지정할 수 있으며, 작성한 순서대로 차례로 보여지게 된다.
- 링크 위젯에 들어갈 내용은 `_config.yml` 하단에서 다음의 코드를 통해 추가할 수 있다.
    
    ```bash
    # Miscellaneous
    miscellaneous:
        links:
            Hexo: http://hexo.io
            Naver blog: https://blog.naver.com/donumm
    ```
    

### **검색**

```bash
# Search
search:
    insight: true # you need to install `hexo-generator-json-content` before using Insight Search
    swiftype: # enter swiftype install key here
    baidu: false # you need to disable other search engines to use Baidu search, options: true, false
```

- 블로그 내의 검색 기능을 설정할 수 있다. 필자는 테마에서 기본적으로 제공하는 Insight Search를 사용하였다. 앞서 언급했듯이 `hexo-generator-json-content`를 설치해야 사용 가능하다.


### **댓글**

```bash
# Comment
comment:
    disqus: gonekng # enter disqus shortname here
```

- 댓글 기능은 기본적으로 제공하는 [Disqus](https://disqus.com/) 서비스를 사용하면 된다.  [Disqus](https://disqus.com/) 사이트에 회원가입 및 로그인 후 해당하는 아이디를 입력한다.
- 자세한 내용은 [Disqus로 블로그 댓글 기능 설정](https://gonekng.github.io/2022/11/16/hexo/disqus_comment/) 참조


### **공유**

```bash
# Share
share: default # options: jiathis, bdshare, addtoany, default
```

- 해당 게시글의 공유 기능에도 몇가지 옵션이 있으나, 필자는 기본값으로 설정하였다.

<br>

# Result

![](/images/hexo/hueman_result.png)


### Reference

- [https://futurecreator.github.io/2016/06/14/hexo-apply-hueman-theme/](https://futurecreator.github.io/2016/06/14/hexo-apply-hueman-theme/)