def calculate():      # define a function named calculate
    total = 0         # set total/count/average variables to zero
    count = 0
    average = 0
    while True:      # Constantly asks user for a number
        number = input("Please enter a number: ")
        if number == ("done"):   # if user types in "done"
            print("Done!")      # python yells out done when user inputs done
            print(total, count, (average))   # python shows total, count, and total/count
            break       # exit out of the loop
        else:   # if else user types in something other than done
            try:  # do this with user input
                count = count + 1   #keep counting how many values the user inputs
                total = total + float(number)
            except:    # user types in something other than a number
                print("Invalid input!")   #print this out
                continue   # go back to the top (while loop)
            average = (total/count)
        

calculate()  #call the function
