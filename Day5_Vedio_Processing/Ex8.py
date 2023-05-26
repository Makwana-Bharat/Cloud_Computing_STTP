import cv2
import os

output_directory = '../Ex8Output/'  # Set the desired output directory

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

video = cv2.VideoCapture('Demo.mp4')
frame_count = 0

while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        frame_count += 1
        # Save the frame as an image
        image_path = os.path.join(output_directory, f'frame_{frame_count}.jpg')
        cv2.imwrite(image_path, frame)
    else:
        break

video.release()
