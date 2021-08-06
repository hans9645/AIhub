import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/yuto/Documents/AIhub/Morphology_Ex_Image/MopTest2.png',cv2.IMREAD_GRAYSCALE)
ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel1=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
kernel2=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

#print(ret)
#print(thresh)
dst1=thresh.copy()
dst2=thresh.copy()
print(dst1.shape)
#print(dst2)
dst1=cv2.erode(dst1,kernel1,iterations=1)
dst2=cv2.erode(dst2,kernel2,iterations=1)


dilation=cv2.dilate(dst2,kernel2,iterations=1)


plt.subplot(221),plt.imshow(thresh,'gray')
plt.title('Threshold'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(dst1,'gray')
plt.title('Kernel(3X3)'),plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(dst2,'gray')
plt.title('kernel(7X7)'),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(dilation,'gray')
plt.title('DST'),plt.xticks([]),plt.yticks([])
plt.show()