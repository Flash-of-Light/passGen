#!/usr/bin/env python3

import random
import string

string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
random.choice(string.ascii_letters)
# print(random.choice(string.ascii_letters))

random.randint(0,9)
# print(random.randint(0,9))

random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '='])
# print(random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=']))

def pwtype():
    pwtype.Type = input("Create your password. Type 1 for alphanumeric only and 2 to include symbols.")
def pwlength():
    pwlength.Length = input("Choose the character length.")
pwtype()
pwlength()
# print(pwlength.Length)
if pwtype.Type == str(1):
    i=0
    pw = ''
    while (i < int(pwlength.Length)):
        x = random.randint(0,1)
        if x == int(0):
            pw = pw + str(random.choice(string.ascii_letters))
            i+=1
        elif x == int(1):
            pw = pw + str(random.randint(0,9))
            i+=1
    print(str(pw))
elif pwtype.Type == str(2):
    i=0
    pw = ''
    while (i < int(pwlength.Length)):
        x = random.randint(0,2)
        if x == int(0):
            pw = pw + str(random.choice(string.ascii_letters))
            i+=1
        elif x == int(1):
            pw = pw + str(random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=']))
            i+=1
        elif x == int(1):
            pw = pw + str(random.randint(0,9))
            i+=1
    print("Here is your randomly generated password: " + str(pw))
