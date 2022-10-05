---
title: "ML Practice 7_3"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-04-05 12:14:17
---
  
# Create DNN Model


```python
from tensorflow import keras
from sklearn.model_selection import train_test_split

(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)
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
    

-  Define function of create model


```python
def model_fn(a_layer=None):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28,28)))
    model.add(keras.layers.Dense(100, activation='relu'))
    if a_layer:
      model.add(a_layer)
    model.add(keras.layers.Dense(10, activation='softmax'))
    return model
  
model = model_fn()
model.summary
```




    <bound method Model.summary of <keras.engine.sequential.Sequential object at 0x7f9181716750>>



# Loss Curve


```python
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs = 5, verbose = 0)
```

- verbose default 1: print the indicator along with the progress bar per epoch.
- verbose 2: print the indicator without the progress bar per epoch.
- verbose 0: print none


```python
print(history) # class
print(history.history) # dictionary
print(history.history.keys())
```

    <keras.callbacks.History object at 0x7f917bab27d0>
    {'loss': [0.5360119342803955, 0.3935061991214752, 0.3552784025669098, 0.33411645889282227, 0.31946054100990295], 'accuracy': [0.8113541603088379, 0.8598541617393494, 0.8732083439826965, 0.8820000290870667, 0.8862708210945129]}
    dict_keys(['loss', 'accuracy'])
    

- loss curve (epoch 5)


```python
import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
```


    
![](/images/Python/ML/ML_ch_7_3_1.png)
    


- accuracy curve (epoch 5)


```python
plt.plot(history.history['accuracy'])
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()
```


    
![](/images/Python/ML/ML_ch_7_3_2.png)
    


- loss curve (epoch 20)


```python
model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')

history = model.fit(train_scaled, train_target, epochs=20, verbose=0)
plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
```


    
![](/images/Python/ML/ML_ch_7_3_3.png)
    


# Validation Loss


```python
model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')

history = model.fit(train_scaled, train_target, epochs=20, verbose=1, 
                    validation_data=(val_scaled, val_target))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()
```

    Epoch 1/20
    1500/1500 [==============================] - 6s 4ms/step - loss: 0.5344 - accuracy: 0.8118 - val_loss: 0.4414 - val_accuracy: 0.8471
    Epoch 2/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3950 - accuracy: 0.8577 - val_loss: 0.3638 - val_accuracy: 0.8668
    Epoch 3/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3573 - accuracy: 0.8702 - val_loss: 0.3754 - val_accuracy: 0.8682
    Epoch 4/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3365 - accuracy: 0.8791 - val_loss: 0.3783 - val_accuracy: 0.8701
    Epoch 5/20
    1500/1500 [==============================] - 5s 4ms/step - loss: 0.3191 - accuracy: 0.8865 - val_loss: 0.3576 - val_accuracy: 0.8772
    Epoch 6/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3085 - accuracy: 0.8898 - val_loss: 0.3556 - val_accuracy: 0.8806
    Epoch 7/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.2982 - accuracy: 0.8948 - val_loss: 0.3736 - val_accuracy: 0.8807
    Epoch 8/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2910 - accuracy: 0.8976 - val_loss: 0.3443 - val_accuracy: 0.8869
    Epoch 9/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2841 - accuracy: 0.8998 - val_loss: 0.3757 - val_accuracy: 0.8832
    Epoch 10/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.2755 - accuracy: 0.9031 - val_loss: 0.4034 - val_accuracy: 0.8766
    Epoch 11/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.2700 - accuracy: 0.9059 - val_loss: 0.4085 - val_accuracy: 0.8792
    Epoch 12/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2655 - accuracy: 0.9075 - val_loss: 0.3936 - val_accuracy: 0.8835
    Epoch 13/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.2589 - accuracy: 0.9105 - val_loss: 0.4122 - val_accuracy: 0.8812
    Epoch 14/20
    1500/1500 [==============================] - 5s 4ms/step - loss: 0.2545 - accuracy: 0.9116 - val_loss: 0.4056 - val_accuracy: 0.8842
    Epoch 15/20
    1500/1500 [==============================] - 6s 4ms/step - loss: 0.2506 - accuracy: 0.9137 - val_loss: 0.4048 - val_accuracy: 0.8815
    Epoch 16/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.2454 - accuracy: 0.9159 - val_loss: 0.4132 - val_accuracy: 0.8808
    Epoch 17/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.2410 - accuracy: 0.9177 - val_loss: 0.4343 - val_accuracy: 0.8831
    Epoch 18/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2356 - accuracy: 0.9190 - val_loss: 0.4574 - val_accuracy: 0.8767
    Epoch 19/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2326 - accuracy: 0.9201 - val_loss: 0.4499 - val_accuracy: 0.8817
    Epoch 20/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.2284 - accuracy: 0.9204 - val_loss: 0.4834 - val_accuracy: 0.8751
    


    
![](/images/Python/ML/ML_ch_7_3_4.png)
    


- There is a large difference in loss between training data and verification data.
- This is a typical overfitting model.


```python
model = model_fn()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')

history = model.fit(train_scaled, train_target, epochs=20, verbose=1, 
                    validation_data=(val_scaled, val_target))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()
```

    Epoch 1/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.5231 - accuracy: 0.8183 - val_loss: 0.4741 - val_accuracy: 0.8357
    Epoch 2/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3940 - accuracy: 0.8576 - val_loss: 0.3736 - val_accuracy: 0.8671
    Epoch 3/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3557 - accuracy: 0.8703 - val_loss: 0.3567 - val_accuracy: 0.8712
    Epoch 4/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3273 - accuracy: 0.8796 - val_loss: 0.3398 - val_accuracy: 0.8790
    Epoch 5/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3091 - accuracy: 0.8872 - val_loss: 0.3324 - val_accuracy: 0.8803
    Epoch 6/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2904 - accuracy: 0.8925 - val_loss: 0.3194 - val_accuracy: 0.8842
    Epoch 7/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2802 - accuracy: 0.8967 - val_loss: 0.3333 - val_accuracy: 0.8796
    Epoch 8/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2679 - accuracy: 0.9010 - val_loss: 0.3265 - val_accuracy: 0.8830
    Epoch 9/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2588 - accuracy: 0.9040 - val_loss: 0.3298 - val_accuracy: 0.8858
    Epoch 10/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2482 - accuracy: 0.9068 - val_loss: 0.3282 - val_accuracy: 0.8840
    Epoch 11/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2413 - accuracy: 0.9094 - val_loss: 0.3098 - val_accuracy: 0.8889
    Epoch 12/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2315 - accuracy: 0.9131 - val_loss: 0.3250 - val_accuracy: 0.8867
    Epoch 13/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2260 - accuracy: 0.9141 - val_loss: 0.3164 - val_accuracy: 0.8911
    Epoch 14/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2181 - accuracy: 0.9185 - val_loss: 0.3511 - val_accuracy: 0.8774
    Epoch 15/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2128 - accuracy: 0.9200 - val_loss: 0.3397 - val_accuracy: 0.8817
    Epoch 16/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2059 - accuracy: 0.9222 - val_loss: 0.3219 - val_accuracy: 0.8903
    Epoch 17/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2021 - accuracy: 0.9240 - val_loss: 0.3423 - val_accuracy: 0.8859
    Epoch 18/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.1952 - accuracy: 0.9277 - val_loss: 0.3313 - val_accuracy: 0.8916
    Epoch 19/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.1918 - accuracy: 0.9272 - val_loss: 0.3396 - val_accuracy: 0.8871
    Epoch 20/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.1879 - accuracy: 0.9295 - val_loss: 0.3354 - val_accuracy: 0.8904
    


    
![](/images/Python/ML/ML_ch_7_3_5.png)
    


- Overfitting has decreased a little, but it is still necessary to improve.

# Dropout
- Basically, it is a principle to calculate all parameters.
- Neurons without some output are excluded from the calculation.


```python
model = model_fn(keras.layers.Dropout(0.3)) # drop out 30%
model.summary()
```

    Model: "sequential_5"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     flatten_5 (Flatten)         (None, 784)               0         
                                                                     
     dense_10 (Dense)            (None, 100)               78500     
                                                                     
     dropout (Dropout)           (None, 100)               0         
                                                                     
     dense_11 (Dense)            (None, 10)                1010      
                                                                     
    =================================================================
    Total params: 79,510
    Trainable params: 79,510
    Non-trainable params: 0
    _________________________________________________________________
    


```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')

history = model.fit(train_scaled, train_target, epochs=20, verbose=1, 
                    validation_data=(val_scaled, val_target))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()
```

    Epoch 1/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.5967 - accuracy: 0.7907 - val_loss: 0.4495 - val_accuracy: 0.8294
    Epoch 2/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.4413 - accuracy: 0.8409 - val_loss: 0.4071 - val_accuracy: 0.8472
    Epoch 3/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.4044 - accuracy: 0.8547 - val_loss: 0.3616 - val_accuracy: 0.8674
    Epoch 4/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3833 - accuracy: 0.8603 - val_loss: 0.3605 - val_accuracy: 0.8651
    Epoch 5/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3688 - accuracy: 0.8646 - val_loss: 0.3423 - val_accuracy: 0.8750
    Epoch 6/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3542 - accuracy: 0.8696 - val_loss: 0.3479 - val_accuracy: 0.8744
    Epoch 7/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.3439 - accuracy: 0.8725 - val_loss: 0.3449 - val_accuracy: 0.8752
    Epoch 8/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3356 - accuracy: 0.8763 - val_loss: 0.3356 - val_accuracy: 0.8802
    Epoch 9/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3280 - accuracy: 0.8796 - val_loss: 0.3361 - val_accuracy: 0.8801
    Epoch 10/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3212 - accuracy: 0.8781 - val_loss: 0.3394 - val_accuracy: 0.8734
    Epoch 11/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3200 - accuracy: 0.8813 - val_loss: 0.3327 - val_accuracy: 0.8763
    Epoch 12/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3115 - accuracy: 0.8852 - val_loss: 0.3325 - val_accuracy: 0.8776
    Epoch 13/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3061 - accuracy: 0.8860 - val_loss: 0.3216 - val_accuracy: 0.8860
    Epoch 14/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3034 - accuracy: 0.8860 - val_loss: 0.3193 - val_accuracy: 0.8864
    Epoch 15/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2961 - accuracy: 0.8880 - val_loss: 0.3198 - val_accuracy: 0.8846
    Epoch 16/20
    1500/1500 [==============================] - 4s 2ms/step - loss: 0.2913 - accuracy: 0.8900 - val_loss: 0.3310 - val_accuracy: 0.8823
    Epoch 17/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2870 - accuracy: 0.8933 - val_loss: 0.3162 - val_accuracy: 0.8848
    Epoch 18/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2838 - accuracy: 0.8931 - val_loss: 0.3321 - val_accuracy: 0.8838
    Epoch 19/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2829 - accuracy: 0.8935 - val_loss: 0.3320 - val_accuracy: 0.8840
    Epoch 20/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2814 - accuracy: 0.8942 - val_loss: 0.3218 - val_accuracy: 0.8882
    


    
![](/images/Python/ML/ML_ch_7_3_6.png)
    


- Overfitting has improved a lot.

# Save and Load Model


```python
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')

history = model.fit(train_scaled, train_target, epochs=10, verbose=0, 
                    validation_data=(val_scaled, val_target))
```

- save_weights() : method of saving the parameters of a model
- save() : method of saving both the parameters and structure of a model
- '.h5' : HDF5 format


```python
model.save_weights('model-weights.h5')
model.save('model-whole.h5')
```


```python
!ls -al *.h5
```

    -rw-r--r-- 1 root root 982664 Apr  5 02:37 best-model.h5
    -rw-r--r-- 1 root root 333448 Apr  5 02:42 model-weights.h5
    -rw-r--r-- 1 root root 982664 Apr  5 02:42 model-whole.h5
    

- load previously saved parameters


```python
model = model_fn(keras.layers.Dropout(0.3))
model.load_weights('model-weights.h5')
```


```python
# Returns the largest value in the predict method result
import numpy as np
val_labels = np.argmax(model.predict(val_scaled), axis=-1)
print(np.mean(val_labels == val_target))
```

    0.8825833333333334
    

- load previously saved model


```python
model = keras.models.load_model('model-whole.h5')
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.3248 - accuracy: 0.8826
    




    [0.3247545063495636, 0.8825833201408386]



# Callback


```python
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', 
              metrics='accuracy')

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', 
                                                save_best_only=True)

model.fit(train_scaled, train_target, epochs=20, verbose=1, 
          validation_data=(val_scaled, val_target),
          callbacks=[checkpoint_cb])
```

    Epoch 1/20
    1500/1500 [==============================] - 5s 3ms/step - loss: 0.5955 - accuracy: 0.7909 - val_loss: 0.4305 - val_accuracy: 0.8437
    Epoch 2/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.4369 - accuracy: 0.8436 - val_loss: 0.3847 - val_accuracy: 0.8572
    Epoch 3/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.4027 - accuracy: 0.8533 - val_loss: 0.3737 - val_accuracy: 0.8633
    Epoch 4/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3833 - accuracy: 0.8607 - val_loss: 0.3648 - val_accuracy: 0.8628
    Epoch 5/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3675 - accuracy: 0.8662 - val_loss: 0.3481 - val_accuracy: 0.8703
    Epoch 6/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3544 - accuracy: 0.8710 - val_loss: 0.3434 - val_accuracy: 0.8758
    Epoch 7/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3435 - accuracy: 0.8736 - val_loss: 0.3388 - val_accuracy: 0.8781
    Epoch 8/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3360 - accuracy: 0.8759 - val_loss: 0.3333 - val_accuracy: 0.8760
    Epoch 9/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3261 - accuracy: 0.8777 - val_loss: 0.3333 - val_accuracy: 0.8755
    Epoch 10/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3203 - accuracy: 0.8808 - val_loss: 0.3319 - val_accuracy: 0.8807
    Epoch 11/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3154 - accuracy: 0.8822 - val_loss: 0.3275 - val_accuracy: 0.8794
    Epoch 12/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3063 - accuracy: 0.8849 - val_loss: 0.3206 - val_accuracy: 0.8842
    Epoch 13/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3024 - accuracy: 0.8871 - val_loss: 0.3239 - val_accuracy: 0.8815
    Epoch 14/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.3002 - accuracy: 0.8882 - val_loss: 0.3249 - val_accuracy: 0.8838
    Epoch 15/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2928 - accuracy: 0.8911 - val_loss: 0.3237 - val_accuracy: 0.8827
    Epoch 16/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2891 - accuracy: 0.8911 - val_loss: 0.3216 - val_accuracy: 0.8839
    Epoch 17/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2854 - accuracy: 0.8918 - val_loss: 0.3301 - val_accuracy: 0.8844
    Epoch 18/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2834 - accuracy: 0.8942 - val_loss: 0.3315 - val_accuracy: 0.8833
    Epoch 19/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2776 - accuracy: 0.8959 - val_loss: 0.3381 - val_accuracy: 0.8790
    Epoch 20/20
    1500/1500 [==============================] - 4s 3ms/step - loss: 0.2758 - accuracy: 0.8965 - val_loss: 0.3273 - val_accuracy: 0.8830
    




    <keras.callbacks.History at 0x7f916df86590>




```python
model = keras.models.load_model('best-model.h5')
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.3206 - accuracy: 0.8842
    




    [0.32058343291282654, 0.8842499852180481]



- early stopping : to stop training before overfitting begins


```python
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', 
              metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', 
                                                save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                                  restore_best_weights=True)
history = model.fit(train_scaled, train_target, epochs=20, verbose=0, 
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])
```


```python
print(early_stopping_cb.stopped_epoch)
```

    5
    


```python
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()
```


    
![](/images/Python/ML/ML_ch_7_3_7.png)
    


- It stopped early in 5 epoch, and the issue of overfitting was solved.

*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*