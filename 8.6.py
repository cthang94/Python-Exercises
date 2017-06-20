def calculate():
    biggest = None
    smallest = None
    userList = []

    while True:
        numbers = (input("Please enter a number: "))
        if numbers == ("done"):
            break
        numbers = int(numbers)
        userList.append(numbers)
        biggest = max(userList)
        smallest = min(userList)

    print("The maximum: ", biggest)
    print("The minimum: ", smallest)


calculate()
