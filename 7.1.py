
fname = input("Please enter a file name: ")
fhand = open(fname)
fhand = fhand.read()
text = str.upper(fhand)
print(text)
    
