import cv2


def capture_size(capture):
    width = capture.get(3)  # frame width
    height = capture.get(4)  # frame height

    print("Width: ", width)
    print("Height: ", height)

    return (int(width), int(height))


def codec(codecName):
    print("Using codec:", codecName)
    return cv2.VideoWriter_fourcc(*codecName)


def setup_stream(inputFile, outputFile, codecName="avc1"):
    inputVideo = cv2.VideoCapture(inputFile)

    videoSize = capture_size(inputVideo)
    videoCodec = codec(codecName)
    frameRate = 20.0

    outputVideo = cv2.VideoWriter(
        outputFile, videoCodec, frameRate, videoSize, True)

    return (inputVideo, outputVideo)
