import cv2
def image_add():
    img2=cv2.imread('/home/yuto/Documents/AIhub/download.jpeg')
    img1=cv2.imread('/home/yuto/Documents/AIhub/2_1_Image_RSW.jpg')

    h,w,c=img2.shape

    img_add=img1.copy()
    img_add[50:h+50,600:w+600]=img2


    cv2.imshow('JetsonNano_Add_Image1',img1)
    cv2.imshow('JetsonNano_Add_Image2',img2)
    cv2.imshow('JetsonNano_Add_Result',img_add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_add()