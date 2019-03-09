import cv2
import numpy as np
import matplotlib.pyplot as plt

SENSITIVITY = 3 #  A number between 0 and 10, for intensity of flashes
BUFFER_SIZE = 3 # The number of frames to hold in history, minimum of 2

# Gets a numeric value, for average brightness of a given frame
def getBrightness (frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    value = cv2.split(frame)[2]
    average = cv2.mean(value)
    return average[0]


# Determins if a given frame is a camera flash, or just slight change
def detectIfFlash (frameBrightness):
    if len(frameBrightness) < BUFFER_SIZE:
        return False
    didFlashHappen = True
    for b in range(BUFFER_SIZE-1):        
        if frameBrightness[b] + SENSITIVITY > frameBrightness[BUFFER_SIZE-1]:
            didFlashHappen = False
            break
    return didFlashHappen
    

# Takes a frame which has white flash, brings brightness down to match before frame
def fixFlash ():
    return True

# Start main. Read in video
vidcap = cv2.VideoCapture('sample-videos/lady-gaga.mp4')
success, image = vidcap.read()

count = 0 # Iterating through number of frames

buffer = []

while success:
    # Read stream
    cv2.imwrite("sample-output/frame%d.jpg" % count, image) 

    # Calculate brightness of current frame
    frameBrightness = getBrightness(image)

    # Maintain a buffer of the past 3 frames
    buffer.append(frameBrightness)
    if len(buffer) > BUFFER_SIZE:
        buffer.pop(0))

    # Detect if flash
    if detectIfFlash(buffer):
        print("Flash detected at frame %d" % count)


    success, image = vidcap.read()
    # print('Frame: %d'  % count, success)
    # print(frameBrightness)
    # print(buffer)
    # print()
    count += 1