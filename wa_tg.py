import pyautogui as pyg
import time
import pandas as pd
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import PeerChannel
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.errors.rpcerrorlist import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import PeerChannel
import asyncio
import configparser
import json
import re
import shutil
from utils import *

doc = input("How many docs?")

if __name__ == "__main__":
    print("Please dont touch your mouse until python downloads data from whatsapp")
    win_search = pyg.locateCenterOnScreen(
        "C:/Users/.../Desktop/python_automate/win_search.png"
    )
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)
    pyg.typewrite("whatsapp")
    pyg.press("enter")

    time.sleep(10)  # 15 seconds sleep

    wait = True
    while wait:
        win_search = pyg.locateCenterOnScreen(
            "C:/Users/.../Desktop/python_automate/whatsapp_search.png"
        )
        if type(win_search) == type(None):
            wait = True
        else:
            wait = False

    win_search = pyg.locateCenterOnScreen(
        "C:/Users/.../Desktop/python_automate/whatsapp_search.png"
    )
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)
    pyg.typewrite("test")
    pyg.press("enter")

    time.sleep(5)  # 5 seconds sleep

    win_search = pyg.locateCenterOnScreen(
        "C:/Users/.../Desktop/python_automate/whatsapp_attach3dots.png"
    )
    x = win_search[0] + 15
    y = win_search[1]
    pyg.click(x, y)

    time.sleep(1)  # 5 seconds sleep

    win_search = pyg.locateCenterOnScreen(
        "C:/Users/.../Desktop/python_automate/whatsapp_groupinfo.png"
    )
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    time.sleep(1)  # 5 seconds sleep

    win_search = pyg.locateCenterOnScreen(
        "C:/Users/.../Desktop/python_automate/whatsapp_medialinks.png"
    )
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    time.sleep(1)  # 5 seconds sleep

    doc_number = range(1, int(doc) + 1)

    win_search = pyg.locateCenterOnScreen(
        "C:/Users/.../Desktop/python_automate/whatsapp_docs.png"
    )
    x_doc = win_search[0]
    y_doc = win_search[1]

    for doc in doc_number:
        print(doc)
        y_axis = 200 * doc

        pyg.click(x_doc, y_doc)
        time.sleep(3)  # 5 seconds sleep

        pyg.moveRel(-30, y_axis)
        pyg.click()

        time.sleep(1)  # 5 seconds sleep

        wait = True
        while wait:
            win_search = pyg.locateCenterOnScreen(
                "C:/Users/.../Desktop/python_automate/win_save.png"
            )
            if type(win_search) == type(None):
                wait = True
            else:
                wait = False

        unix_time = time.time()
        pyg.press("left")
        pyg.typewrite("python_gen" + "_" + str(unix_time).split(".")[0])

        time.sleep(1)  # 5 seconds sleep

        win_search = pyg.locateCenterOnScreen(
            "C:/Users/.../Desktop/python_automate/win_save.png"
        )
        x = win_search[0]
        y = win_search[1]
        pyg.click(x, y)

        time.sleep(5)

    unix_time = time.time()
    file = "temp_watg_folder" + "_" + str(unix_time).split(".")[0]

    os.mkdir(file)
    new_path = os.path.abspath(file)

    downloaded_path = r"C:\Users\...\Downloads"

    for file_name in os.listdir(downloaded_path):
        if "python_gen_" in file_name:
            shutil.move(downloaded_path + "/" + file_name, new_path)

    nest_asyncio.apply()
    info = information_parser("config.ini")

    client = TelegramClient(info[0], info[2], info[3])

    for file_name in os.listdir(new_path):

        print(file_name)

        async def main():
            await client.send_file("Test", file)

        async with client:
            client.loop.run_until_complete(main())
