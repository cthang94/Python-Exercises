try:
    fname = input("Please enter a file name: ")
    fhand = open(fname, "r")
    counter = 0
    
    for line in fhand:
        if line.startswith("Subject"):
            counter = counter + 1
    print("There are %d subject lines in the file" % counter)

except:
    if fname.startswith("na na boo boo"):
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit
    else:
        print("Invalid input")
