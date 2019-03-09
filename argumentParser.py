import sys
import getopt

CORRECT_USAGE = 'strobe_destroyer.py -i <inputfile> -o <outputfile>'


def parseArguments(argv):
    inputFile = ''
    outputFile = ''

    try:
        opts, _ = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])

    except getopt.GetoptError:
        return (False, ('', ''))

    for opt, arg in opts:
        if opt == '-h':
            return (False, ('', ''))

        elif opt in ("-i", "--ifile"):
            inputFile = arg

        elif opt in ("-o", "--ofile"):
            outputFile = arg

    if not inputFile or not outputFile:
        return (False, ('', ''))

    else:
        return (True, (inputFile, outputFile))
