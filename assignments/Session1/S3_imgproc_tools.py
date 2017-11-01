# -*- coding: utf-8 -*-
##
#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : Image processing basics : inverse image colors

# import the OpenCV library
import cv2
# import the numpy library
import numpy as np

# load an image in gray levels
img_gray=cv2.imread('myimage.jpg',0)
# load an image in Blue Green Red
img_bgr=cv2.imread('myimage.jpg',1)

# display the matrix shapes
print("Gray levels image shape = "+ str(img_gray.shape))
print("BGR image shape = "+ str(img_bgr.shape))

# display the loaded images
cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)

cv2.waitKey(0)

def invert_colors_manual(input_img):
    ##
    # Function able to inverse colors of an image
    # @param input_img: the input img to be scanned

    (x,y,z) = (input_img.shape[:3])
    for i in range(x):
        for j in range(y):
            for k in range(z):
                input_img[i,j,k]=255-input_img[i,j,k]
                 
    return input_img

def invert_colors_numpy(input_img):
    ##
    # Function able to inverse colors of an image using numpy
    # @param input_img: the input img to be scanned

    reverse_image=255 - input_image
    return reverse_image

def invert_colors_opencv(input_img):
    ##
    # Function able to inverse colors of an image using opencv
    # @param input_img: the input img to be scanned

    reverse_image=cv2.bitwise_not(input_image)
    return reverse_image
