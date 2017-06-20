#5.4 Infinite loops and break

while True:
    line = input("Enter name: ")
    if line == "done":
        break
    print (line)
print("Done")
