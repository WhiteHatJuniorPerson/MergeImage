import cv2 
import numpy as np

image1 = cv2.imread("wp4471392.jpg")
image3 = cv2.imread("1138973.jpg")
weightedSum = cv2.addWeighted(image1,0.5,image3,0.4,0)
cv2.imshow('Merge',weightedSum)
cv2.waitKey(0)