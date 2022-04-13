---
title: "ML Practice 8_1"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-04-06 11:26:18
---
  
# CNN(Convolution Neural Network)
- Neural network operations can also be applied to two-dimensional arrays by CNN.
- Neuron in CNN is called filter or kernel.


```python
from tensorflow import keras
keras.layers.Conv2D(10, kernel_size=(3,3), activation="relu")
```




    <keras.layers.convolutional.Conv2D at 0x7effd27dea10>



## Padding & Stride
### Padding : Filling the border of the input array with virtual elements
  - To prevent the loss of the original features of the image even if you resize the array,
  - Same padding : Padding to zero around the input to make the input and feature map the same size
  - Valid padding : Convolution only in a pure input array without padding

### Stride : Size of the filter moving over the input layer (default 1)


```python
keras.layers.Conv2D(10, kernel_size=(3,3), activation='relu', padding='same', strides=1)
```




    <keras.layers.convolutional.Conv2D at 0x7effceb4fb10>



## Pooling
- Reducing the size of the feature map while maintaining the original features of the image
- Max pooling, Average pooling, etc


```python
keras.layers.MaxPooling2D(2, strides=2, padding="valid")
```




    <keras.layers.pooling.MaxPooling2D at 0x7effce850fd0>




```python
keras.layers.AveragePooling2D(2, strides=2, padding="valid")
```




    <keras.layers.pooling.AveragePooling2D at 0x7effcea305d0>



# Overall process in CNN
1. Input Image Data
2. CNN Layer
  - kernel_size, padding, stride
  - activation function
  - Calculate each feature map
3. Pooling Layer
  - Maxpooling / Averagepooling
  - final feature map
4. Repeat the above process
5. Fully Connected Layer
6. Calculate classification predictions (Softmax)

*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*