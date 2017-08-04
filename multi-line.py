numberOfLines = input("How many lines? ")
whatGoesOnEachLine = input("What do you want on each line? ")


def printmultiline(howmanylines, whattotype):
    for i in range(0, int(howmanylines)):
        print(whattotype)

printmultiline(numberOfLines, whatGoesOnEachLine)
