import cv2 
from matplotlib import pyplot as plt

img =cv2.imread('/home/yuto/Documents/AIhub/2_1_Image_RSW.jpg',cv2.IMREAD_COLOR)
fig=plt.figure()

fig.canvas.set_window_title('JetsonNano_Matplot1')
plt.imshow(img)
plt.xticks([])
plt.yticks([])
#plt.show()


fig=plt.figure()
fig.canvas.set_window_title('JetsonNano_Matplot2')
b,g,r=cv2.split(img)
img2=cv2.merge([r,g,b])
plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()