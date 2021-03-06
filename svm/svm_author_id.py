#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

import numpy as np
from sklearn.metrics import accuracy_score
from class_vis import prettyPicture


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
#print labels_train
#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(kernel="rbf", C=10000)
clf.fit(features_train, labels_train)  
print "fitting model"
pred = clf.predict(features_test)


print "No of chris emails: ", sum(pred)
acc = accuracy_score(pred, labels_test)
print "accuracy: ", acc
#########################################################
"""34, 37"""
