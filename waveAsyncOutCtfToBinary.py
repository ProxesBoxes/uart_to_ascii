BYTE_SIZE = 8

fileName = "./async_out.ctf"
currentState = ""
position = 0
tickInterval = 10
currentString = ""
asciiChars = []
skipFirstLine = True
waitingForStart = True
prevState = 1


def swapEndianness(byteToSwap):
    newValue = ""
    for letter in byteToSwap:
        newValue = letter + newValue
    return newValue


with open(fileName, "r") as analogFile:
    for line in analogFile.readlines():
        if skipFirstLine:
            skipFirstLine = False
            continue

        runTime, notUsed, newState = line.split()
        while position < int(runTime):
            position += tickInterval
            if not waitingForStart:
                currentString += currentState

                if len(currentString) == BYTE_SIZE:
                    asciiChars.append(chr(int(swapEndianness(currentString),2)))
                    currentString = ""
                    waitingForStart = True

            else:
                if (prevState == "1") and (currentState == "0"):
                    waitingForStart = False

        prevState = currentState
        currentState = newState


print("".join(asciiChars))
