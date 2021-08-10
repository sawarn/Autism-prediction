#!/usr/printbin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 13:45:52 2021

@author: ga1ileo
"""

import Autism_1 as au
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import accuracy_score

df=au.df
y=df.autism
x=df.drop(['autism'],axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   n_jobs=None, penalty='l2',
                   random_state=0, solver='newton-cg', tol=0.0001, verbose=0,
                   warm_start=False)
model.fit(x_train,y_train)
prediction=model.predict(x_test)
print("Accuracy =",accuracy_score(y_test,prediction)*100,"%")
saved_model=pickle.dumps(model)




