---
title: "Crawling Data from Web"
categories:
  - python
  - crawling
tag:
  - python
  - crawling
  - BeautifulSoup
author: "Jiwon Kang"
date: 2022-04-22 12:39:12
---

## Step 1. Set virtual environment

- Create a new directory under the C drive and virtual environment.

```python
$ mkdir crawling && cd crawling
$ virtualenv venv
$ sourve venv/Scipts/activate
```

- Install some required packages.

```python
$ pip install beautifulsoup4
$ pip install numpy pandas matplotlib seaborn
$ pip install requests
```

## Step 2. Crawling Practice 1

- Create a HTML file `index.html`
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <titl>test</titl>
    </head>
    <body>
        <h1>aaaaaaaa</h1>
        <h2>dddd</h2>
        <div class="chapter01">
            <p>Don't Crawl here </p>
        </div>
        <div class="chapter02">
            <p>Just Crawling here</p>
        </div>
    		<div id="main">
    		    <p> Crawling .................. </p>
        </div>
    </body>
    </html>
    ```
    

- Create a python file `main.py` crawling text from `index.html`
    
    ```python
    from bs4 import BeautifulSoup
    def main():
        # Convert index.html to BeautifulSoup Object
        soup = BeautifulSoup(open("index.html", encoding='UTF-8'), "html.parser")
        print(type(soup))
    
        print(soup.find("p"))
        print("----------------")
        print(soup.find_all("p"))
        print("----------------")
        print(soup.find("div", class_ = "chapter02"))
        print("----------------")
        print(soup.find("div", id = "main").find("p").get_text())
    
    if __name__ == "__main__":
        main()
    ```
    

- Run the `main.py` and check the result printed.
    
    ```bash
    $ python main.py
    
    <class 'bs4.BeautifulSoup'>
    <p>Don't crawl here!</p>
    ----------------
    [<p>Don't crawl here!</p>, <p>Just Crawl here!</p>, <p> Crawling .................. </p>]
    ----------------
    <div class="chapter02">
    <p>Just Crawl here!</p>
    </div>
    ----------------
    ```
    

## Step 3. Quick Start BeautifulSoup4

- URL : [https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)
- `index2.html`
    
    ```html
    <!DOCTYPE html>
    <html>
            <head>
                    <title>The Dormouse's story</title>
            </head>
            <body>
                    <p class="title"><b>The Dormouse's story</b></p>
                    <p class="story">
                            Once upon a time there were three little sisters; and their names were
                            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
                            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                            and they lived at the bottom of a well.
                    </p>
                    <p class="story">...</p>
            </body>
    </html>
    ```
    

- `temp1.py`
    
    ```python
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open("index2.html"), 'html.parser')
    
    print(soup.prettify())
    ```
    
    ```bash
    $ python temp1.py
    
    <!DOCTYPE html>
    <html>
     <head>
      <title>
       The Dormouse's story
      </title>
     </head>
     <body>
      <p class="title">
       <b>
        The Dormouse's story
       </b>
      </p>
      <p class="story">
       Once upon a time there were three little sisters; and their names were
       <a class="sister" href="http://example.com/elsie" id="link1">
        Elsie
       </a>
       ,
       <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>
       and
       <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>
       ;
                            and they lived at the bottom of a well.
      </p>
      <p class="story">
       ...
      </p>
     </body>
    </html>
    ```
    

- `temp2.py`
    
    ```python
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open("index2.html"), 'html.parser')
    
    print(soup.title)
    print("----------------")
    print(soup.title.name)
    print("----------------")
    print(soup.title.string)
    print("----------------")
    print(soup.title.parent.name)
    print("----------------")
    print(soup.p)
    print("----------------")
    print(soup.p['class'])
    print("----------------")
    print(soup.a)
    print("----------------")
    print(soup.find_all('a'))
    print("----------------")
    print(soup.find(id="link3"))
    ```
    
    ```bash
    $ python temp2.py
    
    <title>The Dormouse's story</title>
    ----------------
    title
    ----------------
    The Dormouse's story
    ----------------
    head
    ----------------
    <p class="title"><b>The Dormouse's story</b></p>
    ----------------
    ['title']
    ----------------
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    ----------------
    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    ----------------
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    ```
    

- `temp3.py`
    
    ```python
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open("index2.html"), 'html.parser')
    
    for link in soup.find_all('a'):
        print(link.get('href'))
    
    print(soup.get_text())
    ```
    
    ```bash
    $ python temp3.py
    
    http://example.com/elsie
    http://example.com/lacie
    http://example.com/tillie
    
    The Dormouse's story
    
    The Dormouse's story
    
                            Once upon a time there were three little sisters; and their names were
                            Elsie,
                            Lacieand
                            Tillie;
                            and they lived at the bottom of a well.
    
    ...
    ```
