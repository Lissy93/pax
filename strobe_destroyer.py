import cv2
import numpy as np

video = cv2.VideoCapture('video-sources/lady-gaga.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('sample-output/output.avi', fourcc, 20.0, (250, 250))

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

video.release()
output.release()
cv2.destroyAllWindows()
