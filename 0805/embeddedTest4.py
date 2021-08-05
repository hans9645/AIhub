import cv2
from matplotlib import pyplot as plt

img=cv2.imread('',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
th=127
th_max=255

ret,th1=cv2.Threshold(gray,th,th_max,cv2.THRESH_BINARY)
th2=cv2
#to be continue,,,,
