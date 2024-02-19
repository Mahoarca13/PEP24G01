# dictionary


my_dict = {'one': 1, 'two': 2, 'true': True}

print(my_dict)
print(type(my_dict))

my_dict = dict(one=1, two=2)
print(my_dict)

for element in my_dict:  # same as my_dict.keys()
    print('dict key:', element)
for element in my_dict.values():
    print('dict key:', element)
for element in my_dict.keys():
    print('dict key:', element)
for element in my_dict.items():
    print('dict key:', element)
for key, values in my_dict.items():
    print('dict key:', key, values)

# test = {[1]: 'test'}
# print(test)

# Tuple

a, b = (1, 2) # same as 1, 2 se pun paranteze ca e mai usor de citit, daca ai un singur element se pune elementul urmat cu virgula

print(a)
print(b)

a, b = b, a
print(a)
print(b)

#not like this
# a=b
# b=a
# print(a)
# print(b)

#get key/values

value = my_dict['one']
print(f'returned value is: {value}')
value = my_dict['one'] = '''one'''
print(f'returned value is: {value}')

