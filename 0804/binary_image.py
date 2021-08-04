import cv2
import numpy as np

def image_binary():
    img=cv2.imread('/home/yuto/Documents/AIhub/nanoimage/7_1_Binary_Image.jpg',cv2.IMREAD_COLOR)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,dst=cv2.threshold(gray,140,255,cv2.THRESH_BINARY) 
    #cv2.THRESH_OTSU : cv2 for otsu's binary, regardless of parameter it just adjust everyrhing automatically

    cv2.imshow('JetsonNano_Original',img)
    cv2.imshow('JetsonNano_Binary',dst)
    print(ret)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_binary()