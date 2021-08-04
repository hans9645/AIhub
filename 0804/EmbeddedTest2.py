import cv2
fname='/home/yuto/Documents/AIhub/download.jpeg'
original=cv2.imread(fname,cv2.IMREAD_COLOR)

b,g,r=cv2.split(original)
#b=0
original=cv2.merge((b,g,r))
cv2.imshow('Image',original)
#cv2.imwrite('file3.png',original)
cv2.waitKey(0)
cv2.destroyAllWindows()