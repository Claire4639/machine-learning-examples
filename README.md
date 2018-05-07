## Udacity Datascience course
This is my personal exploration of machine learning. Going through udacity course.

### 01 - Naive Bayesian Classifier
![plot](/01_naiveby_terrain_data/test.png)

Using sklearn to run a naive Bayesian Classifer
```
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train)
```