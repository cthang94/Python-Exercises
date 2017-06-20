def calculate():
    biggest = None
    smallest = None
    n = 0

    while n < 5:
        numbers = float(input("Please enter a number: "))
        n += 1
        if smallest is None or numbers < smallest:
            smallest = numbers
        elif biggest is None or numbers > biggest:
            biggest = numbers
    print("The smallest number is: ", smallest)
    print("The biggest number is: ", biggest)

calculate()
