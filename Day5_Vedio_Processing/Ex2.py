import os
import cv2
import datetime

video = cv2.VideoCapture('Demo.mp4')

frame_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

video_size_mb = os.stat('Demo.mp4').st_size / (1024 * 1024)

duration = frame_count / fps
duration = datetime.timedelta(seconds=int(duration))

print('Video Width:', frame_width)
print('Video Height:', frame_height)
print('Video FPS:', fps)
print('Video FRAMES:', frame_count)
print('Video Size:', video_size_mb, 'MB')
print('Video Duration:', duration)

video.release()
cv2.destroyAllWindows()