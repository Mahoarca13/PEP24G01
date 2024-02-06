# print(23 * '#', 'Equality: the equal to operator', 23 * '#')  # Equality: the equal to operator
# var = 0  # Assigning 0 to var
# var2 = var == 0  # assigning the result to another variable
# print(var2)  # result will be true because 0 is equal to 0
#
# var = 1  # Assigning 1 to var
# var3 = var == 0  # assigning the result to another variable
# print(var3)  # result will be false because 1 is  not equal to 0
#
# print(20 * '#', 'Inequality: the not equal to operator', 20 * '#')  # Inequality: the not equal to operator
# var = 0  # Assigning 0 to var
# var4 = var != 0  # assigning the result to another variable
# print(var4)  # result will be false because 0 is not different than 0
#
# var = 1  # Assigning 1 to var
# var5 = var != 0  # assigning the result to another variable
# print(var5)  # result will be true because 1 is different than 0
#
# print(20 * '#', 'Comparison operators: greater than', 20 * '#')  # Comparison operators: greater than
# black_sheep = 10
# white_sheep = 5
# sheep1 = black_sheep > white_sheep
# print(sheep1)
#
# print(20 * '#', 'Comparison operators: greater than or equal to',
#       20 * '#')  # Comparison operators: greater than or equal to
# black_sheep = 10
# white_sheep = 8
# sheep2 = black_sheep >= white_sheep
# print(sheep2)
#
# print(20 * '#', 'Comparison operators: less than', 20 * '#')  # Comparison operators: less than
# black_sheep = 8
# white_sheep = 10
# sheep3 = black_sheep < white_sheep
# print(sheep3)
#
# print(20 * '#', 'Comparison operators: less than or equal to',
#       20 * '#')  # Comparison operators: less than or equal to
# black_sheep = 8
# white_sheep = 8
# sheep4 = black_sheep <= white_sheep
# print(sheep4)

# how to identify the larger of two numbers:

# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)
#
# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)
#
# # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1
#
# # We check if the second number is larger than current largest_number
# # and update largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
#
# # We check if the third number is larger than current largest_number
# # and update largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
#
# # Print the result
# print("The largest number is:", largest_number)

# # Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.
#
# largest_number = max(number1, number2, number3)
#
# # Print the result.
# print("The largest number is:", largest_number)

# #Scenario
#
# #Spathiphyllum

# floare = input('Intoduceti nume floare: ')
# if floare == 'Spathiphyllum':
#     print('"Spathiphyllum is the best plant ever!"')
# elif floare == 'spathiphyllum':
#     print('No, I want a big Spathiphyllum!')
# else:
#     print('Spathiphyllum! Not:', floare)


# #tax collector
# income = float(input("Enter the annual income: "))
#
# if income <= 85528:
#     tax = (income * 0.18) - 556.2
#     print(tax)
#     if tax < 0:
#         tax = 0
# elif income > 85528:
#     tax = (income - 85528) * 0.32 + 14839.2
#     print(tax)
#
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

# #Year calculator

