#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:57:34 2021

@author: ga1ileo
"""

import Autism_3 as au
import pickle
import Autism_2 as au1

loaded_model=pickle.loads(au1.saved_model)
prediction=loaded_model.predict(au.df)
if prediction==0:
    print("The user does not show strong symptoms of Autism")
elif prediction==1:
    print("The user shows symptoms of Autism")
else:
    print("Inconclusive")



