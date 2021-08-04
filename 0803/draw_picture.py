import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
img.fill(255) #255
img=cv2.line(img,(300,0),(100,511),(0,255,0),5) #line

img=cv2.rectangle(img,(100,150),(500,300),(255,255,0),7) #rectangle

img=cv2.circle(img,(300,200),100,(255,0,1),-1) #circle

cv2.imshow('JetsonNano_line+rectangle+circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
