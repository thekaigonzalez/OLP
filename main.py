import hashlib
import os
import string
import sys

def generate_password(
    len): 
    """
    Generates a password

    When this algorithm is run, it will use a range with 1-9, [a-Z], and extra symbols, and create
    an array based on that string, then it will check the length, and continue adding random characters from the
    character array.
    
    """
    import random

    length = 0
    rand = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    rage = [ch for ch in rand]
    gen = ""


    while (length < len):
        gen += random.choice(rage)
        length += 1

    return gen

def save_password_hash(string):
    """
    Saves the password to the user's home directory in .olp-passwords 
    as a hash.
    """
    open(os.path.expanduser("~/.olp-passwords"), "a").write(": password : " + string[0:2] + "... : " + str(hashlib.sha1(string.encode("utf-8")).hexdigest() + "\n"))

# variables controlled by args
save = False
length = 15

# parse args
for i in sys.argv:
    if (i == '--save' or i == '-s'):
        print("saving password")
        save = True
    elif i.startswith("-l"):
        length = int(i[2:] if len(i[2:]) > 0 else "15")
        

    
passwd = generate_password(length)

print(passwd)

if (save):
    save_password_hash(passwd)


    