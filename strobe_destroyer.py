import cv2
import numpy as np

video = cv2.VideoCapture('lady-gaga.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while True:
    ret, frame = video.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output.write(frame)

    cv2.imshow('grey', grey)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
output.release()
cv2.destroyAllWindows()
