fhand = open("mbox-short.txt")
delimiter = "@"
dictionaryOfDomains = dict()

for line in fhand:
    if line.startswith("From"):
        split_line = line.split()
        if len(split_line) > 2:
            continue
        else:
            index_one = split_line[1]
            index_two = index_one.split("@")
            domain = index_two[1]

            if domain in dictionaryOfDomains:
                dictionaryOfDomains[domain] += 1
            else:
                dictionaryOfDomains[domain] = 1
print(dictionaryOfDomains)
