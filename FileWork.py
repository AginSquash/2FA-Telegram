import crypt
import json

def SaveJson(name, data, password):
    key = crypt.generatePassword(password)
    encrypted = crypt.encrypt(key, json.dumps(data) )
    crypt.WriteFile('%s.enc' % name, encrypted)

def OpenJson(name, password):
    key = crypt.generatePassword(password)
    data = crypt.OpenFile('%s.enc' % name, key)
    j = json.loads( data )
    return j