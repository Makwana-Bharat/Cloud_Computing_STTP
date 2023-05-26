#sharping blur
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:\ImageProcessing\Puppy-care.webp",1)
k2=np.array(([-1,-1,-1],[-1,9,-1],[-1,-1,-1]),np.float32)
print(k2)
output=cv2.filter2D(img,-1,k2)
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),'gray')
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(output,cv2.COLOR_BGR2RGB),'gray')
plt.title('Filtered Images')
plt.show()

# homework
# -prewit
# -sobel