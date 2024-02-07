duplicated = [1, 3, 5, 7, 7, 7, 7, 7, 9, 3]  # remove duplicates

new_list = []
for number in duplicated[::]:    #tot timpul incercati sa copiati o lista inainte da face modificari pe lista respectiva
    if number not in new_list:
        new_list.append(number)
    else:
        duplicated.remove(number)
        print(number, 'number is duplicate')
    duplicated.sort()

print(new_list)
print(duplicated)
