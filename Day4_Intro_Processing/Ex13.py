import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread("D:\ImageProcessing\Puppy-care.webp", cv2.IMREAD_GRAYSCALE)

# Display the original image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Set the sampling rate
samplerate = 8

# Calculate the dimensions of the resized imagex``
new_height = img.shape[0] // samplerate
new_width = img.shape[1] // samplerate

# Resize the image using sampling rate
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('ReSized', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Zoom in by resizing to a larger size
zoomed_width = new_width * 4  # Adjust the zoom factor as needed
zoomed_height = new_height * 4
zoomed_img = cv2.resize(resized_img, (zoomed_width, zoomed_height), interpolation=cv2.INTER_CUBIC)

# Display the zoomed image
cv2.imshow('Zoomed', zoomed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
