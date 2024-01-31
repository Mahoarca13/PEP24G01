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

print(80 * '#')
#len function

ex1 = 'example1'
print(len(ex1))


print(80 * '#')
#index of a string

hello = 'hello world'
        #012345678910
print(hello[2])
print(hello[3:7])  #last index not included
print(hello[0:10:2])  #last index not included
print(hello[0:12:2])  #not all versions of python 3
print(hello[::2])  #nu specifici unde incepe si unde se termina pt a cuprinde tot textul
print(hello[:len(hello):2])
#hello = 'h e l l o  w o r l d '
#                -3 -2 -1
print(hello[::-1])  #sirul va fi printat invers
print(hello[-5:-1:]) #pazul pozitiv 1 este implicit
print(hello[::-1])
hello = 'hello world'
print(hello[-5::1])
print('negative step')
print(hello[-5:-10:-1])