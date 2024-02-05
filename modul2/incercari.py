my_str = "test {}"
print(my_str.format('''example'''))

str1 = "Pluto {1} {0}"
print(str1.format('sapa gradina', 'daca e moale'))

str2 = "Pluto {arg1} si {arg3} daca {arg2}"
print(str2.format(arg1='sapa gradina', arg2='e moale', arg3='scoate trandafirii'))

str3 = "Andreea {1} {1} {2}"
print(str3.format(2, 3, 4))

print(80 * '*')

a = 'sapa gradina'
b = 'daca e moale'
c = 'scoate trandafirii'
d = 'tunde leylandii'
print(f'Pluto {a} {b} si {c}')
print(f'Andreea {c} {b}')
print(f'Petre {a} {b} dupa care {d}')

print(80 * '*')

num = 'Mergem la mare inghesuiala'
print(len(num))

print(80 * '*')

mambo = "Pluto_sapa_gradina1"
# 0123456789-1234567
print(len(mambo))
print(mambo[2])  # printeaza caracterul indicat in [], numaratarea incepe de la 0
print(mambo[2:5])  # printeaza intervalul de la 2 la 5 iar ultimul caracter nu e inclus
print(mambo[0:18:2])  # printeaza intervalul de la 0 la 19 din 2 in 2 ultimul caracter nu e inclus
print(mambo[::2])  # printeaza tot intervalul de la 0 la 19 din 2 in 2, iclude si ultimul caracter
print(mambo[-1])  # printeaza ultimul caracter adica incepe de la coada
print(mambo[::-1])  # printeaza tot sirul invers
print(mambo[-7:-3:])  # printeaza intervalul de la -7 la -3 de la stanga la dreapta
print(mambo[-5::1])  # printeaza de la -5 pana la sfarsit din 1 in 1
print(mambo[-3:-7:-1])  # printeaza intervalul de la -3 a -7 dar invers

print(80 * '*')

# b = int(input('Introduceti valoare baza: '))
# h = int(input('Introduceti valoarea inaltimii: '))
# r = b * h * 0.5
# print(type(r))
# print(f'Aria triunghiului A este: {r}')

print(80 * '*')

# Pass = int(input('Introduceti Parola: '))
# Pass2 = 7710
# Pass3 = Pass == Pass2
# if Pass3:
#     True;
#     print('Parola introdusa este: True')
# else:
#     print('Parola introdusa este: False')
# print(f'Parola introdusa este: {Pass3} ' )
print(80 * '*')

# b = int(input('Introduceti valoare baza: '))
# h = int(input('Introduceti valoarea inaltimii: '))
# r = b * h * 0.5
# print(type(r))
# print(f'Aria triunghiului A este: {r}')
# d = int(r)
# e = d == 7
# if e:
#     True;
#     print('poate ai inteles ceva din if')
# else:
#     print('mai citeste si exerseaza')
print(80 * '*')

a = int(input('Introduceti primul numar: '))
b = int(input('Introduceti al 2-lea numar: '))
print('Media numerelor este:', (a + b)/2)
