#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

#training time= 0.06 s - prtime=0.016s - accuracity = 0.916
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=25, criterion='entropy')

t0 = time()
clf.fit(features_train, labels_train)
print "\ntraining time:", round(time()-t0, 3), "s\n"

t0 = time()
clf.predict(features_test)
print "\nprediction time:", round(time()-t0, 3), "s\n"

print "The accuracity is ", clf.score(features_test, labels_test)
