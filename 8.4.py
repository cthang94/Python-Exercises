finput = input("Please enter a file name: ")
fhand = open(finput)
romeoList = []

for line in fhand:
    words = line.split()
    for word in words:
        if word in romeoList:
            continue
        else:
            romeoList.append(word)
romeoList.sort()
print(romeoList)

