#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

classifier = tree.DecisionTreeClassifier(min_samples_split=40)

training_start_time = time()
classifier.fit(features_train, labels_train)
print "training time:", round(time() - training_start_time, 3), "s"

prediction_start_time = time()
predictions = classifier.predict(features_test)
print "prediction time:", round(time() - prediction_start_time, 3), "s"

accuracy = accuracy_score(labels_test, predictions)
print "accuracy ", accuracy

# In local runs, the training time is ~32.3s, the prediction one is ~0.015s and the accuracy is 0.977815.
# Regarding the feature selection, if we use percentile=1 (rather than 10) for SelectPercentile, we get
# a training time around 3.3s, the prediction one ~0.003s and the accuracy is 0.965870