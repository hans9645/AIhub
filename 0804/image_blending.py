import cv2

def nothing(x):
    pass
def image_blending():
    cv2.namedWindow('JetsonNano_image_Blending')
    cv2.createTrackbar('W','JetsonNano_image_blending',0,100,nothing)

    img1=cv2.imread('/home/yuto/Documents/AIhub/nanoimage/6_2_Image_Blending_A.jpg')
    img1=cv2.resize(img1,(512,512))
    img2=cv2.imread('/home/yuto/Documents/AIhub/nanoimage/6_2_Image_Blending_B.jpg')
    img2=cv2.resize(img2,(512,512))

    while(1):
        w=cv2.getTrackbarPos('W','JetsonNano_image_blending')
        dst=cv2.addWeighted(img1,float(100-w)*0.01,img2,float(w)*0.01,0)
        cv2.imshow('JetsonNano_Image_Blending',dst)
        if cv2.waitKey(1)&0xFF == 27:
            break
        cv2.destroyAllWindows()
image_blending()