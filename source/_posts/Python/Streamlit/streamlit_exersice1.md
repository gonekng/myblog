---
title: "Streamlit을 이용한 지도 시각화 예제"
categories:
  - python
  - streamlit
tag:
  - python
  - streamlit
author: "Jiwon Kang"
date: 2023-04-06 22:29:04
---

# Streamlit이란?

Python으로 작성된 **데이터 시각화 및 웹 애플리케이션 개발용 프레임워크**로,  
웹 어플리케이션 개발 시간을 줄일 수 있고, 데이터 시각화 라이브러리와 연동하여 직관적인 분석이 가능한 것이 특징이다.  
다만, 다른 웹 프레임워크에 비해 고급 기능이나 복잡한 애플리케이션을 만드는 데에는 다소 제한적이다.  


# Streamlit 예제

이번 예제는 지인들과의 약속 장소를 정하던 중 Streamlit을 이용하여 홍대입구역까지의 거리를 알아보기 위해 만든 웹애플리케이션이다.  
Folium 패키지를 이용하여 지도 상에 각 위치를 표시하고, Streamlit에서 제공하는 탭 기능을 이용하여 데이터와 지도를 함께 제공한다.
이때 Vworld에서 제공하는 API를 통해 지도에 배경 레이어를 삽입하여 보기 쉽게 시각화하였다.  


## 1. 필요한 라이브러리 Import

```python
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import folium
import vworld_key
```

- `numpy` : 수치 계산을 위한 라이브러리
- `pandas` : 데이터를 다루기 위한 라이브러리
- `streamlit` : 파이썬 기반의 웹 애플리케이션 개발 도구
- `PIL` : 이미지 처리 라이브러리
- `folium` : 지도 시각화 라이브러리
- `vworld_key` : 지도 API를 사용하기 위한 API 키 (비공개)


## 2. 페이지 기본 설정

```python
st.set_page_config(page_title='Where to meet', page_icon='🌱', layout="wide")
```

- `streamlit`에서 제공하는 `set_page_config()` 함수를 사용하여 페이지 설정 가능
    - layout : 페이지의 레이아웃 설정 (wide, centered 등)
    - theme : 페이지의 테마 설정 (light, dark, colorblind 등)


## 3. 사이드바 커스터마이징

```python
st.sidebar.image(Image.open('streamlit_logo.png'))
st.sidebar.write("---")

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
color = ['black', 'black', 'black', 'white', 'white', 'white', 'white']
text = 'WELCOME'
for r, c, t in zip(rainbow, color, text):
    st.sidebar.markdown(f"<h3 style='color:{c}; background-color:{r}'>__{t}:</h3>", unsafe_allow_html=True)
st.sidebar.write("---")
st.sidebar.text("This is Jiwon!\nNice to meet you!")
```

- `st.sidebar` 함수를 사용하여 사이드바를 커스터마이징할 수 있음
    - `st.sidebar.image()` 함수로 이미지를 출력
        -  Image 라이브러리의 open 함수를 사용하여 저장된 이미지 파일을 불러옴
    - `st.sidebar.write()` / `st.sidebar.markdown()` / `st.sidebar.text()`
        - write 함수에 "---" 입력하여 화면에 구분선 추가
        - unsafe_allow_html : html 태그를 사용할 수 있도록 허용하는 기능


## 4. 메인 화면 작성

```python
st.header("A Letter From Peter")
st.subheader(':blue["Let me know where we will meet on Satuerday, with the dashboard made by streamlit."]')
st.write("---")
```

- `st.header()` / `st.subheader()` 함수로 제목 및 부제목을 지정


### 4-1. 레이아웃 (컬럼 분할)

```python
col1, col2 = st.columns([1,2])
with col1:
    st.image(Image.open('question.jpg'))

with col2:
    st.subheader(':blue["What about 홍대입구?"]')
```

- `st.columns()` : 화면을 분할하고자 하는 컬럼 개수 및 크기만큼 리스트 형태로 입력
- with 구문으로 각 컬럼에서 출력하고자 하는 내용 작성


### 4-2. 데이터 Load

```python
center = [37.5575,126.9245] # 홍대입구역 좌표

# 데이터 불러오기
df = pd.read_csv("place.csv", encoding='utf-8')
df['to_홍대'] = np.round(np.sqrt(np.power((df['Lat']-center[0]),2) + np.power((df['Lon']-center[1]),2)),2)
```

- 본 예제에서는 기준점으로 사용할 데이터로 홍대입구역의 좌표를 사용함
- csv 파일을 불러온 후, 각 지역에 대하여 홍대입구와의 거리를 나타내는 `to_홍대` 라는 새로운 컬럼 생성
    - `np.power()` : 첫번째 인수를 두번째 인수만큼 거듭제곱하는 함수
    - `np.sqrt()` :  양의 제곱근을 계산하는 함수
    - `np.round()` : 첫번째 인수를 두번째 인수의 자릿수까지 반올림하는 함수


### 4-3. 탭 기능 추가

```python
tab1, tab2 = st.tabs(['On Map', 'Raw Data'])

with tab2:
    st.write(df)
    
with tab1:
		st.write("---")
```

- `st.tabs()`  : 화면에 출력하고자 하는 탭의 이름을 리스트 형태로 입력
- with 구문으로 각 탭에서 출력하고자 하는 내용 작성


## 5. 지도 시각화

### 5-1. 지도 객체 생성

```python
m = folium.Map(location=center, zoom_start=11, min_zoom=9, max_zoom=12)
```

- `folium` 라이브러리의 `Map()` 함수를 사용하여 지도 객체를 생성
    - location : 지도의 중심점 좌표 정보가 담긴 변수를 전달
    - zoom_start : 초기 확대/축소 수준을 지정합니다.
        - min_zoom / max_zoom : 최소/최대 줌 수준 지정


### 5-2. 배경 레이어 삽입(*vworld API)

```python
tiles = f"http://api.vworld.kr/req/wmts/1.0.0/{vworld_key.key}/Base/{{z}}/{{y}}/{{x}}.png"
folium.TileLayer(
    tiles=tiles,
    attr="Vworld",
    overlay=True,
    control=True
).add_to(m)
```

- 지도의 배경 레이어는 공간정보 오픈플랫폼 오픈API([https://www.vworld.kr/dev/v4api.do](https://www.vworld.kr/dev/v4api.do))를 사용하여 삽입하였음
    - `{{z}}`, `{{y}}`, `{{x}}`는 folium에서 동적으로 생성되는 변수로, `tiles` URL에 삽입되어 해당 위치의 타일을 요청함
- `folium.TileLayer()` : 지도 객체의 배경 레이어를 설정하는 함수
    - tiles : 타일 이미지의 URL 또는 타일 이미지를 제공하는 Provider의 이름을 지정
    - attr : 타일 제공자의 속성 정보를 설정
    - overlay : 타일 레이어가 지도의 오버레이로 표시될지 여부 설정
    - control : 타일 레이어를 지도의 컨트롤에 표시할지 여부 설정
- `.add_to(m)` : 지도 객체에 추가하는 메소드


### 5-3. 마커 및 직선 삽입

```python
for idx, row in df.iterrows():
    folium.Marker(location = [row['Lat'],row['Lon']], tooltip=row['Name'], icon=folium.Icon(color='gray')).add_to(m)
    folium.PolyLine(locations = [center, [row['Lat'],row['Lon']]], tooltip=row['to_홍대']).add_to(m)   
folium.Marker(location = center, tooltip='홍대입구역', icon=folium.Icon(color='red')).add_to(m)
```

- `df.iterrows()` : 데이터프레임의 각 행을 이터레이터 객체로 변환
- `folium.Marker()` : 지도 객체에 마커를 추가하는 함수
    - location : 마커를 추가할 좌표 지정
    - tooltip : 마커 위에 마우스를 올렸을 때 출력할 값 지정
    - icon : 마커 아이콘 설정 → `folium.Icon()` 함수를 통해 마커의 스타일 설정
- `folium.PolyLine()` : 지도 객체에 직선을 추가하는 함수
    - locations : 직선의 양 끝 좌표 지정
    - tooltip : 직선 위에 마우스를 올렸을 때 출력할 값 지정


### 5-4. 경계선 맞추기

```python
m.fit_bounds(m.get_bounds())
```

- `m.get_bounds()` : 지도 객체에 포함된 모든 마커와 경로들의 경계를 계산하여 반환
- `m.fit_bounds()` : 인자로 받은 경계값에 맞게 지도 객체의 위치를 조정
    
    → 지도가 현재 표시되는 모든 데이터가 보일 수 있도록 자동으로 지도의 중심과 확대/축소 레벨을 조정하는 코드
    

### 5-5. 지도 저장 및 출력

```python
m.save('map.html')
st.components.v1.html(open("map.html", "rb").read(), height=600)
```

- 지도 객체를 HTML 파일로 저장한 다음, 해당 파일을 바이트 형태로 불러온 후 화면에 출력하는 코드


# Reference

- Streamlit Documentation : [https://docs.streamlit.io/](https://docs.streamlit.io/)
- OpenAPI 발급 방법 : [https://blog.naver.com/v-world/222009887650](https://blog.naver.com/v-world/222009887650)
- 웹앱 배포 방법 : [https://dschloe.github.io/python/2022/11/streamlit_deploy/](https://dschloe.github.io/python/2022/11/streamlit_deploy/)


# 전체 코드

```python
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import folium
import vworld_key

def main():
    
    # 페이지 설정
    st.set_page_config(page_title='Where to meet', layout="wide")
    
    # 사이드바
    st.sidebar.image(Image.open('streamlit_logo.png'))
    st.sidebar.write("---")
    
    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
    color = ['black', 'black', 'black', 'white', 'white', 'white', 'white']
    text = 'WELCOME'
    for r, c, t in zip(rainbow, color, text):
        st.sidebar.markdown(f"<h3 style='color:{c}; background-color:{r}'>__{t}:</h3>", unsafe_allow_html=True)
    st.sidebar.write("---")
    st.sidebar.text("This is Jiwon!\nNice to meet you!")
    
    # 메인 화면
    st.header("A Letter From Peter")
    st.subheader(':blue["Let me know where we will meet on Satuerday, with the dashboard made by streamlit."]')
    st.write("---")

    # 레이아웃(2분할)
    col1, col2 = st.columns([1,2])
    with col1:
        st.image(Image.open('question.jpg'))
        
    with col2:
        st.subheader(':blue["What about 홍대입구?"]')
        center = [37.5575,126.9245] # 홍대입구역 좌표
        
        # 데이터 불러오기
		    df = pd.read_csv("place.csv", encoding='utf-8')
        df['to_홍대'] = np.round(np.sqrt(np.power((df['Lat']-center[0]),2) + np.power((df['Lon']-center[1]),2)),2)
        
        # 탭 만들기
        tab1, tab2 = st.tabs(['On Map', 'Raw Data'])

        with tab2:
            st.write(df)
            
        with tab1:
            # 지도 객체 만들기
            m = folium.Map(location=center, zoom_start=11)
            
            # 배경 레이어 삽입 (*vworld API)
            tiles = f"http://api.vworld.kr/req/wmts/1.0.0/{vworld_key.key}/Base/{{z}}/{{y}}/{{x}}.png"
            folium.TileLayer(
                tiles=tiles,
                attr="Vworld",
                overlay=True,
                control=True
            ).add_to(m)
            
            # 마커 및 직선 삽입
            for idx, row in df.iterrows():
                folium.Marker(location = [row['Lat'],row['Lon']], tooltip=row['Name'], icon=folium.Icon(color='gray')).add_to(m)
                folium.PolyLine(locations = [center, [row['Lat'],row['Lon']]], tooltip=row['to_홍대']).add_to(m)   
            folium.Marker(location = center, tooltip='홍대입구역', icon=folium.Icon(color='red')).add_to(m)
            
            # 경계선 맞추기
            m.fit_bounds(m.get_bounds())
            
            # 지도 저장 및 화면 출력
            m.save('map.html')
            st.components.v1.html(open("map.html", "rb").read(), height=600)
            
    st.write("---")
    
if __name__ == '__main__':
    
    main()
```