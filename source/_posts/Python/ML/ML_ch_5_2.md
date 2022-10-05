---
title: "ML Practice 5_2"
categories:
  - python
  - ML
tag:
  - python
  - machine learning
  - google colab
author: "Jiwon Kang"
date: 2022-03-30 15:40:40
---

# Cross Validation
#### : Repeated process of spliting validation set and evaluating model.
- Train set : Validation set : Test set = 6 : 2 : 2 (generally)
- Test sets are not used in the model learning process.
- In Kagge competition, test sets are given separately.
- purpose : To make a good model
  + A good model doesn't mean high-performance model.
  + A good model means low-error and stable model.
- Because it takes a long time, it is useful when there is not much data.

### Prepare data


```python
import pandas as pd
wine = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine[['class']].to_numpy()
```


```python
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42
)
sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42
)
```


```python
sub_input.shape, val_input.shape, test_input.shape
```




    ((4157, 3), (1040, 3), (1300, 3))



### Create model


```python
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target)) # overfitting
```

    0.9971133028626413
    0.864423076923077
    

### Validate model


```python
from sklearn.model_selection import cross_validate
scores = cross_validate(dt, train_input, train_target) # dictionary type
for item in scores.items():
  print(item)
```

    ('fit_time', array([0.01251197, 0.00755358, 0.0074594 , 0.00742102, 0.00734329]))
    ('score_time', array([0.00133634, 0.00079608, 0.0007925 , 0.00083232, 0.00076413]))
    ('test_score', array([0.86923077, 0.84615385, 0.87680462, 0.84889317, 0.83541867]))
    


```python
import numpy as np
print(np.mean(scores['test_score']))
```

    0.855300214703487
    

- In cross-validation, a splitter must be specified to mix training sets.
  + Regression model > KFold
  + Classification model > StratifiedKFold


```python
from sklearn.model_selection import StratifiedKFold
splitter = StratifiedKFold(shuffle=True, random_state=42) # default : 5 fold
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))
```

    0.8539548012141852
    


```python
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42) # 10 fold
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))
```

    0.8574181117533719
    



---



# Hyperparameter Tuning
- ex) max_depth=3, accuracy=0.84
- Finding the best value by adjusting multiple parameters simultaneously.
- AutoML : technology that automatically performs hyperparameter tuning without intervention of person.
  + Grid Search, Random Search

## Grid Search
- Perform hyperparameter tuning and cross-validation simultaneously
- Find the optimal hyperparameters based on all combinations of predetermined values.


```python
%%time

from sklearn.model_selection import GridSearchCV
params = {
    'min_impurity_decrease' : [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]
}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)
```

    CPU times: user 70.1 ms, sys: 6.06 ms, total: 76.1 ms
    Wall time: 183 ms
    


```python
dt = gs.best_estimator_
print(dt)
print(dt.score(train_input, train_target))
```

    DecisionTreeClassifier(min_impurity_decrease=0.0001, random_state=42)
    0.9615162593804117
    


```python
print(gs.cv_results_['mean_test_score'])
print(gs.best_params_)
```

    [0.86819297 0.86453617 0.86492226 0.86780891 0.86761605]
    {'min_impurity_decrease': 0.0001}
    


```python
%%time

from sklearn.model_selection import GridSearchCV
params = {
    'min_impurity_decrease' : [0.0001, 0.0002, 0.0003, 0.0004, 0.0005],
    'max_depth' : [3, 4, 5, 6, 7]
}

# Change the values in params and create a total of 5 models with each value.
# n_jobs=-1 : to enable all cores in the system
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)
```

    CPU times: user 167 ms, sys: 4.85 ms, total: 172 ms
    Wall time: 585 ms
    


```python
dt = gs.best_estimator_
print(dt)
print(dt.score(train_input, train_target))
```

    DecisionTreeClassifier(max_depth=7, min_impurity_decrease=0.0005,
                           random_state=42)
    0.8830094285164518
    


```python
print(gs.cv_results_['mean_test_score']) # 5*5=25
print(gs.best_params_)
```

    [0.84125583 0.84125583 0.84125583 0.84125583 0.84125583 0.85337806
     0.85337806 0.85337806 0.85337806 0.85318557 0.85780355 0.85799604
     0.85857352 0.85857352 0.85838102 0.85645721 0.85799678 0.85876675
     0.85972866 0.86088306 0.85607093 0.85761031 0.85799511 0.85991893
     0.86280466]
    {'max_depth': 7, 'min_impurity_decrease': 0.0005}
    

- The optimal value of 'min_impurity_decrease' varies when the value of 'max_depth' changes.

## Random Search
- Find the optimal hyperparameters based on possible combinations within a predetermined range of values.
- Delivers probability distribution objects that can sample parameters.


```python
# randint : sampling int
# uniform : sampling float
from scipy.stats import uniform, randint
params = {
    'min_impurity_decrease' : uniform(0.0001, 0.001),
    'max_depth' : randint(20, 50)
}
```


```python
%%time

from sklearn.model_selection import RandomizedSearchCV
gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params,
                        n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)
```

    CPU times: user 629 ms, sys: 15.8 ms, total: 645 ms
    Wall time: 2.54 s
    


```python
dt = gs.best_estimator_
print(dt)
print(dt.score(train_input, train_target))
```

    DecisionTreeClassifier(max_depth=29, min_impurity_decrease=0.000437615171403628,
                           random_state=42)
    0.8903213392341736
    


```python
print(gs.best_params_)
```

    {'max_depth': 29, 'min_impurity_decrease': 0.000437615171403628}
    

*Ref.) <u> 혼자 공부하는 머신러닝+딥러닝 (박해선, 한빛미디어) <u/>*