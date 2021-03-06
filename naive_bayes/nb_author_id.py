#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

classifier = GaussianNB()
training_start_time = time()
classifier.fit(features_train, labels_train)
print "training time:", round(time() - training_start_time, 3), "s"

prediction_start_time = time()
predictions = classifier.predict(features_test)
print "prediction time:", round(time() - prediction_start_time, 3), "s"

accuracy = accuracy_score(labels_test, predictions)
print accuracy
# In local runs, the training time is ~0.7s, the prediction one is ~0.09s and the accuracy is 0.973265.


