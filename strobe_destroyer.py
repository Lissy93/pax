import cv2
import numpy as np

video = cv2.VideoCapture('video-sources/lady-gaga.mp4')


fourcc = cv2.VideoWriter_fourcc(*'H264')
output = cv2.VideoWriter('./output.mp4', fourcc, 20.0, (1280, 720), False)

while video.isOpened():

    ret, frame = video.read()

    if ret == True:
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        output.write(grey)
        cv2.imshow('grey', grey)

        print("frame saved")
    else:
        print("stream failed to read")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("stream ended")
        break

output.release()
print("Output released")

video.release()
print("Input released")

cv2.destroyAllWindows()
print("Windows destroyed")
