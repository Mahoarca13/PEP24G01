# string format

# method format

my_str = "test {}"
print(my_str.format('''example'''))
my_str = "test {1} {0}"
print(my_str.format('example1', 'example2'))
my_str = "test {ex1} {ex2}"
print(my_str.format(ex1='example1', ex2='example2'))
my_str = "test {}"
print(my_str.format(2))

print(80 * '#')
# formatted string
ex1 = 'example1'
ex2 = 'example2'
print(f"text2 {ex1}")
print(f"text2 {2}")
print(f"text2 {ex1} {ex2} {ex1}")