finput = input("Please enter a file name: ")
fhand = open(finput)
count = 0

for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words) > 2:
            print(words[1])
            count += 1
print("Counter is: ", count)
