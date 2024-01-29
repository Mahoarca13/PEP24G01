#copararea numerelor - problema 2
password = 7710
user_pass = input('Enter Password: ')
print(user_pass)
#rezultatul va fi fals deoarece primul e vazut ca numar al 2-lea e vazut ca string fara o transformare
# daca -> print(password == user_pass) rezultatul va fi totimpul fals indiferent de ce introduci
print(str(password) == user_pass) # primul e facut string pentru a compara string cu string
print(password == int(user_pass)) # al 2-lea e facut numar din string pentru a compara numar cu numar