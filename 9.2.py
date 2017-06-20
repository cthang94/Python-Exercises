import string

fhand = open("mbox-short.txt")
dictionaryOfDays = dict()
count = 0


for line in fhand:
    if line.startswith("From"):
        words = line.strip("\n")
        words2 = words.split()

        if len(words2) > 3:
            days = words2[2]
            print(days)
            count += 1

            if days not in dictionaryOfDays:
                dictionaryOfDays[days] = 1

            else:
                dictionaryOfDays[days] += 1

print(dictionaryOfDays)
