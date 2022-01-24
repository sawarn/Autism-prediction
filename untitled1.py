#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:51:14 2021

@author: sivjos
"""

import nibabel as ni
img=ni.load('/home/sivjos/Desktop/mprage.nii.gz')

img_data=img.get_fdata()
print(img_data.shape)

import matplotlib.pyplot as plt
def show_slices(slices):
   """ Function to display row of image slices """
   fig, axes = plt.subplots(1, len(slices))
   for i, slice in enumerate(slices):
       axes[i].imshow(slice.T, cmap="gray", origin="lower")
slice_0 = img_data[128, :, :]
slice_1 = img_data[:, 66, :]
slice_2 = img_data[:, :, 128]
show_slices([slice_0, slice_1, slice_2])
plt.suptitle("Center slices for EPI image")  