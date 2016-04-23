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
from sklearn.metrics import accuracy_score
from sklearn import svm


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

classifier = svm.SVC(kernel='rbf', C=10000)
training_start_time = time()
classifier.fit(features_train, labels_train)
print "training time:", round(time() - training_start_time, 3), "s"

prediction_start_time = time()
predictions = classifier.predict(features_test)
print "prediction time:", round(time() - prediction_start_time, 3), "s"

accuracy = accuracy_score(labels_test, predictions)
print "accuracy ", accuracy

# Linear kernel
#    In local runs, the training time is ~162s, the prediction one is ~18s and the accuracy  is 0.984072.
#    Reducing the training set to 1% of its original size, the training time is ~0.094s, the prediction one is ~0.987s and the accuracy is 0.884527.
# Rbf kernel
#    1% of training set: the training time is ~0.105s, the prediction one is ~1.133s and the accuracy is 0.616040.
#    Using parameter C set to 10K (a more complex decision boundary), accuracy reaches 0.892491.
#    And restoring the full training set, accuracy becomes 0.990898
