import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("D:\ImageProcessing\Puppy-care.webp",1)
img2=abs(255-img1)
titles=['Original','Contrast']
images=[img1,img2]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title=titles[i]
    plt.xticks([])
    plt.yticks([])
plt.show()