word = ("tyrannosaurus")
d = dict()

for letter in word:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] = d[letter] + 1
print(d)
