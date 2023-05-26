#Create Video
import cv2
video=cv2.VideoCapture(0)
size=(int(video.get(3)),int(video.get(4)))
result=cv2.VideoWriter('Ex3Output.avi',cv2.VideoWriter_fourcc(*'MJPG'),30,size)
while video.isOpened():
    ret,frame=video.read()
    result.write(frame)
    if ret==True:
        cv2.imshow('Frame',frame)
        key=cv2.waitKey(1)
        if key == ord('q') : break
    else: break
video.release()
cv2.destroyAllWindows()