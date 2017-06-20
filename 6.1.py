animal = ("wolf") # make a string named animal with value of wolf
n = len(animal)    # make the length of string animal go inside n

while n > 0:      # while n is greater than 0, n starts at 4
    letter = animal[n-1]   # reverse the string and make it go inside letter
    print(letter)   # print out what the previous statement does
    n = n - 1   # subtract by n to keep looping
