fname = input("Please enter a file name: ")
fhand = open(fname, "r")
counter = 0
total = 0
average = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        newLine = line.split()
        newLine2 = float(newLine[1])
        counter += 1
        total = newLine2 + total
        
print(total / counter)
        
