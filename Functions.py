# Defining Function
# def function_name():
#     print(2 + 2)
#
# function_name()

# Parameter
# def function_name(parameter):
#     print(parameter + 2)
#
# function_name(8)



# Multiple Parameter
# first_str = "The Number "
#
# def function_name(p1, p2, p3):
#     print(p1 + str(p2) + p3)
#
# function_name(first_str, 5, " is an integer")



# Default Parameter
# def default_example(num1=7,num2=8):
#     print(num1 * num2)
#
# default_example()   # RESULT = 56
# default_example(2)  # RESULT = 16, replacing 7 with 2 and keep 8 as default
# default_example(4 , 6)  # RESULT = 24, replacing 7 with 4 and  8 with 6



# Return
# def default_example(num1=7,num2=8):
#     return num1 * num2
#
# print(default_example() + 44)


# Volume of a Rectangular Prism
# length = int(input("Enter an integer that represents length in feet: "))
# width = int(input("Enter an integer that represents width in feet: "))
# height = int(input("Enter an integer that represents height in feet: "))
#
#
# def prism_vol(l, w, h):
#     return l * w * h
#
#
# print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")

# Celsius to Fahrenheit
# celsius = int(input("Please enter an integer value for degrees celsius: "))


# def fahrenheit(cel):
#     # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
#     # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
#     # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
#     # temperature.
#     return (18 * cel + 320) / 10
#
#
# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)))


# Celsius to Fahrenheit Solution with round()
# celsius = int(input("Please enter an integer value for degrees celsius: "))
#
#
# def fahrenheit(cel):
#     # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
#     # after the decimal point
#     return round((1.8 * cel + 32), 1)
#
#
# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)))


# Generic Imports
# import random
# print(random.randint(1, 25))

# # Function Imports
# from random import randint
# print(randint(1, 25))

# Universal Imports
# from random import *
# print(random())


# Miles Per Gallon
from random import randint
# generates random integer between and inclusive of 10 and 25 to represent gas in the car's fuel tank
fuel = randint(10, 25)
# generates random integer between and inclusive of 200 and 400 to represent miles the car can go without refueling
miles = randint(200, 400)
# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")