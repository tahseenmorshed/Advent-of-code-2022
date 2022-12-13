file = open("values.txt", "r")

startIndex = 0
endIndex = 3
finalIndex = 0

for line in file.readlines():
    lineLength = len(line)
    print(lineLength)

    for endIndex in range(endIndex, lineLength, 1):
        window = line[startIndex:endIndex + 1]
        print("Current window ", window)
        startIndex = startIndex + 1

        windowLength = len(window)
        numUniqueLetters = 0
        for currLetterIndex in range(0, windowLength, 1):
            currLetter = window[currLetterIndex]
            print(currLetter, " start index ", startIndex, " end index ", endIndex)

            if window.count(currLetter) == 1:
                numUniqueLetters = numUniqueLetters + 1

        if numUniqueLetters == 4:
            print("Found")
            finalIndex = endIndex
            break
            
        uniqueLetters = 0

print("Final index is ", finalIndex + 1)