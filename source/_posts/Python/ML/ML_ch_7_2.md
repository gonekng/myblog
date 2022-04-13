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
date: 2022-04-05 10:20:01
---

# Prepare Dataset


```python
from tensorflow import keras

(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
```


```python
from sklearn.model_selection import train_test_split

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)
```

# DNN Layer


```python
# hidden layer 
dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(784,))

# output layer 
dense2 = keras.layers.Dense(10, activation='softmax')
```


```python
model = keras.Sequential([dense1, dense2])
model.summary()
```

    Model: "sequential_3"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     dense_9 (Dense)             (None, 100)               78500     
                                                                     
     dense_10 (Dense)            (None, 10)                1010      
                                                                     
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

    Model: "sequential_4"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     dense_11 (Dense)            (None, 100)               78500     
                                                                     
     dense_12 (Dense)            (None, 10)                1010      
                                                                     
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
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.5627 - accuracy: 0.8077
    Epoch 2/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.4080 - accuracy: 0.8529
    Epoch 3/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.3740 - accuracy: 0.8660
    Epoch 4/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.3508 - accuracy: 0.8720
    Epoch 5/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3345 - accuracy: 0.8810
    




    <keras.callbacks.History at 0x7fcf5e9c8810>



# Relu function


```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()
```

    Model: "sequential_6"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     flatten_2 (Flatten)         (None, 784)               0         
                                                                     
     dense_16 (Dense)            (None, 100)               78500     
                                                                     
     dense_17 (Dense)            (None, 10)                1010      
                                                                     
    =================================================================
    Total params: 79,510
    Trainable params: 79,510
    Non-trainable params: 0
    _________________________________________________________________
    


```python
model.summary()
```

    Model: "sequential_6"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     flatten_2 (Flatten)         (None, 784)               0         
                                                                     
     dense_16 (Dense)            (None, 100)               78500     
                                                                     
     dense_17 (Dense)            (None, 10)                1010      
                                                                     
    =================================================================
    Total params: 79,510
    Trainable params: 79,510
    Non-trainable params: 0
    _________________________________________________________________
    


```python
(train_input, train_target), (test_input, test_target) =\
      keras.datasets.fashion_mnist.load_data()
train_scaled = train_input / 255.0
train_scaled, val_scaled, train_target, val_traget = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42
)
```


```python
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.5362 - accuracy: 0.8096
    Epoch 2/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.3953 - accuracy: 0.8578
    Epoch 3/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3570 - accuracy: 0.8722
    Epoch 4/5
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3360 - accuracy: 0.8808
    Epoch 5/5
    1500/1500 [==============================] - 6s 4ms/step - loss: 0.3200 - accuracy: 0.8871
    




    <keras.callbacks.History at 0x7fcf5e813250>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.3565 - accuracy: 0.8775
    




    [0.35651248693466187, 0.8774999976158142]



# Optimizer
- a variety of gradient descent algorithms provided by Keras
- Optimizer have to consider both step direction and width
  + direction : GD, SGD, Momentum, NAG
  + width : GD, SGD, Adagrad, RMSProp
  + direction & width : Adam (generally, the best performance)

## SGD

#### Learning rate: default 0.01


```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
```


```python
model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy',
              metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.8096 - accuracy: 0.7362
    Epoch 2/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.5421 - accuracy: 0.8163
    Epoch 3/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4886 - accuracy: 0.8329
    Epoch 4/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4604 - accuracy: 0.8426
    Epoch 5/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4404 - accuracy: 0.8490
    




    <keras.callbacks.History at 0x7fcf5e524250>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 1ms/step - loss: 0.4474 - accuracy: 0.8464
    




    [0.44738978147506714, 0.8464166522026062]



#### Learning rate: 0.1


```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
```


```python
sgd = keras.optimizers.SGD(learning_rate=0.1)
model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy',
              metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.5663 - accuracy: 0.7985
    Epoch 2/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4148 - accuracy: 0.8493
    Epoch 3/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3765 - accuracy: 0.8620
    Epoch 4/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3503 - accuracy: 0.8707
    Epoch 5/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3315 - accuracy: 0.8777
    




    <keras.callbacks.History at 0x7fcf5e614e90>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.3469 - accuracy: 0.8744
    




    [0.3468727171421051, 0.8744166493415833]



#### Nesterov momentum


```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
```


```python
sgd = keras.optimizers.SGD(momentum=0.9, nesterov=True)
model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy',
              metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.5365 - accuracy: 0.8099
    Epoch 2/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.4051 - accuracy: 0.8562
    Epoch 3/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3659 - accuracy: 0.8690
    Epoch 4/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3448 - accuracy: 0.8737
    Epoch 5/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3255 - accuracy: 0.8802
    




    <keras.callbacks.History at 0x7fcf5e1de1d0>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.3611 - accuracy: 0.8718
    




    [0.36112430691719055, 0.871833324432373]



## Adagrad


```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
```


```python
adagrad = keras.optimizers.Adagrad()
model.compile(optimizer=adagrad, loss='sparse_categorical_crossentropy',
              metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 1.1751 - accuracy: 0.6441
    Epoch 2/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.7733 - accuracy: 0.7556
    Epoch 3/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.6848 - accuracy: 0.7837
    Epoch 4/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.6372 - accuracy: 0.7972
    Epoch 5/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.6071 - accuracy: 0.8053
    




    <keras.callbacks.History at 0x7fcf5e480390>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 1ms/step - loss: 0.6081 - accuracy: 0.8025
    




    [0.6081421375274658, 0.8025000095367432]



## RMSprop


```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
```


```python
rmsprop = keras.optimizers.RMSprop()
model.compile(optimizer=rmsprop, loss='sparse_categorical_crossentropy',
              metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.5261 - accuracy: 0.8139
    Epoch 2/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3931 - accuracy: 0.8598
    Epoch 3/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.3556 - accuracy: 0.8733
    Epoch 4/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3349 - accuracy: 0.8806
    Epoch 5/5
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3173 - accuracy: 0.8869
    




    <keras.callbacks.History at 0x7fcf5e374710>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.3817 - accuracy: 0.8742
    




    [0.3816753029823303, 0.8741666674613953]



## Adam


```python
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
```


```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)
```

    Epoch 1/5
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.5273 - accuracy: 0.8153
    Epoch 2/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3943 - accuracy: 0.8584
    Epoch 3/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3522 - accuracy: 0.8727
    Epoch 4/5
    1500/1500 [==============================] - 3s 2ms/step - loss: 0.3264 - accuracy: 0.8815
    Epoch 5/5
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3074 - accuracy: 0.8882
    




    <keras.callbacks.History at 0x7fcf5e47b050>




```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.3356 - accuracy: 0.8788
    




    [0.33555400371551514, 0.8788333535194397]



*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*