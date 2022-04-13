---
title: "ML Practice Tree plot Example"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-03-31 12:40:40
---


# Goal : To change the color of tree plot


```python
!pip install -U matplotlib
```

    Requirement already satisfied: matplotlib in c:\programdata\anaconda3\lib\site-packages (3.4.3)
    Collecting matplotlib
      Downloading matplotlib-3.5.1-cp39-cp39-win_amd64.whl (7.2 MB)
    Requirement already satisfied: kiwisolver>=1.0.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (1.3.1)
    Requirement already satisfied: numpy>=1.17 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (1.20.3)
    Requirement already satisfied: pillow>=6.2.0 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (8.4.0)
    Requirement already satisfied: cycler>=0.10 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (0.10.0)
    Requirement already satisfied: fonttools>=4.22.0 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (4.25.0)
    Requirement already satisfied: pyparsing>=2.2.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (3.0.4)
    Requirement already satisfied: python-dateutil>=2.7 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (2.8.2)
    Requirement already satisfied: packaging>=20.0 in c:\programdata\anaconda3\lib\site-packages (from matplotlib) (21.0)
    Requirement already satisfied: six in c:\programdata\anaconda3\lib\site-packages (from cycler>=0.10->matplotlib) (1.16.0)
    Installing collected packages: matplotlib
      Attempting uninstall: matplotlib
        Found existing installation: matplotlib 3.4.3
        Uninstalling matplotlib-3.4.3:
    

    ERROR: Could not install packages due to an OSError: [WinError 5] 액세스가 거부되었습니다: 'c:\\programdata\\anaconda3\\lib\\site-packages\\__pycache__\\pylab.cpython-39.pyc'
    Consider using the `--user` option or check the permissions.
    
    

# Stackflow Ex.


```python
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap, to_rgb
import numpy as np
from sklearn import tree

X = np.random.rand(50, 2) * np.r_[100, 50]
y = X[:, 0] - X[:, 1] > 20

clf = tree.DecisionTreeClassifier(random_state=2021)
clf = clf.fit(X, y)

fig, ax = plt.subplots(figsize=(15, 10))

colors = ['crimson', 'dodgerblue']

artists = tree.plot_tree(clf, feature_names=["X", "y"], class_names=colors,
                         filled=True, rounded=True)
for artist, impurity, value in zip(artists, clf.tree_.impurity, clf.tree_.value):
    # let the max value decide the color; whiten the color depending on impurity (gini)
    r, g, b = to_rgb(colors[np.argmax(value)])
    f = impurity * 2 # for N colors: f = impurity * N/(N-1) if N>1 else 0
    artist.get_bbox_patch().set_facecolor((f + (1-f)*r, f + (1-f)*g, f + (1-f)*b))
    artist.get_bbox_patch().set_edgecolor('black')

plt.tight_layout()
plt.show()
```


    
![](/images/Python/ML/plot_tree_ex_1.png)
    


# Iris Ex.

## Tree plot


```python
%matplotlib inline 

import sklearn
print(sklearn.__version__)
import matplotlib
print(matplotlib.__version__)

from sklearn.datasets import load_iris
from sklearn import tree 
import matplotlib.pyplot as plt

iris = load_iris()
print(iris.data.shape, iris.target.shape)
print("feature names", iris.feature_names)
print("class names", iris.target_names)

dt = tree.DecisionTreeClassifier(random_state=0)
dt.fit(iris.data, iris.target)

fig, ax = plt.subplots(figsize=(18, 10))
ax = tree.plot_tree(dt, max_depth = 2, filled=True,
                    feature_names = iris.feature_names, class_names = iris.target_names)
plt.show()
```

    0.24.2
    3.4.3
    (150, 4) (150,)
    feature names ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    class names ['setosa' 'versicolor' 'virginica']
    


    
![](/images/Python/ML/plot_tree_ex_2.png)
    


## matplotlib.text.Annotation


```python
%matplotlib inline
fig, ax = plt.subplots(figsize=(15, 10))
ax = tree.plot_tree(dt, max_depth = 2, 
                    filled=True, 
                    feature_names = iris.feature_names, 
                    class_names = iris.target_names)

for i in range(0, len(ax)):
  print(type(ax[i]))
```

    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    <class 'matplotlib.text.Annotation'>
    


    
![](/images/Python/ML/plot_tree_ex_3.png)
    


- get_bbox_patch() method


```python
%matplotlib inline
fig, ax = plt.subplots(figsize=(15, 10))
ax = tree.plot_tree(dt, max_depth = 2, 
                    filled=True, 
                    feature_names = iris.feature_names, 
                    class_names = iris.target_names)

for i in range(0, len(ax)):
  print(ax[i].get_bbox_patch()) # get patch properties (facecolor, edgewidth,,,)
```

    FancyBboxPatch((0, 0), width=120.875, height=56.4)
    FancyBboxPatch((0, 0), width=87.875, height=44.8)
    FancyBboxPatch((0, 0), width=127.25, height=56.4)
    FancyBboxPatch((0, 0), width=131.625, height=56.4)
    FancyBboxPatch((0, 0), width=30, height=33.2)
    FancyBboxPatch((0, 0), width=30, height=33.2)
    FancyBboxPatch((0, 0), width=131.625, height=56.4)
    FancyBboxPatch((0, 0), width=30, height=33.2)
    FancyBboxPatch((0, 0), width=30, height=33.2)
    


    
![](/images/Python/ML/plot_tree_ex_4.png)
    


- set_boxstyle()


```python
%matplotlib inline
fig, ax = plt.subplots(figsize=(15, 10))
ax = tree.plot_tree(dt, max_depth = 2, 
                    filled=True, 
                    feature_names = iris.feature_names, 
                    class_names = iris.target_names)

for i in range(0, len(ax)):
  # set patch properties
  if i % 2 == 0:
    ax[i].get_bbox_patch().set_boxstyle("Rarrow", pad=0.3)
  else:
    ax[i].get_bbox_patch().set_boxstyle("Round", pad=0.3)
```


    
![](/images/Python/ML/plot_tree_ex_5.png)
    


# Final ex.


```python
import numpy as np 

colors = ["indigo", "violet", "crimson"]
print(colors[np.argmax([[0., 0., 50.]])])
print(colors[np.argmax([[50., 0., 0.]])])
print(colors[np.argmax([[0., 50., 0.]])])
print(colors[np.argmax([[50., 50., 50.]])])
```

    crimson
    indigo
    violet
    indigo
    


```python
from matplotlib.colors import to_rgb
%matplotlib inline
fig, ax = plt.subplots(figsize=(15, 10))
ax = tree.plot_tree(dt, max_depth = 3, 
                    filled=True, 
                    feature_names = iris.feature_names, 
                    class_names = iris.target_names)

i = 0
colors = ["yellow", "violet", "lavenderblush"]
for artist, impurity, value in zip(ax, dt.tree_.impurity, dt.tree_.value):
  r, g, b = to_rgb(colors[np.argmax(value)])
  # 코드가 길어서 i로 재 저장
  ip = impurity
  # print(ip + (1-ip)*r, ip + (1-ip)*g, ip + (1-ip)*b)
  if i % 2 == 0:
    # set_boxtyle 적용
    ax[i].get_bbox_patch().set_boxstyle("round", pad=0.3)
    ax[i].get_bbox_patch().set_facecolor((ip + (1-ip)*r, ip + (1-ip)*g, ip + (1-ip)*b))
    ax[i].get_bbox_patch().set_edgecolor('black')  
  else:
    ax[i].get_bbox_patch().set_boxstyle("circle", pad=0.3)
    ax[i].get_bbox_patch().set_facecolor((ip + (1-ip)*r, ip + (1-ip)*g, ip + (1-ip)*b))
    ax[i].get_bbox_patch().set_edgecolor('black')   
  i = i+1
```


    
![](/images/Python/ML/plot_tree_ex_6.png)
    


*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*