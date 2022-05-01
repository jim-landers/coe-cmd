import sys
import webbrowser
import requests

import api_key

COETOOL_API_URL = 'https://tools.engr.oregonstate.edu/coetools/api/'
JB_BASE_URL     = 'https://support.engineering.oregonstate.edu/{}'
JB_ASSET_URL    = JB_BASE_URL.format('Assets/Edit/{}')
JB_TICKET_URL   = JB_BASE_URL.format('Ticket/{}')


CYDER_BASE_URL  = 'https://cyder.oregonstate.edu/search/?search={}'

ACTLOG_BASE_URL = 'https://tools.engr.oregonstate.edu/coetools/lablogs/labinfo.php?{}'




def JB_GetAssetJSON(assetName: str):
    assetURL = COETOOL_API_URL

    payload = {
        'name' : assetName,
        'api'  : api_key.GetApiKey()
    }

    req = requests.post(assetURL, data=payload)
    return req.json()


def JB_OpenTicket(ticketNumber: str):
    OpenPage(JB_TICKET_URL.format(ticketNumber))


def JB_OpenAssetPage(assetName: str):
    assetJSON = JB_GetAssetJSON(assetName)
    assetID   = assetJSON[0]['ItemID']
    assetURL  = JB_ASSET_URL.format(f"{assetID}")

    OpenPage(assetURL)


def CYDER_OpenSearch(assetName: str):
    URL = CYDER_BASE_URL.format(assetName)
    OpenPage(URL)


def ACTLOG_OpenMachineLog(assetName: str):
    URL = ACTLOG_BASE_URL.format(f"hostname={assetName}")
    OpenPage(URL)


def ACTLOG_OpenUserLog(ONID: str):
    URL = ACTLOG_BASE_URL.format(f"username={ONID}")
    OpenPage(URL)


def OpenPage(URL: str):
    print(f"Opening {URL} ...")
    webbrowser.open(URL)


def PrintHelp():
    print()
    print('Current list of supported flags: ')
    print('---------------------------------')
    print('#    jb/jitbit <MachineName>')
    print('#    t/ticket <TicketNumber>')
    print('#    cy/cyder <MachineName>')
    print('#    alm/activitylogm <MachineName>')
    print('#    alu/activitylogu <ONID>')
    print()




def main():
    if len(sys.argv) != 3:
        PrintHelp()
        return

    if not api_key.ApiKeyExists():
        api_key.PromptForKey()

    command  = sys.argv[1]
    identity = sys.argv[2]

    if command in ('jb', 'jitbit'):
        JB_OpenAssetPage(identity)
    elif command in ('t', 'ticket'):
        JB_OpenTicket(identity)
    elif command in ('cy', 'cyder'):
        CYDER_OpenSearch(identity)
    elif command in ('alm', 'activitylogm'):
        ACTLOG_OpenMachineLog(identity)
    elif command in ('alu', 'activitylogu'):
        ACTLOG_OpenUserLog(identity)
    else:
        PrintHelp()


if __name__ == '__main__':
    main()
