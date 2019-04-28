import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generatePassword(password):
    '''
    Generate Fernet-key with your string password
    '''
    password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes(password),
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    return f

def encrypt(fer, text):
    '''
    Encrypt your string
    '''
    token = fer.encrypt( text.encode() )
    return token

def decrypt(fer, text):
    '''
    Decrypt your string
    '''
    token = fer.decrypt( text.encode() )
    return token

def OpenFile(file, fer):
    with open(file, 'rb') as f:
        decrypted = fer.decrypt(f.read())
    return decrypted.decode()

def WriteFile(file, encryptedTest):
    with open(file, 'wb') as f:
        f.write( encryptedTest )

