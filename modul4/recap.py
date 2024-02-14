#check one of the following chars are in the string

my_str = "abcd1232"
check_chars = ['2', '!']

for char_ in check_chars:
    if char_ in my_str:
        print(f'success found: {char_}')
        break
else:
    print(f'Could not find any char in: {check_chars}')


