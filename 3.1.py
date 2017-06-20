hours = float(input("Enter Hours: "))  #will put user input value into hours variable
rate = float(input("Enter rate: ")) #will put user input value into rate variable
overtimePay = int(0)
overtimeHours = int(0)


if hours <= 40:
    pay = rate * hours #computes rate and hours into pay
    print("The price is $", pay) #displays the total pay for under/equal to 40 hours
else:    #checks if the hours is greater than 40
    overtimeHours = hours - 40     #see how many overtime hours are there
    overtimePay = (rate * 1.5) * overtimeHours    #calculates payment for overtime hours
    pay = (hours - overtimeHours) * rate + overtimePay
    print(pay)





