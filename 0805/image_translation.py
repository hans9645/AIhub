import cv2
import numpy as np

def image_translation():
    img=cv2.imread('/home/yuto/Documents/AIhub/nanoimage/9_1_Transformations.png',cv2.IMREAD_COLOR)
    height,width,c=img.shape

    shrink=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    zoom1=cv2.resize(img,(width*2,height*2),fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
    zoom2=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

    cv2.imshow('JetsonNano_Original',img)
    cv2.imshow('JetsonNano_Shrink',shrink)
    cv2.imshow('JetsonNano_Zoom1',zoom1)
    cv2.imshow('JetsonNano_Zoom2',zoom2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_translation()