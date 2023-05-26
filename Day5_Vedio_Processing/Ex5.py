import cv2

video = cv2.VideoCapture('Demo.mp4')

frames = []
while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        frames.append(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video.release()

# Reverse the video frames
reversed_frames = frames[::-1]

# Play the reversed video frames
for frame in reversed_frames:
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
