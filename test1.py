import cv2
 
def image_RSW():
    fname='./download.jpeg'
    original =cv2.imread(fname,cv2.IMREAD_COLOR)
    cv2.imshow('JetsonNano_Original',original)
    gray = cv2.imread(fname,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('JetsonNano_gray',gray)
    unchange=cv2.imread(fname,cv2.IMREAD_UNCHANGED)
    cv2.imshow('JetsonNano_Unchange',unchange)

    cv2.imwrite('GrayImage.png',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
