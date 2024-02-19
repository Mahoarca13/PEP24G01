def suma(number_list):
    return sum(number_list)

def medie(lista: list):



def putere(number_list):
    for number in number_list:
        result.append(number ** 2)


meniu = {
    "1": medie,
    "2": suma,
    "3": putere
}
num_list = []
while True:
    number = input('Type a number: ').lower()
    if number == 'x':
        break
    try:
        number = float(number)
    except Exception:
        print('Invalid number. Type again: ')
        continue

    num_list.append(number)

methods_dict = {1: 'Media numerelor', 2: 'Suma numerelor', 3: 'Puterea numerelor', 4: 'Iesire'}
for option_number, option_name in methods_dict.items():
    print(f'{option_number}, {option_name}')
choice = input('Introduceti optiunea dvs: ')
result = meniu.get(choice)(num_list)
print(f'Rezultatul: {result}')

