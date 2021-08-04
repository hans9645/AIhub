import cv2
import numpy as np


def bitwise_operation():
    img1 =cv2.imread('/home/yuto/Documents/AIhub/nanoimage/6_3_Bitwise_Operation_A.png')
    img1=cv2.resize(img1,(256,256))
    img2 =cv2.imread('/home/yuto/Documents/AIhub/nanoimage/6_3_Image_Operation_B.jpg')
    img2=cv2.resize(img2,(512,512))
    point=(512-140,20)

    cv2.imshow('JetsonNano_Original',img1)
    rows,cols,channels=img1.shape
    roi=img2[0:rows,0:cols]

    img2gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    cv2.imshow('JetsonNano_Gray',img2gray)

    ret,mask=cv2.threshold(img2gray,100,255,cv2.THRESH_BINARY)
    mask_inv=cv2.bitwise_not(mask)
    cv2.imshow('JetsonNano_Mask',mask)

    img1_fg=cv2.bitwise_and(img1,img1,mask=mask)
    img2_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
    dst=cv2.add(img1_fg,img2_bg)
    img2[0:rows,0:cols]=dst
    cv2.imshow('JetsonNano_Result',img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
bitwise_operation()


