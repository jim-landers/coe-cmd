import sys, requests, webbrowser
import creds


JB_BASE_ASSET_URL  = 'https://support.engineering.oregonstate.edu/Assets/Edit{}'
COETOOL_BASE_URL   = 'https://tools.engr.oregonstate.edu/coetools/jitbit/?name={}'
CYDER_BASE_URL     = 'https://cyder.oregonstate.edu/search/?search={}'
ACTLOG_BASE_URL    = 'https://tools.engr.oregonstate.edu/coetools/lablogs/labinfo.php?hostname={}'




def JB_GetAssetJSON(assetName):
    assetURL = COETOOL_BASE_URL.format(assetName)
    headers = {
        'Authorization' : 'Basic ' + creds.auth
    }

    req = requests.get(assetURL, headers=headers)
    return req.json()


def JB_OpenAssetPage(assetName):
    assetJSON = JB_GetAssetJSON(assetName)
    assetID   = assetJSON[0]['ItemID']
    assetURL  = JB_BASE_ASSET_URL.format(f"/{assetID}")

    OpenPage(assetURL)


def CYDER_OpenSearch(assetName):
    URL = CYDER_BASE_URL.format(assetName)
    OpenPage(URL)


def ACTLOG_OpenLog(assetName):
    URL = ACTLOG_BASE_URL.format(assetName)
    OpenPage(URL)



def OpenPage(URL):
    print(f"Opening {URL}")
    print(f"...")
    webbrowser.open(URL)


def printHelp():
    print('')
    print('Current list of supported flags: ')
    print('---------------------------------')
    print('#    jb/jitbit <MachineName>')
    print('#    cy/cyder <MachineName>')
    print('#    al/activitylog <MachineName>')

    print('')


if __name__ == '__main__':
    try:
        command   = sys.argv[1]
        assetName = sys.argv[2]

        if command == 'jb' or command == 'jitbit':
            JB_OpenAssetPage(assetName)
        elif command == 'cy' or command == 'cyder':
            CYDER_OpenSearch(assetName)
        elif command == 'al' or command == 'activitylog':
            ACTLOG_OpenLog(assetName)
        else:
            printHelp()
    except:
        printHelp()
