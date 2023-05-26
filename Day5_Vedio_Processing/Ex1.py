#Normal Vedio Play
import cv2
video=cv2.VideoCapture('Demo.mp4')
while video.isOpened():
    ret,frame=video.read()
    if ret==True:
        cv2.imshow('Frame',frame)
        key=cv2.waitKey(1)
        if key == ord('q'): break
    else: break
video.release()
cv2.destroyAllWindows()