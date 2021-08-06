import cv2
img=cv2.imread('/home/yuto/Documents/AIhub/Morphology_Ex_Image/MopTest3.png',cv2.IMREAD_COLOR)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

erode_ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
erosion=cv2.erode(thresh,erode_ker,iterations=13)
dilate_ker=cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
dilation=cv2.dilate(erosion,dilate_ker,iterations=3)

cv2.imshow('Original',img)
cv2.imshow('Threshold',thresh)
cv2.imshow('Morphology',dilation)
cv2.waitKey(0)
cv2.destroyAlWindows()