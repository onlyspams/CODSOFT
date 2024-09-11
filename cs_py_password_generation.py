# -*- coding: utf-8 -*-
"""cs_py_password_generation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B33oVcYFbeeqivOPYU2kljkyn6ezBoMc
"""

import random
import string

def generate_pass(length , complexity):
    if complexity == 1:
        passcode = string.ascii_letters

    elif complexity == 2:
        passcode = string.ascii_letters + string.digits

    elif complexity == 3:
        passcode = string.ascii_letters + string.digits + string.punctuation

    else:
        print("Wrong Input")

    return ''.join(random.choices(passcode, k = length))


length = int(input("Enter the length of password \n"))
com = int(input("Enter the complexity between 1 and 3 \n"))
print(generate_pass(length,com))