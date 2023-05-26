#scale or resize
import cv2
img = cv2.imread("D:\ImageProcessing\Puppy-care.webp",1)
result=cv2.resize(img,None,fx=0.6,fy=0.6)
cv2.imshow('Resize',result)
cv2.waitKey(0)
cv2.destroyAllWindows()