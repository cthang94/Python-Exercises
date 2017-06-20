def computepay(hours, rate):

    if hours > 40:
        overtimeHours = hours - 40
        overtimeRate = rate * 1.5 * overtimeHours
        overtimePay = (hours - overtimeHours) * rate + overtimeRate
        overtimePay = float(overtimePay)
        return overtimePay
    else:
        pay = hours * rate
        pay = float(pay)
        return pay
        
compute = computepay(20,2)
print("The total payment is: ", compute)
        
        
