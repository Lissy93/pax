import cv2
import numpy as np
import sys
import argumentParser
import captureUtils


def startStream(inputFile, outputFile):

    inputVideo, outputVideo = captureUtils.setupStream(inputFile, outputFile)

    while inputVideo.isOpened():

        ret, frame = inputVideo.read()

        if ret == True:
            # TODO: Alicia to add her bits here...
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            outputVideo.write(grey)

        else:
            print("stream failed to read")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("stream ended")
            break

    outputVideo.release()
    print("Output released")

    inputVideo.release()
    print("Input released")

    cv2.destroyAllWindows()
    print("Windows destroyed")


def main(argv):

    (success, (inputFile, outputFile)) = argumentParser.parseArguments(argv)

    if not success:
        print(argumentParser.CORRECT_USAGE)
        sys.exit()

    else:
        print("inputFile: ", inputFile)
        print("outputFile: ", outputFile)

        startStream(inputFile, outputFile)


if __name__ == "__main__":
    main(sys.argv[1:])
