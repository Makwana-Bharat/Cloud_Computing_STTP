#Mask Photo on Vedio
import cv2

video = cv2.VideoCapture('Demo.mp4')
avatar = cv2.imread('avatar.jpg')

while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        frame_height, frame_width, _ = frame.shape
        avatar_resized = cv2.resize(avatar, (100, 100))  # Resize the avatar image as per your requirement

        # Overlay the avatar image on the top right corner of the frame
        x_offset = frame_width - avatar_resized.shape[1] - 10  # Adjust the x-offset as needed
        y_offset = 10  # Adjust the y-offset as needed
        frame[y_offset:y_offset+avatar_resized.shape[0], x_offset:x_offset+avatar_resized.shape[1]] = avatar_resized

        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
