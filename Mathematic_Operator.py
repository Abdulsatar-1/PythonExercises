Number_1 = int(input("Enter the first number: "))
Number_2 = int(input("Enter the second number: "))

print("\n------ RESULT-------")
# Addition
Addition = Number_1 + Number_2;
print("Additional Result is: ",Addition)

# Multiplication
Multiplication = Number_1 * Number_2;
print("Multiplication Result is: ",Multiplication)

# Substraction
Subtraction = Number_1 - Number_2;
print("Subtraction Result is: ",Subtraction)

# Division
Division = Number_1 / Number_2
print("Division Result is: ", Division)

# Modulo
if Number_1 % Number_2 == 0:
    print(f"The number {Number_1} is divisible by {Number_2}")
else:
    print(f"The number {Number_1} is not divisible by {Number_2}")

# Exponentiaton
Exponentiaton = Number_1 ** Number_2;
print("Exponentiaton Result is: ", Exponentiaton)

# Floor_divison
Floor_divison = Number_1 // Number_2;
print("Floor_divison Result is: ", Floor_divison)
