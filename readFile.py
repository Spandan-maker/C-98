text = "Hi, I am Coding"
print(text.split())

#---------------------------------------------------

file = open("text.txt")
fileLines = file.readlines()

for i in fileLines:
    print(i)