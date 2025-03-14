# GPA = float(input("What was the appplcan's GPA? "))
# inst_app = input("Is the student going to be educatedat an approved instution y/n ? ")
#
# if GPA >= 3.7:
#     if inst_app == "y":
#         print("The Student is qualifies for a loan")
#     else:
#         print("The Student is not qualifies for a loan")
# else:
#     print("The student did not have hight degree qualification")


# Grade Determiner
score = int(input("Please enter the student's score. "))

if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score >= 80:
        print("This student's score of " + str(score) + " is a B.")
    else:
        if score >= 70:
            print("This student's score of " + str(score) + " is a C.")
        else:
            if score >= 60:
                print("This student's score of " + str(score) + " is a D.")
            else:
                print("This student's score of " + str(score) + " is a F.")