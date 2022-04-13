---
title: "ML Practice 6_1"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-03-31 17:03:00
---

# Unsupervised Learning
- No dependent variables and targets. (↔ Supervised Learning)
- Clustering (Multiple class)
  + Must be many different types of data
  + Linked to deep learning
- Dimensionality reduction

# Import Numpy Data


```python
!wget https://bit.ly/fruits_300_data -O fruits_300.npy
```

    --2022-03-31 01:12:51--  https://bit.ly/fruits_300_data
    Resolving bit.ly (bit.ly)... 67.199.248.11, 67.199.248.10
    Connecting to bit.ly (bit.ly)|67.199.248.11|:443... connected.
    HTTP request sent, awaiting response... 301 Moved Permanently
    Location: https://github.com/rickiepark/hg-mldl/raw/master/fruits_300.npy [following]
    --2022-03-31 01:12:51--  https://github.com/rickiepark/hg-mldl/raw/master/fruits_300.npy
    Resolving github.com (github.com)... 140.82.113.4
    Connecting to github.com (github.com)|140.82.113.4|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fruits_300.npy [following]
    --2022-03-31 01:12:51--  https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fruits_300.npy
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.109.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 3000128 (2.9M) [application/octet-stream]
    Saving to: ‘fruits_300.npy’
    
    fruits_300.npy      100%[===================>]   2.86M  --.-KB/s    in 0.02s   
    
    2022-03-31 01:12:51 (157 MB/s) - ‘fruits_300.npy’ saved [3000128/3000128]
    
    


```python
import numpy as np

# 100 apples, 100 pineapples, 100 bananas
fruits = np.load('fruits_300.npy')
print(fruits.shape)
```

    (300, 100, 100)
    

- image samples of three dimensions
  + dimension 1: the number of samples
  + dimension 2: the height of image
  + dimension 3: the width of image
- 300 pieces of image sample of 100 x 100 size.

# Visualize Image Data
- black-and-white photographs
- integer value from 0 to 255


```python
import matplotlib.pyplot as plt

plt.imshow(fruits[0], cmap='gray') # 0: black, 255: white
plt.show()
```


    
![](/images/Python/ML/ML_ch_6_1_.png)
    



```python
plt.imshow(fruits[0], cmap='gray_r') # 0: white, 255: black
plt.show()
```


    
![](/images/Python/ML/ML_ch_6_1_2.png)
    


- multiple images


```python
fig, ax = plt.subplots(1,2)
ax[0].imshow(fruits[100], cmap='gray_r')
ax[1].imshow(fruits[200], cmap='gray_r')
plt.show()
```


    
![](/images/Python/ML/ML_ch_6_1_3.png)
    


# Pixel value analysis


```python
# convert 100*100 images to one-dimensional array with a length of 10000
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)
print(apple.shape, pineapple.shape, banana.shape)
```

    (100, 10000) (100, 10000) (100, 10000)
    

- average comparison of pixel values for each image


```python
plt.hist(np.mean(apple, axis=1), alpha=0.8)
plt.hist(np.mean(pineapple, axis=1), alpha=0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)
plt.legend(['apple','pineapple','banana'])
plt.show()
```


    
![](/images/Python/ML/ML_ch_6_1_4.png)
    



```python
fig, ax = plt.subplots(1,3,figsize=(15,5))
ax[0].bar(range(10000),np.mean(apple, axis=0))
ax[1].bar(range(10000),np.mean(pineapple, axis=0))
ax[2].bar(range(10000),np.mean(banana, axis=0))
plt.show()
```


    
![](/images/Python/ML/ML_ch_6_1_5.png)
    


- representative image using pixel mean


```python
apple_mean = np.mean(apple, axis=0).reshape(100,100)
pineapple_mean = np.mean(pineapple, axis=0).reshape(100,100)
banana_mean = np.mean(banana, axis=0).reshape(100,100)

fig, ax = plt.subplots(1,3,figsize=(15,5))
ax[0].imshow(apple_mean, cmap='gray_r')
ax[1].imshow(pineapple_mean, cmap='gray_r')
ax[2].imshow(banana_mean, cmap='gray_r')
plt.show()
```


    
![](/images/Python/ML/ML_ch_6_1_6.png)
    


- 100 images close to the average value


```python
# MAE(Mean Absolute Error)
abs_diff = np.abs(fruits - apple_mean)
abs_mean = np.mean(abs_diff, axis=(1,2))
print(abs_mean.shape) # one-dimensions array
```

    (300,)
    


```python
apple_index = np.argsort(abs_mean)[:100] # extract 100 indexes in the smallest order of MAE
fig, ax = plt.subplots(10,10,figsize=(10,10))
for i in range(10):
  for j in range(10):
    ax[i,j].imshow(fruits[apple_index[i*10+j]], cmap='gray_r')
    ax[i,j].axis('off') # remove axis
plt.show()
```

    33 48 70 57 87 12 78 59 1 74 
    86 38 50 92 69 27 68 30 66 24 
    76 98 15 84 47 90 3 94 53 23 
    14 71 32 7 73 36 55 77 21 10 
    17 39 99 95 11 35 65 6 61 22 
    56 89 2 13 80 0 97 4 58 34 
    40 43 75 82 54 16 31 49 93 37 
    63 64 41 28 67 25 96 8 83 46 
    19 79 72 5 85 29 20 60 81 9 
    45 51 88 62 91 26 52 18 44 42 
    


    
![](/images/Python/ML/ML_ch_6_1_7.png)
    


*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*