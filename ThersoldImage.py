# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 06:50:50 2019

@author: Muhammad
"""
import cv2
from PIL import Image

img=cv2.imread(r"C:\Users\Muhammad\Desktop\img5.jpg")
grayimage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgt=cv2.threshold(grayimage,127,255,cv2.THRESH_BINARY)
cv2.imwrite(r"C:\Users\Muhammad\binaryImage.jpg",imgt)