import getpass
import time
import sys
import shutil

#Custom Libs
import pyotp

import crypt
import FileWork as fw

### My fucntions here starts
def help():
    teer()
    print("1 - add\n2 - del\n3 - change\n4 - get\n\n9 - exit")
    teer()

def add(pswd):
    '''
    Add codes to codes.enc
    '''
    name = input("Enter name of new service: ")
    secure_code = input("Secure code: ")
    codes = fw.OpenJson("codes", pswd)
    codes[name] = secure_code 
    fw.SaveJson("codes", codes, pswd)
    totp = pyotp.TOTP(secure_code)
    print("Current code:", totp.now())

def delete(codes, pswd):
    teer()
    print("WARNING!\nTHIS ACTION MAY DELETE YOUR SECURE DATA\nPLEASE BE CAREFUL")
    teer()
    time.sleep(1)
    print("Enter name service that you want to delete:\n")
    service_name = input()
    if service_name not in codes:
        print("This key is not in the codes.enc")
    else:
        print("Are you sure want to delete %s ?" % service_name.upper() )
        ans = input()
        if ans == "yes" or ans == "y":
            shutil.copy2(r'codes.enc', r'codes.enc.OLD')
            del codes[service_name]
            fw.SaveJson("codes", codes, pswd)
            teer()
            print("Succeful delete!")
    teer()

def change(codes):
    pswd_new = getpass.getpass("Enter new password: ")
    pswd_new_second = getpass.getpass("Repeat your new password: ")
    if pswd_new != pswd_new_second:
        print("Passwords do not match")
    else:
        fw.SaveJson("codes", codes, pswd_new)
        print("Succeful password change")
    teer()

def get(codes):
    service_name = input("Enter name of service: ")
    if service_name in codes:
        secure_code = codes[service_name]
        totp = pyotp.TOTP(secure_code)
        print(service_name + ": " + totp.now())
    teer()

def getValues(pswd):
    teer()
    print("Youre services:\n")
    codes = fw.OpenJson("codes", pswd)
    for code in codes:
        print(code)
    teer()
    return codes

def teer():
    s = "\n--------------------"
    print(s + "\n")

### My functions here ends(?)



teer()
pswd = getpass.getpass("Enter password: ")
help()
codes = getValues(pswd)

while True:
    print("Enter command:\n")
    cmd = input()
    if cmd == "add" or cmd == "1":
        add(pswd)
        getValues(pswd)
    if cmd == "del" or cmd == "2":
        delete(codes, pswd)
        getValues(pswd)

    if cmd == "change" or cmd == "3":
        change(codes)
        sys.exit()

    if cmd == "get" or cmd == "4":
        get(codes)

    if cmd == "exit" or cmd == "ex" or cmd == "9":
        print("~~~~~~ GoodBye ~~~~~~")
        sys.exit()