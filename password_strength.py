
import re


def password_blacklist(filepath):
    black_list = re.findall('\w+', open(filepath).read())
    return black_list


def get_password_strength(password):
    password_strenght = 1
    if len(password) > 10:
        password_strenght += 2
    if re.findall('\d', password):
        password_strenght += 1
    if re.findall('[!@#$%^&*()_+№,.]', password):
        password_strenght += 2
    if password.lower() != password and password.upper() != password: 
        password_strenght += 2
    if password not in (password_blacklist(filepath)):
        password_strenght += 2 
    return password_strenght     


if __name__ == '__main__':
    filepath = input("Введите путь к файлу черного списка паролей\n")
    password = input("Введите пароль\n")
    if password == '':
        print ('Вы не ввели пароль')
    else:    
        print (get_password_strength(password))
