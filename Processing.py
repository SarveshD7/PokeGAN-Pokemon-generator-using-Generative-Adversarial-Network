import cv2
import numpy as np

image = cv2.imread('Photos/pokemon.jpg')
kernel = np.array([[-1, -1, -1],
                   [-1, 10, -1],
                   [-1, -1, -1]])
sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow('Image Sharpening', sharpened)
ret, th = cv2.threshold(sharpened, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Image Thresholding', th)
kernel = np.ones((6, 6), np.float32) / 36
dst = cv2.filter2D(th, -1, kernel)
cv2.imshow("Image Smoothening", dst)
cv2.waitKey(0)
