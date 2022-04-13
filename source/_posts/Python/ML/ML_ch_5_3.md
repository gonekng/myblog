---
title: "ML Practice 5_3"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-03-30 16:48:30
---

# Ensemble
- algorithm that performs best in dealing with structured data
- Bagging : A method of aggregating results by taking multiple bootstrap samples and training each model. (parallel learning)
  + Random Forest
- Boosting : (sequential learning)
  + GBM --> XGBoost --> LightGBM



---



# Random Forest
- Create decision trees randomly and make final predictions based on each tree's predictions.
  + Classification : Average the probabilities for each class of each tree and uses the class with the highest probability as a prediction.
  + Regression : Average the predictions of each tree.
- Bootstrap : method of sampling data by permitting duplication in a dataset


```python
import numpy as np
import pandas as pd
wine = pd.read_csv('https://bit.ly/wine_csv_data')

data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42
)
```


```python
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score'])) # overfitting
```

    0.9973541965122431 0.8905151032797809
    


```python
rf.fit(train_input, train_target)
print(rf.feature_importances_)
```

    [0.23167441 0.50039841 0.26792718]
    

- OOB(out of bag) Sample : remaining sample not included in bootstrap sample
  + same effect as cross-validation using a verification set


```python
rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
rf.fit(train_input, train_target)
print(rf.oob_score_)
```

    0.8934000384837406
    



---



# GBM(Gradient Boosting Machine)
- Correct errors in previous trees by using shallow trees.
- Adjust the speed (step width) through the learning rate parameter
- less likely to overfit but speed is slow


```python
from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score'])) # good fitting
```

    0.8881086892152563 0.8720430147331015
    


```python
# n_estimators = 500 (default 100), learning rate = 0.2 (default 0.1)
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2, random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score'])) # good fitting
```

    0.9464595437171814 0.8780082549788999
    



---



# Overall Flow of ML
0. Data preprocessing, EDA, Visualization
1. Design the entire flow as a basic model
2. compare multiple models with default hyperparameter
3. Cross-validation and Hyperparameter tuning
4. Repeat the above process until finding the best result

*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*