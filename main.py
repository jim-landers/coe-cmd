import sys, requests, webbrowser
import creds


BASE_ASSET_URL  = 'https://support.engineering.oregonstate.edu/Assets/Edit{}'
COE_WRAPPER_URL = 'https://tools.engr.oregonstate.edu/coetools/jitbit/?name={}'

CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# Random powershell command to open a window, please ignore.
# Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList https://support.engineering.oregonstate.edu/Assets/Edit/2934


def GetAssetJSON(assetName):
    assetURL = COE_WRAPPER_URL.format(assetName)

    header = {
        'Authorization' : 'Basic ' + creds.auth
    }

    req = requests.get(assetURL, headers=header)
    return req.json()




if __name__ == '__main__':

    assetJSON = GetAssetJSON(sys.argv[1])
    assetID   = assetJSON[0]['ItemID']
    assetURL  = BASE_ASSET_URL.format(f"/{assetID}")

    print(assetURL)

    webbrowser.get(CHROME_PATH).open(assetURL)
