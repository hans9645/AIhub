import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/yuto/Documents/AIhub/nanoimage/7_3_Object_Tracking.jpg',cv2.IMREAD_COLOR)
b,g,r=cv2.split(img)
img=cv2.merge([r,g,b])
pos1=np.float32([[10,10],[30,10],[10,320],[630,320]])
pos2=np.float32([[90,300],[550,300],[125,435],[515,435]])
M=cv2.getPerspectiveTransform(pos2,pos1)
dst=cv2.warpPerspective(img,M,(640,320))
fig=plt.figure()
fig.canvas.manager.set_window_title('Test_Perspective')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(dst),plt.title('Result')
plt.show()