#histogram Demo

import cv2
from matplotlib import pyplot as plt
img =cv2.imread("D:\ImageProcessing\Puppy-care.webp",1)
for i in range(3):
    plt.plot(cv2.calcHist([img],[i],None,[256],[0,256]))
plt.show()