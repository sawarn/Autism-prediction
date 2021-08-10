#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:53:03 2021

@author: ga1ileo
"""

import Autism_2 as au
import easygui
import numpy as np
import pandas as pd
import pickle

easygui.msgbox("Welcome!", title="Message")

inputs=[]
inputs.append(input("Enter your age: "))
inputs.append(input("Gender: "))
inputs.append(input("What is your Ethnicity: "))
inputs.append(input("Do you have jaundice?: "))
inputs.append(input("Enter country of residence: "))
inputs.append(input("He/She often notices small sounds when others do not or notices patterns all the time?: "))
inputs.append(input("He/She usually concentrates more on the whole picture, rather than the small detail: "))
inputs.append(input("In a social group, he/she can easily keep track of several different peoples conversations: "))
inputs.append(input("If there is an interruption, he/she can switchback to what he/she was doing very quick,: "))
inputs.append(input("He/She doesnt know how to keep a conversation going with his/her peers: "))
inputs.append(input("He/She knows how to tell if someone listening to him/her is getting bored: "))
inputs.append(input("When he/she was younger,he/she used to enjoy playing games involving pretending with other children: "))
inputs.append(input("Does he/she like to collect information about categories of things(e.g. types of car, types of bird, types of train, types of plant etc): "))
inputs.append(input("Does he/she find it easy to work out what someone is thinking or feeling just by looking at their face: "))
inputs.append(input("Does he/she find it difficult to work out peoples intentions: "))

inputs=list(map(int,inputs))
result=inputs[5]+inputs[6]+inputs[7]+inputs[8]+inputs[9]+inputs[10]+inputs[11]+inputs[12]+inputs[13]+inputs[14]
inputs.append(result)
col=['age','gender','ethnicity','jaundice','country_of_res','A1_Score','A2_Score','A3_Score','A4_Score','A5_Score','A6_Score','A7_Score','A8_Score','A9_Score','A10_Score','result']

input_dict={}

for key in col:
    for value in inputs:
        input_dict[key]=value
        inputs.remove(value)
        break

df=pd.DataFrame(input_dict,index=[0])
#print(df)
#loaded_model=pickle.loads(au.saved_model)
#loaded_model.predict(arr)
