fhand = open("mbox-short.txt")
dictionaryOfEmails = dict()
counter = 0

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
print(dictionaryOfEmails)
