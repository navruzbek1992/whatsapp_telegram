import pyautogui as pyg
import time
from datetime import datetime
from telethon.sync import TelegramClient
import asyncio
import configparser
import json
import re
import shutil
from utils import *
import os
import nest_asyncio
import subprocess
import webbrowser


nest_asyncio.apply()

doc = input("How many docs?: ")

async def send_data(new_path):
    for file_name in os.listdir(new_path):
        if "python_gen_" in file_name:
            file = new_path + "/" + file_name
            await client.send_file("me", file)


def send_to_tg(new_path):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_data(new_path))



if __name__ == "__main__":

    print("Please dont touch your mouse until python downloads data from whatsapp")
    username = input("What is username for this PC?: ")
    openweb = input("Is whatsapp installed: ")

    if not openweb:        
        subprocess.Popen(
            [
                "C:/Users"
                + "/"
                + str(username)
                + "/"
                + "AppData/Local/WhatsApp/WhatsApp.exe",
                "-new-tab",
            ]
        )
    else:
        webbrowser.open('https://web.whatsapp.com/')
    
    time.sleep(10)
    waiter("whatsapp_search.png")
    win_search = pyg.locateCenterOnScreen("whatsapp_search.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)
    pyg.typewrite("test")
    pyg.press("enter")

    time.sleep(5)

    waiter("whatsapp_attach3dots.png")
    win_search = pyg.locateCenterOnScreen("whatsapp_attach3dots.png")
    x = win_search[0] + 15
    y = win_search[1]
    pyg.click(x, y)

    time.sleep(2)
    win_search = pyg.locateCenterOnScreen("whatsapp_groupinfo.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    waiter("whatsapp_medialinks.png")
    win_search = pyg.locateCenterOnScreen("whatsapp_medialinks.png")
    x = win_search[0]
    y = win_search[1]
    pyg.click(x, y)

    time.sleep(2)  # 5 seconds sleep
    doc_number = range(1, int(doc) + 1)

    win_search = pyg.locateCenterOnScreen("whatsapp_docs.png")
    x_doc = win_search[0]
    y_doc = win_search[1]

    for doc in doc_number:
        print(doc)
        y_axis = 150 * doc

        pyg.click(x_doc, y_doc)
        time.sleep(3)  # 5 seconds sleep

        pyg.moveRel(-30, y_axis)
        pyg.click()

        time.sleep(2)

        unix_time = time.time()
        pyg.press("left")
        pyg.typewrite("python_gen" + "_" + str(unix_time).split(".")[0])

        time.sleep(2)  # 5 seconds sleep

        waiter("win_save.png")
        win_search = pyg.locateCenterOnScreen("win_save.png")
        x = win_search[0]
        y = win_search[1]
        pyg.click(x, y)

        time.sleep(5)

    unix_time = time.time()
    file = "temp_watg_folder" + "_" + str(unix_time).split(".")[0]

    os.mkdir(file)
    new_path = os.path.abspath(file)

    downloaded_path = "C:/Users" + "/" + str(username) + "/" + "Downloads"

    for file_name in os.listdir(downloaded_path):
        if "python_gen_" in file_name:
            shutil.move(downloaded_path + "/" + file_name, new_path)

    nest_asyncio.apply()
    info = information_parser("config.ini")

    async with TelegramClient(info[0], info[2], info[3]) as client:
        await client.start()
        
        send_to_tg(new_path)
    
    print("Done!")
