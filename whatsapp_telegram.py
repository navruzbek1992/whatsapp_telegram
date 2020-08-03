
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
import json
import re
import nest_asyncio

def information_parser(config_read, sniffer_name, channel):
    
    config = configparser.ConfigParser()
    config.read(config_read) ##"config.ini"

    if sniffer_name == 'Telegram':
        # Setting configuration values
        api_id = config['Telegram']['api_id']
        api_hash = config['Telegram']['api_hash']
        api_hash = str(api_hash)

        phone = config['Telegram']['phone']
        username = config['Telegram']['username']
        return(tuple([phone, username, api_id, api_hash]))
    
nest_asyncio.apply()
info = information_parser('config.ini', 'Telegram', channel = False)

###### create a connection #######
client = TelegramClient(info[0], info[2], info[3])

### check if the user is authorized or not ###
client.connect()

# Ensure I am authorized #
if not client.is_user_authorized():
    client.send_code_request(info[0])
    try:
        client.sign_in(info[0], input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))
        ## assuming u have set up the password

#### just for fun ####
if client.is_connected:
    print('Connected to TG')
    sniffer_notifier(text = 'Connected to TG', token = info2[0], channel = info2[1])

#################################################
##### get all channels of that user #####
def channel_extractor():
    chats = []
    chunk_size = None
    ## could be changed ## set None to retrieve all
    groups=[]
    last_date = None
    chunk_size = 100
    groups=[]

    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)
    channels = []
    for a in chats:
        try:
            channels.append(a.username)
            # only chats with username are channels which returns messages
        except AttributeError:
            continue
    channels = [i for i in channels if i is not None]
    return(channels)

my_channels = channel_extractor() ## get channel id
print(my_channels)