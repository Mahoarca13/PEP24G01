# # # Store the current largest number here.
# # largest_number = -999999999
# #
# # # Input the first value.
# # number = int(input("Enter a number or type -1 to stop: "))
# #
# # # If the number is not equal to -1, continue.
# # while number != -1:
# #     # Is number larger than largest_number?
# #     if number > largest_number:
# #         # Yes, update largest_number.
# #         largest_number = number
# #     # Input the next number.
# #     number = int(input("Enter a number or type -1 to stop: "))
# #
# # # Print the largest number.
# # print("The largest number is:", largest_number)
# # #
#
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
##
# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1,my_list[v])
# print(my_list)
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ** b
# print(c + d + e)
# my_list = [i for i in range(-1, 2)]
# print(my_list)
# var = 0
# while var < 6:
#     var +=1
#     if var % 2 == 0:
#         continue
#     print('#')
# for i in range(1):
#     print('#')
# else:
#     print('#')
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2] [0])
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)
# var1 = [1, 2, 3]
# var2 = []
# for v in var1:
#     var2.insert(0, v)
# print(var2)

# i = 0
# while i <= 3:
#     i += 2
#     print('*')

# t = [[3 - i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 ==0:
#         break
#     print('*')

# var = 1
# while var < 10:
#     print('#')
#     var = var << 1

# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)