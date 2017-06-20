try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))

    if hours > 40:
        overtimeHours = hours - 40
        overtimePay = 1.5 * rate * overtimeHours
        pay = ((hours - overtimeHours) * rate + overtimePay)
        print("The pay with overtime is: ", pay)

    elif hours <= 40:
        pay = hours * rate
        print("The pay is: ", pay)

except:
    print("Invalid input!")
