# 5.5 Finishing Iterations with Continue

while True:
    line = input("What is your name?")
    if line[0] == ("#"):
        continue
    if line == ("Done"):
        break
    print (line)
print("Done")
