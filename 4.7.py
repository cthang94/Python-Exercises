
def computegrade(score):
    try:
        
        score = input("Enter a score: ")
        score = float(score)
        if score >= 0.9:
            grade = ("A")
            return grade
        elif score >= 0.8 and score < 0.9:
            grade = ("B")
            return grade
        elif score >= 0.7 and score < 0.8:
            grade = ("C")
            return grade
        elif score >= 0.6 and score < 0.7:
            grade = ("D")
            return grade
        elif score < 0.6:
            grade = ("F")
            return grade
    except:
            print("Invalid input!")

compute = computegrade(.1)
print (compute)
