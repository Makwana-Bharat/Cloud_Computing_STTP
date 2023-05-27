#rotet Live  Vedio 
import cv2

video = cv2.VideoCapture(0)
size = (int(video.get(3)), int(video.get(4)))
result = cv2.VideoWriter('Ex3Output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, size)

while video.isOpened():
    ret, frame = video.read()

    # Rotate the frame by 90 degrees clockwise
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    result.write(frame)

    if ret:
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
