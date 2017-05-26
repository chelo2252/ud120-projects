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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC

classifier = SVC(kernel='rbf', C=10000.)

t0 = time()
classifier.fit(features_train, labels_train)
print "\ntraining time:", round(time()-t0, 3), "s\n"

t0 = time()
labels_predicted = classifier.predict(features_test)
print "\nprediction time:", round(time()-t0, 3), "s\n"

accuracy = classifier.score(features_test, labels_test)

print 'Accuracy: ', accuracy 

chris = 0
sara = 0
for prediction in labels_predicted:
	if(prediction == 1):
		chris +=1
	else:
		sara +=1

print 'Chris: ', chris, '\n', 'Sara: ', sara, '\n'


