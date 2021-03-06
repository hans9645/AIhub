import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/divertome/github_repository/AIhub-1/download.jpeg', 0)
rows,cols=img.shape
crow,ccol=rows//2, cols//2


f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
magnitude_spectrum=20*np.log(np.abs(fshift))

fshift[crow-30:crow+30,ccol-30:ccol+30]=0
f_shift=np.fft.ifftshift(fshift)
img_back=np.fft.ifft2(f_shift)
img_back=np.abs(img_back)

fig=plt.figure()
fig.canvas.manager.set_window_title('JetsonNano_Fourier')
plt.subplot(131),plt.imshow(img,cmap='gray')
plt.title('Input Image'),plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(img_back,cmap='gray')
plt.title('Image after HPF'),plt.xticks([]),plt.yticks([])
plt.show()

