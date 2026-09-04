empty = ""
print("UNWEIGHTED GPA CALCULATOR FOR EDISON")
print(empty)
course_amount = input("How many classes are you taking? (max 10):")
print(empty)
if course_amount.isdigit():
    course_amount = int(course_amount)
yes = "y"
no = "n"
yes_no = input("Is this right: " + str(course_amount) + " classes? (y/n):")

while yes_no == no:
    course_amount = input("How many classes are you taking? (max 10):")
    print(empty)
    if course_amount.isdigit():
        course_amount = int(course_amount)
    yes_no2 = input("Is this right:" + "" + str(course_amount) + " classes? (y/n):")
    yes2 = yes_no2.lower() == "y"
    no2 = yes_no2.lower() == "n"
    if yes2 == True:
        break
    print(empty)

if yes_no == yes:
    print(empty)
A_plus_grade = "A+"
A_grade = "A"
A_minus_grade = "A-"
B_plus_grade = "B+"
B_grade = "B"
B_minus_grade = "B-"
C_plus_grade = "C+"
C_grade = "C"
C_minus_grade = "C-"
D_grade = "D"
F_grade = "F"

print("Please enter your grades for each class. (A+, A, A-, B+, B, B-, C+, C, C-, D, or F)")
print(empty)
class_1_grade = input("class 1: ") if course_amount >= 1 else None
class_2_grade = input("class 2: ") if course_amount >= 2 else None
class_3_grade = input("class 3: ") if course_amount >= 3 else None
class_4_grade = input("class 4: ") if course_amount >= 4 else None
class_5_grade = input("class 5: ") if course_amount >= 5 else None
class_6_grade = input("class 6: ") if course_amount >= 6 else None
class_7_grade = input("class 7: ") if course_amount >= 7 else None
class_8_grade = input("class 8: ") if course_amount >= 8 else None
class_9_grade = input("class 9: ") if course_amount >= 9 else None
class_10_grade = input("class 10: ") if course_amount >= 10 else None
print (empty)

A_plus_grade = 4.0
A_grade = 4.0
A_minus_grade = 3.7
B_plus_grade = 3.3
B_grade = 3.0
B_minus_grade = 2.7
C_plus_grade = 2.3
C_grade = 2.0
C_minus_grade = 1.7
D_plus_grade = 1.3
D_grade = 1.0
D_minus_grade = 0.7
F_grade = 0.0

Final_GPA = int((class_1_grade + class_2_grade + class_3_grade + class_4_grade + class_5_grade + class_6_grade + class_7_grade + class_8_grade + class_9_grade + class_10_grade) / course_amount)

print("Your GPA" + "(4.0)" + "is: " + str(Final_GPA))