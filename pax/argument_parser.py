import getopt

CORRECT_USAGE = 'strobe_destroyer.py -i <inputfile> -o <outputfile> -c <codecName>'


def parseArguments(argv):
    inputFile = ''
    outputFile = ''
    codecName = ''

    try:
        opts, _ = getopt.getopt(argv, "hi:o:c:", ["ifile=", "ofile=", "codecName="])

    except getopt.GetoptError:
        return (False, ('', '', ''))

    for opt, arg in opts:
        if opt == '-h':
            return (False, ('', '', ''))

        elif opt in ("-i", "--ifile"):
            inputFile = arg

        elif opt in ("-o", "--ofile"):
            outputFile = arg

        elif opt in ("-c", "--codecName"):
            codecName = arg

    if not inputFile or not outputFile:
        return (False, ('', '', ''))

    else:
        return (True, (inputFile, outputFile, codecName))
