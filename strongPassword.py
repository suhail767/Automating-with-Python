#! python3
#strongPassword.py - Checks whether a password is strong or not

import re

password = input()
length = len(password)


isCapital = re.compile(r'[A-Z]+')
mo1 = isCapital.findall(password)

isLower = re.compile(r'[a-z]+')
mo2 = isLower.findall(password)

isDigit = re.compile(r'[0-9]+')
mo3 = isDigit.findall(password)

a =(len(mo1))
b =(len(mo2))
c =(len(mo3))




if (a==b==c>=1) and (length>=8):
    print('Password is Strong')

else:
    print('''Password Should contain upper and lower case
        along with atleast one digit.''')


