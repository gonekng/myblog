---
title: "ML Practice 7_2"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-04_04 11:30:05
---

# DNN(Deep Neural Network)

## Prepare Dataset


```python
from tensorflow import keras

(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
```

    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz
    32768/29515 [=================================] - 0s 0us/step
    40960/29515 [=========================================] - 0s 0us/step
    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz
    26427392/26421880 [==============================] - 0s 0us/step
    26435584/26421880 [==============================] - 0s 0us/step
    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz
    16384/5148 [===============================================================================================] - 0s 0us/step
    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz
    4423680/4422102 [==============================] - 0s 0us/step
    4431872/4422102 [==============================] - 0s 0us/step
    


```python
from sklearn.model_selection import train_test_split

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)
```

## Create Layers


```python
# hidden layer
dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(784,))

# ouput layer
dense2 = keras.layers.Dense(10, activation='softmax')
```


```python
model = keras.Sequential([dense1, dense2])
model.summary()
```

    Model: "sequential"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     dense (Dense)               (None, 100)               78500     
                                                                     
     dense_1 (Dense)             (None, 10)                1010      
                                                                     
    =================================================================
    Total params: 79,510
    Trainable params: 79,510
    Non-trainable params: 0
    _________________________________________________________________
    

# Another way to add layers


```python
model = keras.Sequential([
    keras.layers.Dense(12, activation='sigmoid', input_shape=(16,), name='hidden'),
    keras.layers.Dense(10, activation='softmax', name='hidden_2'),
    keras.layers.Dense(1, activation='softmax', name='output')
], name='fashion MNIST')
model.summary()
```

    Model: "fashion MNIST"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     hidden (Dense)              (None, 12)                204       
                                                                     
     hidden_2 (Dense)            (None, 10)                130       
                                                                     
     output (Dense)              (None, 1)                 11        
                                                                     
    =================================================================
    Total params: 345
    Trainable params: 345
    Non-trainable params: 0
    _________________________________________________________________
    


```python
model = keras.Sequential()
model.add(keras.layers.Dense(100, activation='sigmoid', input_shape=(784,)))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()
```

    Model: "sequential_1"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     dense_2 (Dense)             (None, 100)               78500     
                                                                     
     dense_3 (Dense)             (None, 10)                1010      
                                                                     
    =================================================================
    Total params: 79,510
    Trainable params: 79,510
    Non-trainable params: 0
    _________________________________________________________________
    


```python
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.5636 - accuracy: 0.8073
    Epoch 2/5
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.4066 - accuracy: 0.8546
    Epoch 3/5
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3724 - accuracy: 0.8659
    Epoch 4/5
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3493 - accuracy: 0.8749
    Epoch 5/5
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3327 - accuracy: 0.8782
    




    <keras.callbacks.History at 0x7f2e335dc6d0>




```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(300, activation='relu'))
model.add(keras.layers.Dense(100, activation='sigmoid'))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()
```

    Model: "sequential_2"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     flatten (Flatten)           (None, 784)               0         
                                                                     
     dense_4 (Dense)             (None, 300)               235500    
                                                                     
     dense_5 (Dense)             (None, 100)               30100     
                                                                     
     dense_6 (Dense)             (None, 10)                1010      
                                                                     
    =================================================================
    Total params: 266,610
    Trainable params: 266,610
    Non-trainable params: 0
    _________________________________________________________________
    


