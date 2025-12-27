# students marks/grade calculator

students_grade = float(input("Enter the student's total marks:"))

if  students_grade<40:
    print("you are fail!")
elif students_grade>= 40 and students_grade<50:
    print("you are just passed and your grade is C")
elif students_grade>=50 and students_grade<=70:
    print("you scored good marks! and your grade is B")
elif students_grade>70 and students_grade<=100:
    print("you scored great marks and your grade is A")
else:
    print("your marks is not valid")
