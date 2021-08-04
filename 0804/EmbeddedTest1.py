import cv2

fname='/home/yuto/Documents/AIhub/2_1_Image_RSW.jpg'
original=cv2.imread(fname,cv2.IMREAD_COLOR)

img1=original.copy()
img1=cv2.putText(img1,'AI HUB',(500,600),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)

img2=original.copy()
img2=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
img2=cv2.putText(img2,'AI HUB',(500,600),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

cv2.imwrite('file1.png',img1)
cv2.imwrite('file2.png',img2)

cv2.imshow('image_1',img1)
cv2.imshow('image_2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
