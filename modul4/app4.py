def check_password():
    required_chars = ['!', '@', '%']
    password = input("Introducti parola: ")
    if len(password) < 7:
        print('Parola cu lungime gresita')
        check_password()
    for character in required_chars:
        if character in password:
            break


    else:
        print('Parola trebuie sa contina: ! @ %')


check_password()

