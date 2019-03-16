import sys

import cv2

from pax import argument_parser, capture_utils

SENSITIVITY = 3  # A number between 0 and 10, for intensity of flashes
BUFFER_SIZE = 3  # The number of frames to hold in history, minimum of 2

# Gets a numeric value, for average brightness of a given frame


def getBrightness(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    value = cv2.split(frame)[2]
    average = cv2.mean(value)
    return average[0]


# Determins if a given frame is a camera flash, or just slight change
def detectIfFlash(frameBrightness):
    if len(frameBrightness) < BUFFER_SIZE:
        return False
    didFlashHappen = True
    for b in range(BUFFER_SIZE-1):
        if frameBrightness[b] + SENSITIVITY > frameBrightness[BUFFER_SIZE-1]:
            didFlashHappen = False
            break
    return didFlashHappen


# Takes a frame which has white flash, brings brightness down to match before frame
def fixFlash():
    return True


def startStream(inputFile, outputFile, codecName):

    inputVideo, outputVideo = capture_utils.setupStream(
        inputFile, outputFile, codecName)
    count = 0  # Iterating through number of frames
    buffer = []

    while inputVideo.isOpened():
        ret, frame = inputVideo.read()

        if ret is True:
            # Calculate brightness of current frame
            frameBrightness = getBrightness(frame)

            # Maintain a buffer of the past 3 frames
            buffer.append(frameBrightness)
            if len(buffer) > BUFFER_SIZE:
                buffer.pop(0)

            # Detect if flash
            if detectIfFlash(buffer):
                print("Flash detected at frame %d" % count)

            count += 1

            outputVideo.write(frame)

        else:
            print("stream failed to read")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("stream ended")
            break

    # Close everything
    outputVideo.release()
    inputVideo.release()
    cv2.destroyAllWindows()


def main(argv):

    (success, (inputFile, outputFile, codecName)
     ) = argument_parser.parseArguments(argv)

    if not success:
        print(argument_parser.CORRECT_USAGE)
        sys.exit()
    else:
        print("inputFile: ", inputFile)
        print("outputFile: ", outputFile)
        startStream(inputFile, outputFile, codecName)


if __name__ == "__main__":
    main(sys.argv[1:])
