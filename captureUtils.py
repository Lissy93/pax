import cv2


def captureSize(capture):
    width = capture.get(3)  # frame width
    height = capture.get(4)  # frame height

    print("Width: ", width)
    print("Height: ", height)

    return (int(width), int(height))


def codec():
    print("Using codec:", "avc1")
    return cv2.VideoWriter_fourcc(*'avc1')


def setupStream(inputFile, outputFile):
    inputVideo = cv2.VideoCapture(inputFile)

    videoSize = captureSize(inputVideo)
    videoCodec = codec()
    frameRate = 20.0

    outputVideo = cv2.VideoWriter(
        outputFile, videoCodec, frameRate, videoSize, False)

    return (inputVideo, outputVideo)
