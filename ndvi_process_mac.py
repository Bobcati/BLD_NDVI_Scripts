import cv2
import numpy as np
import os
from os import listdir
from fastiecm import fastiecm

directory = "/Users/therefore/Desktop/Summer_2023/Plant_Test_Pics/Plant_Pictures"

#increases the contrast of the image
def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out

# Calculate NDVI using blue channel
def calc_ndvi_blue(image):    
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b) / bottom
    return ndvi

def calc_ndvi_red(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

# Convert the ndvi image into a color one
def convert_color_ndvi(image):
    #Contrast the image
    contrasted = contrast_stretch(image)
    #display(contrasted, 'Contrasted original')
    #NDVI and contrast NDVI to make clearer
    ndvi = calc_ndvi_red(contrasted)
    ndvi_contrasted = contrast_stretch(ndvi)
    #display(ndvi_contrasted, "NDVI Blue")
    #Color map the image
    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    
    return color_mapped_image 

# Resource for iterating through all images in a given folder: https://www.geeksforgeeks.org/how-to-iterate-through-images-in-a-folder-python/
def process_all():
    for images in os.listdir(directory):
        currentImage = cv2.imread("Plant_Test_Pics/Plant_Pictures/" + images)
        processedImage = convert_color_ndvi(currentImage)
        cv2.imwrite("Plant_Test_Pics/Red_Test/NDVI_" + images, processedImage)

process_all()