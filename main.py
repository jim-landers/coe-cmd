import sys
import requests
import webbrowser

from auth_management import *

JB_BASE_ASSET_URL  = 'https://support.engineering.oregonstate.edu/Assets/Edit{}'
COETOOL_BASE_URL   = 'https://tools.engr.oregonstate.edu/coetools/jitbit/?name={}'
CYDER_BASE_URL     = 'https://cyder.oregonstate.edu/search/?search={}'
ACTLOG_BASE_URL    = 'https://tools.engr.oregonstate.edu/coetools/lablogs/labinfo.php?hostname={}'


def JB_GetAssetJSON(assetName: str):
    assetURL = COETOOL_BASE_URL.format(assetName)
    headers = {
        'Authorization' : 'Basic ' + credentials.auth
    }

    req = requests.get(assetURL, headers=headers)
    return req.json()


def JB_OpenAssetPage(assetName: str):
    assetJSON = JB_GetAssetJSON(assetName)
    assetID   = assetJSON[0]['ItemID']
    assetURL  = JB_BASE_ASSET_URL.format(f"/{assetID}")

    OpenPage(assetURL)


def CYDER_OpenSearch(assetName: str):
    URL = CYDER_BASE_URL.format(assetName)
    OpenPage(URL)


def ACTLOG_OpenLog(assetName: str):
    URL = ACTLOG_BASE_URL.format(assetName)
    OpenPage(URL)


def OpenPage(URL: str):
    print(f"Opening {URL}...")
    webbrowser.open(URL)


def PrintHelp():
    print()
    print('Current list of supported flags: ')
    print('---------------------------------')
    print('#    jb/jitbit <MachineName>')
    print('#    cy/cyder <MachineName>')
    print('#    al/activitylog <MachineName>')
    print()


def main():
    if len(sys.argv) != 3:
        PrintHelp()
        return

    if not CredentialsExist():
        CreateCredentials()

    if credentials.auth == '':
        print("Credentials cannot be blank (edit or remove credentials.py)")
        return

    command   = sys.argv[1]
    assetName = sys.argv[2]

    if command == 'jb' or command == 'jitbit':
        JB_OpenAssetPage(assetName)
    elif command == 'cy' or command == 'cyder':
        CYDER_OpenSearch(assetName)
    elif command == 'al' or command == 'activitylog':
        ACTLOG_OpenLog(assetName)
    else:
        PrintHelp()

if __name__ == '__main__':
    main()