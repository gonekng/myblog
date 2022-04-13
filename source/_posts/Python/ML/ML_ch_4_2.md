---
title: "ML Practice 4_2"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-03-29 16:10:25
---


# Gradient Descent(경사 하강법)
#### : Algorithm for finding the minimum value of a loss function using a sample of a training set
1. stochastic gradient descent(확률적 경사 하강법; SGD)
   - method of randomly selecting **one** sample from a training set
2. minibatch gradient descent(미니배치 경사 하강법)
   - method of randomly selecting **several** samples from a training set
3. batch gradient descent(배치 경사 하강법)
   - method of selecting **all** the samples from a training set at once


- Sampling method is different from the existing model. (more detailed approach)
- It aims to correct errors by reducing the slope of the loss function
- SGDClassifier : Create a classification model using SGD.
- SGDRegressor : Create a regression model using SGD.
- Epoch : process of using the entire training set once


#### Usage
- Deep learning algorithm (especially, image and text)
- Tree algorithm + Gradient Descent = Boosting
  + ex) LightGBM, Xgboost, Catboost

## Loss function(손실 함수)
- Cost function 비용 함수)
- Loss is the difference between the predicted value and the actual value of the model (equivalent to error)
- Loss function is a function that expresses loss of the model
  + an indicator of how poorly a model processes data
- Loss function must be differentiable.



---



# Prepare Data


```python
# Import
import pandas as pd
fish = pd.read_csv("https://bit.ly/fish_csv_data")
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish['Species'].to_numpy()
```


```python
# Split
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42
)
train_input.shape, test_input.shape, train_target.shape, test_target.shape
```




    ((119, 5), (40, 5), (119,), (40,))




```python
# Normalize
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
```

※ To prevent data leakage, make sure to convert the test set to the statistics learned from the training set.
※ Data leakage : containing the information you want to predict in the data used for model training 



---



# SGD Classifier

## Fitting model
- set 2 parameter in SGD Classifier
  + loss : specifying the type of loss function
  + max_iter : specifying the number of epochs to be executed
- In the case of a multi-classification model,<br/> if loss is set as 'log', a binary classification model is created for each class.


```python
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log', max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))
```

    0.773109243697479
    0.775
    

    /usr/local/lib/python3.7/dist-packages/sklearn/linear_model/_stochastic_gradient.py:700: ConvergenceWarning: Maximum number of iteration reached before convergence. Consider increasing max_iter to improve the fit.
      ConvergenceWarning,
    


```python
# partial_fit() : continue training one epoch per call
sc.partial_fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))
```

    0.8151260504201681
    0.85
    

## Finding appropriate epoch


```python
import numpy as np
sc = SGDClassifier(loss='log', random_state=42)
train_score = []
test_score = []
classes = np.unique(train_target)

for _ in range(0, 300): # _ : temporal variable
  sc.partial_fit(train_scaled, train_target, classes=classes)
  train_score.append(sc.score(train_scaled, train_target))
  test_score.append(sc.score(test_scaled, test_target))
```


```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(train_score)
ax.plot(test_score)
ax.set_xlabel('epoch')
ax.set_ylabel('accuracy')
plt.show()
```


    
![](/images/Python/ML/ML_ch_4_2.png)
    


- In the early stages of epoch, the scores of training sets and test sets are low because they are underfitting.
- After epoch 100, the score difference between the training set and the test set gradually increases.
- Epoch 100 appears to be the most appropriate number of iterations.


```python
# SGD classifier stops by itself, if performance does not improve during a certain epoch.
# tol = None : to repeat unconditionally untill max_iter
sc = SGDClassifier(loss='log', max_iter=100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))
```

    0.957983193277311
    0.925
    

*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*