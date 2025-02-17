# Purpose: grading system
marks = float(input("Enter total mark scored"))
scoring= marks/500 * 100
if (scoring >= 90):
    print("A")
elif(scoring < 90 and scoring >=80):
    print("B")
elif(scoring < 80 and scoring >=70):
    print("C")
elif(scoring < 70 and scoring >=60):
    print("D")
else:
    print("try hard next time")