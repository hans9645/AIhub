import cv2
fname='/home/yuto/Documents/AIhub/download.jpeg'
original=cv2.imread(fname,cv2.IMREAD_COLOR)

b,g,r=cv2.split(original)
original[:,:,0]=0 # there are three color channel so, it allows only two channel to make yellow picture
cv2.imshow('Image',original)
cv2.imwrite('file3.png',original)
cv2.waitKey(0)
cv2.destroyAllWindows()