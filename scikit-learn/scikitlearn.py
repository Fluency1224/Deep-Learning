#########################################################################
# File Name: scikitlearn.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 17 Apr 2018 02:46:01 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print(iris_X[:2,:])
print(iris_y)

X_train, X_test, y_train, y_test = train_test_split(
        iris_X,iris_y,test_size=0.3)

print(y_train)


knn = KNeighborsClassifier()
knn.fit(X_train,y_train)

print(knn.predict(X_test))
print(y_test)
