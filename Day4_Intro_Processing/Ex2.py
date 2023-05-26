import cv2
img = cv2.imread("D:\ImageProcessing\Puppy-care.webp",1)

print(type(img))
print('Image Data Type: ',img.dtype)
print('Row Column: ',img.shape)
print('Dimensions: ',img.ndim)
print('Image Size: ',img.size)

(nr,nc,ch)=img.shape

print('Rows: ',nr)
print('Column: ',nc)
print('Channels: ',ch)
cv2.imshow('Gray One',img)
cv2.imwrite("D:\ImageProcessing\gray1.webp",img)
cv2.waitKey(0)
cv2.destroyAllWindows()