# user_num = int(input("Enter a Integer number: "))
#
# if user_num < 0:
#     print("The number u entered is less than 0")
# elif user_num == 0:
#     print("The number u entered is 0")
# elif 0 < user_num <= 100:
#     print("The number u entered can be 1,100 or anything between 1 and 100 ")
# else:
#     print("The number u entered is greater than 100")


# Roman Numeral Equivalent
from random import randint

one_to_ten = randint(1, 10)

if one_to_ten == 1:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")