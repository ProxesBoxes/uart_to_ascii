fileName = "./async_out.ctf"
state = ""
position = 0
tickInterval = 10
binaryString = ""
skipFirstLine = True
BYTE_LEN = 8

with open(fileName, "r") as analogFile:
    for line in analogFile.readlines():
        if skipFirstLine:
            skipFirstLine = False
            continue

        runTime, notUsed, newState = line.split()
        while position < int(runTime):
            binaryString += state
            position += tickInterval
        state = newState

print(' '.join(binaryString[i:i+BYTE_LEN] for i in range(0,len(binaryString),BYTE_LEN)))
