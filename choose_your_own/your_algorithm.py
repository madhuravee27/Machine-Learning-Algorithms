#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors = 1)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,pred)

print "Accuracy for KNN:", accuracy


from sklearn.ensemble import RandomForestClassifier

clf_randomforest= RandomForestClassifier(n_estimators = 30, min_samples_split = 7)
clf_randomforest.fit(features_train, labels_train)
pred = clf_randomforest.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,pred)

print "Accuracy for Random Forest:", accuracy

from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC


clf = AdaBoostClassifier(base_estimator = SVC(C = 482, kernel = "rbf", gamma = 3.1), n_estimators = 30, algorithm='SAMME')
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,pred)
print "Accuracy for Adaboost: ",accuracy


#print len(pred)
#print len(labels_test)

'''
try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
'''