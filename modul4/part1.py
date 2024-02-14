# result = 1
# def factorial(x):
#     global result
#     for i in range(1, x+1):
#         result *= i
#
# factorial(4)
# print(result)
result = 0
def gauss(n):
    global result
    #result = 0
    for i in range(1, n+1):
        result += i
gauss(100)
print(result)

