#TASK----------------------------------------------------------------------------------------------------------
def userInput(name):
    file = open(name)
    count = 0

    for i in file:
        word = len(i.split())
        count = count + word

    print(count)


userInput("text.txt")