import string
import random

def Gen():
    str1 = string.ascii_uppercase
    str2 = string.ascii_lowercase
    str3 = string.digits
    str4 = string.punctuation

    password_length = int(input("Enter the Length of Password:\n"))

    s = []

    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))

    random.shuffle(s)

    password = ("".join(s[0:password_length]))

    print(password)

Gen()