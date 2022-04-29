import platform

from pathlib import Path

FILENAME = ".coe_cmd_config"
REQ_KEY_LENGTH = 36

cached_key = ""


def GetApiKeyPath() -> str:
    path = str(Path.home())
    if platform.system() == "Windows":
        path += "\\"
    else:
        path += "/"
    return path + FILENAME


def GetApiKey() -> str:
    global cached_key

    if cached_key != "":
        return cached_key
    file = open(GetApiKeyPath(), "r")
    out = file.read()
    file.close()
    return out


def ApiKeyExists() -> bool:
    global cached_key

    config = Path(GetApiKeyPath())
    if config.is_file():
        with open(str(config), "r") as keyTxt:
            cached_key = keyTxt.read()
        return len(cached_key) == REQ_KEY_LENGTH
    return False


def PromptForKey():
    global cached_key

    key = input("Enter your COE API key: ")

    while len(key) != REQ_KEY_LENGTH:
        print(f"Your API key must be {REQ_KEY_LENGTH} characters long")
        key = input("Enter your COE API key: ")

    cached_key = key
    path = GetApiKeyPath()
    with open(path, "w") as keyTxt:
        keyTxt.write(key)
    print("Key written to " + path)
