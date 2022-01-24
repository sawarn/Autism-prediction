#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:41:26 2021

@author: ga1ileo
"""

import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.constraints import maxnorm
from keras import backend as K 
import pickle
from keras.models import model_from_json

from keras.utils import np_utils
import os
from imutils import paths
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix

img_width, img_height = 200, 200

train_data="/home/sivjos/Desktop/Autism-Prediction/Train/"
test_data="/home/sivjos/Desktop/Autism-Prediction/Test/"

train_path = list(paths.list_images(train_data)) 
#print(train_path)
totalTrain = len(train_path)
totalTest = len(list(paths.list_images(test_data)))   
      
trainLabels = [p.split(os.path.sep)[6] for p in train_path] 
#trainLabels= [a.split(os.path.sep) for a in trainLabels]
trainLabels= (map(str,trainLabels))
trainLabels= list(map(str,[b.split("_",1)[0:1] for b in trainLabels]))
print(trainLabels)

#trainLabels= list(map(int,trainLabels))

classWeight = dict()
epochs = 30
batch_size = 10

if K.image_data_format() == 'channels_first':
    input_shape = (6, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)
    
model = Sequential(name="GLU")
model.add(Conv2D(64, (3, 3), padding="same",input_shape=(300,300,3)))
model.add(Activation("relu"))

model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (4, 4), padding="same"))
model.add(Activation("relu"))

model.add(Conv2D(128, (4, 4), padding="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))


model.add(Conv2D(256, (4, 4), padding="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation("softmax"))


train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    rotation_range = 40,
    width_shift_range = 0.3,
    height_shift_range = 0.3,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    shuffle = True,
    color_mode="rgb",
    class_mode='categorical') 

test_generator = test_datagen.flow_from_directory(
	test_data,
	class_mode="categorical",
	target_size=(img_width, img_height),
	color_mode="rgb",
	shuffle=False,
	batch_size = batch_size)

optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])


model.fit(
    train_generator,
    steps_per_epoch=totalTrain // batch_size,
    epochs=epochs,
    #validation_data=validation_generator,
    #validation_steps=totalValidation // batch_size,
    class_weight = classWeight)                             #fitting the model

print("[INFO] evaluating network...")
test_generator.reset()
predIdxs = str(model.predict(x=test_generator, steps=(totalTest // batch_size) + 1))
model_json = model.to_json()
with open("model.json", "w") as json_file:
  json_file.write(model_json)



