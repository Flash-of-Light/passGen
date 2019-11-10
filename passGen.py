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
    pwtype.Type = input("Create your password. Type 1 for alphanumeric and 2 for alphanumeric with symbols.")
def pwlength():
    pwlength.Length = input("Choose the character length.")
type()
# print(pwType)
# print(pwLength)
if pwtype.Type == "1":
    print("yes1")
else pwtype.Type == "2":
    print("yes2")
