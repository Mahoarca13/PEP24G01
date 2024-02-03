print(23 * '#', 'Equality: the equal to operator', 23 * '#')  # Equality: the equal to operator
var = 0  # Assigning 0 to var
var2 = var == 0  # assigning the result to another variable
print(var2)  # result will be true because 0 is equal to 0

var = 1  # Assigning 1 to var
var3 = var == 0  # assigning the result to another variable
print(var3)  # result will be false because 1 is  not equal to 0

print(20 * '#', 'Inequality: the not equal to operator', 20 * '#')  # Inequality: the not equal to operator
var = 0  # Assigning 0 to var
var4 = var != 0  # assigning the result to another variable
print(var4)  # result will be false because 0 is not different than 0

var = 1  # Assigning 1 to var
var5 = var != 0  # assigning the result to another variable
print(var5)  # result will be true because 1 is different than 0

print(20 * '#', 'Comparison operators: greater than', 20 * '#')  # Comparison operators: greater than
black_sheep = 10
white_sheep = 5
sheep1 = black_sheep > white_sheep
print(sheep1)

print(20 * '#', 'Comparison operators: greater than or equal to',
      20 * '#')  # Comparison operators: greater than or equal to
black_sheep = 10
white_sheep = 8
sheep2 = black_sheep >= white_sheep
print(sheep2)

print(20 * '#', 'Comparison operators: less than', 20 * '#')  # Comparison operators: less than
black_sheep = 8
white_sheep = 10
sheep3 = black_sheep < white_sheep
print(sheep3)

print(20 * '#', 'Comparison operators: less than or equal to',
      20 * '#')  # Comparison operators: less than or equal to
black_sheep = 8
white_sheep = 8
sheep4 = black_sheep <= white_sheep
print(sheep4)
