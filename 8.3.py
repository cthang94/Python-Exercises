fhand = open("mbox-short.txt", "r")
count = 0

for line in fhand:
    words = line.split()
    #print("Debug:", words)
    if len(words) != 0 and len(words) >= 3 and words[0] == "From":
        print(words[2])
        
