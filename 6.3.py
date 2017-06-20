def count(string, letter):
    counter = 0

    for n in string:
        if n == letter:
            counter = counter + 1
    return counter

x = count("apples", "p")
print(x)
