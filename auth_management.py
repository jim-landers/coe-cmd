import base64
import getpass

import credentials

from pathlib import Path

def CredentialsExist() -> bool:
    creds = Path("credentials.py")
    if not creds.is_file():
        return False
    
    contents = credentials.auth
    return len(contents) > 0

def CreateCredentials():
    print("No credentials found; provide them below")
    username = input("Username: ")
    password = getpass.getpass()
    concat = username + ':' + password
    b64 = base64.b64encode(concat.encode())
    with open('credentials.py', 'w') as creds:
        creds.write("auth=\"" + b64.decode('utf-8') + "\"")

def ReadCredentials():
    return credentials.auth