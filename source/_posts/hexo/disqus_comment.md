---
title: "Disqus로 블로그 댓글 기능 설정"
categories:
  - hexo
tag:
  - hexo
  - hueman
  - disqus
author: "Jiwon Kang"
date: 2022-11-16 18:55:51
---


![](/images/hexo/disqus/0.png)

Hexo 블로그의 Hueman 테마는 기본적으로 Disqus 서비스를 지원하며, 이를 통해 블로그의 댓글 기능을 설정할 수 있다. ([Hexo 블로그 Hueman 테마 설정](https://gonekng.github.io/2022/11/16/hexo/hueman_theme/))

## Disqus 회원가입

- Disqus 사이트에 회원가입 후 로그인한다.

<br>

## Disqus 사이트 추가

- 메인 페이지에서 `Get Started` 클릭
    
    ![](/images/hexo/disqus/1.png)
    
- `I want to install Disqus on my site` 클릭
    
    ![](/images/hexo/disqus/2.png)
    
- `Website Name`, `Category`, `Language` 지정
    
    ![](/images/hexo/disqus/3.png)
    
- `Basic` 요금제 선택
    
    ![](/images/hexo/disqus/4.png)
    
- `I don’t see my platform listed, install manually with Universal Code` 클릭
    
    ![](/images/hexo/disqus/5.png)
    
- `configure` 클릭
    
    ![](/images/hexo/disqus/6.png)
    
- `Website URL` 항목에 블로그 주소 입력 후 `Next` 클릭
    
    ![](/images/hexo/disqus/7.png)
    
- `Balanced` 옵션 선택 후 `Complete Setup` 클릭
    
    ![](/images/hexo/disqus/8.png)
    
- `Dismiss Setup` 클릭
    
    ![](/images/hexo/disqus/9.png)
    
- 오른쪽 상단에 있는 `Edit Settings` 클릭
    
    ![](/images/hexo/disqus/10.png)
    
- `Shortname` 항목에 있는 나의 Shortname 확인

    ![](/images/hexo/disqus/11.png)

<br>

## **_config.icarus.yml에 Shortname 설정하기**

- 블로그 테마 폴더의 `_config.yml` 파일에서 다음 위치에 나의 Disqus Shortname을 입력한다.
    
    ```markdown
    # Comment
    comment:
        disqus: gonekng # enter disqus shortname here
    ```
    
<br>

### Reference

- [https://chinsun9.github.io/2020/09/23/hexo/disqus로-블로그-댓글-사용하기/](https://chinsun9.github.io/2020/09/23/hexo/disqus%EB%A1%9C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%8C%93%EA%B8%80-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/)