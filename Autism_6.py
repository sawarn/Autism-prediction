#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:37:16 2022

@author: sivjos
"""


import nibabel as nb

image1="/home/sivjos/Downloads/mprage.nii.gz"
image2="/home/sivjos/Downloads/rest.nii.gz"

ni_image1=nb.load(image1)
ni_image2=nb.load(image2)

img1_data=ni_image1.get_fdata()
img2_data=ni_image2.get_fdata()

print(img1_data.shape)
print(img2_data.shape)

import matplotlib.pyplot as plt
def show_slices(slices):
   """ Function to display row of image slices """
   fig, axes = plt.subplots(1, len(slices))
   for i, slice in enumerate(slices):
       axes[i].imshow(slice.T, cmap="gray", origin="lower")
       
show_slices([img1_data[128, :, :],
             img1_data[:, 66, :],
             img1_data[:, :, 128]])

show_slices([img2_data[32, :, :,:],
             img2_data[:, 32, :,:],
             img2_data[:, :, 14,:],
             img2_data[:, :,:,90]])