#Extract Audio from Vedio   
import cv2
import subprocess

video = cv2.VideoCapture('Demo.mp4')
while video.isOpened():
    ret, frame = video.read()
    if ret:
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()

# Extract audio from the video file
output_audio_file = 'audio.wav'
audio_cmd = ['ffmpeg', '-y', '-i', 'Demo.mp4', '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', output_audio_file]
subprocess.call(audio_cmd)
