import configparser
import pyautogui as pyg
import subprocess
import time


def information_parser(config_read):
    # Reading Configs
    config = configparser.ConfigParser()
    config.read(config_read)

    # Setting configuration values
    api_id = config["Telegram"]["api_id"]
    api_hash = config["Telegram"]["api_hash"]
    api_hash = str(api_hash)

    phone = config["Telegram"]["phone"]
    username = config["Telegram"]["username"]
    return tuple([phone, username, api_id, api_hash])


def waiter(filename):
    wait = True
    while wait:
        win_search = pyg.locateCenterOnScreen(filename)
        if type(win_search) == type(None):
            wait = True
        else:
            wait = False

    return


def send_by_tg(username, tg_group_name, path):

    subprocess.Popen(
        [
            "C:/Users"
            + "/"
            + str(username)
            + "/"
            + "AppData/Roaming/Telegram Desktop/Telegram",
        ]
    )

    time.sleep(3)
    win_search = pyg.locateCenterOnScreen("tg_search.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    pyg.typewrite(tg_group_name)
    pyg.press("enter")

    time.sleep(2)

    win_search = pyg.locateCenterOnScreen("tg_attach.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    time.sleep(2)

    win_search = pyg.locateCenterOnScreen("tg_file_path.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x + 100, y)

    pyg.typewrite(path)
    pyg.press("enter")

    pyg.moveRel(x, +200)
    pyg.click()
    pyg.hotkey("ctrl", "a")

    time.sleep(2)

    win_search = pyg.locateCenterOnScreen("tg_open.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    time.sleep(2)

    win_search = pyg.locateCenterOnScreen("tg_send.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    return True
