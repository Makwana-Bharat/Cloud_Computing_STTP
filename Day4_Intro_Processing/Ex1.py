import cv2
img = cv2.imread("D:\ImageProcessing\Puppy-care.webp",0)
cv2.imshow('Gray One',img)
cv2.imwrite("D:\ImageProcessing\gray1.webp",img)
cv2.waitKey(0)
cv2.destroyAllWindows()