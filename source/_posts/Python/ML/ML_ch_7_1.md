---
title: "ML Practice 7_1"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-04-04 10:25:10
---

# Fashion MNIST




# Deep Learning Library
- tensorflow : https://www.tensorflow.org/
- pytorch : https://pytorch.org/


```python
import tensorflow
print(tensorflow.__version__)
```

    2.8.0
    

# Load Data


```python
from tensorflow import keras
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
```

- 60,000 images, which is 28 * 28 size


```python
print(train_input.shape, train_target.shape)
print(test_input.shape, test_target.shape)
```

    (60000, 28, 28) (60000,)
    (10000, 28, 28) (10000,)
    

- image visualization


```python
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 10, figsize=(10, 10))
for i in range(10):
  axs[i].imshow(train_input[i], cmap="gray_r")
  axs[i].axis('off')
plt.show()
```


    
![](/images/Python/ML/ML_ch_7_1.png)
    


- list of target values


```python
print([train_target[i] for i in range(10)])
```

    [9, 0, 0, 3, 0, 2, 7, 2, 5, 5]
    

- real target values
- 6,000 images per label.


```python
import numpy as np
print(np.unique(train_target, return_counts=True))
```

    (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8), array([6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000]))
    

# Classify by Logistic Regression


```python
train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)
print(train_scaled.shape)
```

    (60000, 784)
    


```python
from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log', max_iter=10, random_state=42)

scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score'])) # 0.82
```

    0.8243124999999999
    

- Is it reasonable to apply a linear or nonlinear model to unstructured data? : **No**
  + One alternative is artificial neural networks.
- Is it reasonable to apply artificial neural networks and deep learning models to structured data? : **No**

# Classify by Artificial Neural Network


```python
from sklearn.model_selection import train_test_split

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)
```


```python
print(train_scaled.shape, train_target.shape)
print(val_scaled.shape, val_target.shape)
```

    (48000, 784) (48000,)
    (12000, 784) (12000,)
    

- A dense connection is called a fully connected layer.
- Specify activation functions to be applied to neuronal output
  + binary classification : Sigmoid function
  + multi classification : Softmax function
- specifying the type of loss function
  + binary classification : binary_crossentropy
  + multi classification : catogorical_crossentropy
- The integer target value should be one-hot encoded as 0, 1, 2, etc.<br/>but it can distort the operation of the artificial neural network.
  + In tensorflow,<br/> by using sparse_categorical_crossentropy as a loss function,<br/> an integer target value can be used as it is.


```python
dense = keras.layers.Dense(10, activation = "softmax", input_shape=(784, ))
model = keras.Sequential(dense)
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
```


```python
print(train_target[:10])
```

    [7 3 5 8 6 9 3 3 9 9]
    


```python
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.6125 - accuracy: 0.7900
    Epoch 2/5
    1500/1500 [==============================] - 2s 2ms/step - loss: 0.4797 - accuracy: 0.8402
    Epoch 3/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4562 - accuracy: 0.8479
    Epoch 4/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4457 - accuracy: 0.8524
    Epoch 5/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4365 - accuracy: 0.8549
    




    <keras.callbacks.History at 0x7efd2ea9ded0>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 1ms/step - loss: 0.4553 - accuracy: 0.8475
    




    [0.45534512400627136, 0.8475000262260437]



*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*