fhand = open("mbox-short.txt")
dictionaryOfEmails = dict()
counter = 0
largest = None
smallest = None

for line in fhand:
    if line.startswith("From"):
        words = line.split()

        if len(words) > 2:
            continue

        days = words[1]

        if days not in dictionaryOfEmails:
            dictionaryOfEmails[days] = 1

        else:
            dictionaryOfEmails[days] += 1

##        if largest is None or dictionaryOfEmails[days] > largest:
##                largest = dictionaryOfEmails[days]
##print("The largest number of emails is: ", largest)

            largest = max(dictionaryOfEmails, key=dictionaryOfEmails.get)
print(largest, dictionaryOfEmails[largest])
print(dictionaryOfEmails)
