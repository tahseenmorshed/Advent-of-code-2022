file = open("values.txt", "r")

startIndex = 0
endIndex = 4

for line in file.readlines():
    lineLength = len(line)
    print(lineLength)
    window = line[startIndex:endIndex]
    print("First window = ", window)

    endIndex = endIndex + 1
    for endIndex in range(endIndex, lineLength, 1):
        startIndex = startIndex + 1
        window = line[startIndex:endIndex]
        print("Current window ", window)

        windowLength = len(window)
        for currLetterIndex in range(0, windowLength, 1):
            print("Current letter ", window[currLetterIndex])
            #currLetter = window[currLetterIndex]

            if window.count(currLetter) >= 2:
                print("Found")