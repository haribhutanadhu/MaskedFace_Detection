# -*- coding: utf-8 -*-
"""B19EE017_B19EE033.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZQ1uU8HsBu00Hx1EG2HWt1MvOSAGW9AJ
"""

import pandas as pd
import numpy as np
import zipfile  # unziping 
import glob  # finding image paths
import numpy as np  # creating numpy arrays
from skimage.io import imread  # reading images
from skimage.transform import resize  # resizing images
import os
import cv2

#Extractiong zip file
path = '/content/Dataset.zip'
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('Dataset')

!ls
#resizing the images
size=64
names = os.listdir("/content/Dataset/Dataset/with_mask/")                                          
mask = [cv2.resize(cv2.imread("/content/Dataset/Dataset/with_mask/"+img), (size,size)) for img in names]
#print(len(mask))

mask

!ls
size=64
names = os.listdir("/content/Dataset/Dataset/without_mask/")                                          
nomask = [cv2.resize(cv2.imread("/content/Dataset/Dataset/without_mask/"+img), (size,size)) for img in names]
#print(len(nomask))

nomask

# y is class label
x = np.array(mask + nomask)
y = np.array([1]*len(mask) + [0]*len(nomask))

x

y

import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import matplotlib.pyplot as plt # Visualization

nsamples, nx, ny, nz = x.shape
x = x.reshape((nsamples,nx*ny*nz))

"""Splitting the Dataset"""

from sklearn.model_selection import train_test_split
train_ratio = 0.7
validation_ratio = 0.2
test_ratio = 0.1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 - train_ratio)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size=test_ratio/(test_ratio + validation_ratio))

"""KNN Model"""

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
k_range = list(range(1, 9))
param_knn = dict(n_neighbors=k_range)
clf_knn = KNeighborsClassifier(n_neighbors=5)
grid_knn = GridSearchCV(clf_knn, param_knn, cv=5, scoring='accuracy')
grid_knn.fit(x_val, y_val)

print(grid_knn.best_params_)

print(grid_knn.best_score_)

from sklearn.model_selection import cross_val_score
clf_knn=grid_knn.best_estimator_
clf_knn.fit(x_train,y_train)
scores_knn = cross_val_score(clf_knn, x, y, cv = 5)
scores_knn

print(clf_knn.score(x_train,y_train))

print(clf_knn.score(x_test,y_test))

y_pred_knn= clf_knn.predict(x_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred_knn))

"""SVM Model"""

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
parameters= {'kernel': ('linear','rbf','poly'),'C': [1, 10, 100]}
clf_svm=SVC(gamma='scale')
grid_svm = GridSearchCV(clf_svm,parameters,cv=5)
grid_svm.fit(x_val,y_val)

print(grid_svm.best_params_)

print(grid_svm.best_score_)

clf_svm=grid_svm.best_estimator_
clf_svm.fit(x_train,y_train)

from sklearn.model_selection import cross_val_score
scores_svm = cross_val_score(clf_svm, x, y, cv = 5)
scores_svm

print(clf_svm.score(x_train,y_train))

print(clf_svm.score(x_test,y_test))

y_pred_svm= clf_svm.predict(x_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred_svm))

"""MLP Model"""

from sklearn.neural_network import MLPClassifier
clf_mlp = MLPClassifier()
param_mlp={'max_iter':(100, 500, 1000)}
grid_mlp = GridSearchCV(clf_mlp, param_mlp, n_jobs=-1, cv=5)
grid_mlp.fit(x_val, y_val)

print(grid_mlp.best_params_)

print(grid_mlp.best_score_)

clf_mlp=grid_mlp.best_estimator_
clf_mlp.fit(x_train,y_train)
scores_mlp = cross_val_score(clf_mlp, x, y, cv = 5)
scores_mlp

print(clf_mlp.score(x_test,y_test))

print(clf_mlp.score(x_train,y_train))

y_pred_mlp= clf_mlp.predict(x_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred_mlp))

"""Comparison of Model Performances

"""

from matplotlib import pyplot
from matplotlib import pyplot as plt
plt.figure(figsize=(7,5))
res=[[0.78476821, 0.80125828, 0.80794702, 0.80395349, 0.75049834],[0.93377483, 0.94039735, 0.93046358, 0.93023256, 0.95348837],[0.95033113, 0.5, 0.89735099, 0.50166113, 0.95681063]]
name=["KNN","SVM","MLP"]
pyplot.boxplot(res,labels=name,showmeans=True)
pyplot.show()








