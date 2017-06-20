try:
    score = input("Please enter a score: ")
    score = float(score)

    if score >= 0.9:
        print("You have an A with a score of ", score)
    elif score >= 0.8 and score < 0.9:
        print("You have an B with a score of ", score)
    elif score >= 0.7 and score < 0.8:
        print("You have an C with a score of ", score)
    elif score >= 0.6 and score < 0.7:
        print("You have an D with a score of ", score)
    elif score < 0.6:
        print("You have an F with a score of ", score)
except:
    print("Invalid input!")
