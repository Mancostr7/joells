import telethon
import asyncio
import os, sys
import re
import requests
from telethon import TelegramClient, events
from datetime import datetime
from telethon import types
import random
from dataclasses import replace
from email import message, message_from_binary_file
from fileinput import close
from itertools import count, islice
import logging
import os
from pdb import Restart
from typing import Text
from unicodedata import name
from unittest import result
import requests
import time
import string
import random
import asyncio
import re
import datetime
from asyncio import sleep
import os, yaml, sys
from envparse import env
from os import system
from colorama import Fore
import sys

R = "\033[31m"
G = "\033[32m"
M = "\033[0m"
B = M = "\033[34m"

bann = (G + """
╭━━╮╭━━╮╱╱╱╱╭━━━╮╱╭╮
┃╭╮┃╰┫┣╯╱╱╱╱┃╭━╮┃╱┃┃
┃╰╯╰╮┃┃╱╱╱╱╱┃┃╱┃┃╱┃┃
┃╭━╮┃┃┃╱╭━━╮┃╰━╯┣╮┃┃
┃╰━╯┣┫┣╮╰━━╯┃╭━╮┃╰╯┃
╰━━━┻━━╯╱╱╱╱╰╯╱╰┻━━╯ 𝙎𝙪𝙣𝙣𝙮𝙨
""")
print(bann)

SIM = G + "[" + M + ">" + G + "] "
ONE = M + "𝙀𝙣𝙩𝙚𝙧 𝙖𝙥𝙞 𝙞𝙙" + R + " ➤" + G + "➤" + M + "➤ "
DO = M + " 𝙀𝙣𝙩𝙚𝙧 𝙖𝙥𝙞 𝙝𝙖𝙨𝙝" + R + " ➤" + G + "➤" + M + "➤ "
TRI = M + "𝙀𝙣𝙩𝙚𝙧 𝙗𝙤𝙩 𝙩𝙤𝙠𝙚𝙣" + R + " ➤" + G + "➤" + M + "➤ "
CURT = M + "𝙀𝙣𝙩𝙚𝙧 𝙞𝙙 𝙙𝙚𝙡 𝙘𝙖𝙣𝙖𝙡 𝙙𝙚𝙡 𝙨𝙘𝙧𝙖𝙥𝙥𝙚𝙧" + R + " ➤" + G + "➤" + M + "➤ "
FB = R + "─────[sunnys " + M + "@Arielito" + R + "]───────" 
ES = "\n"
TOT = FB + ES + SIM 
SOLL = ES + SIM 
FRASS = "\n\n--|DESEAS ACTUALIZAR LA INFORMACION API_ID, API_HASH, BOT_TOKEN, CHANEL_ID ?\n--|si/no PRECIONA ENTER SI NO QUIERES ACTUALIZAR Y INICIAR EL SCRAPPER, SI QUIERES ACTUALIZAR ESCRIBE--> si : "

archv = os.listdir()
td = """
--|CODIGO ELABORADO POR SUNNYS EN TELEGRAM COMO: @Arielito779|--
--|CODIGO ELABORADO CON EXITO NO ENCONTRARAS NINGUNA REPLICA COMO ESTA EN NINGUN LADO YA QUE ES ORIGINAL|--
"""

print(td)


CONFIGS = {}

with open('config.yml', 'r', encoding='utf-8') as buffer:
    data = yaml.load(buffer, Loader=yaml.FullLoader)
    print("--|LOADED config.yml|--")
    print(f"--|TOTAL LOADED KEYS FROM config.yml:|--> ", len(data))
    CONFIGS.update(data)
    cn = f"{data}"

def yml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

if "None" in cn:
    API_ID = int(input(SOLL + ONE))
    API_HASH = input(SOLL + DO)
    BOT_TOKEN = input(SOLL + TRI)
    CHANEL_ID = int(input(SOLL + CURT))
    api_hash = (f"{API_HASH}")
    bot_token = (f"{BOT_TOKEN}")
    api_id = int(API_ID)
    chanel_id = int(CHANEL_ID)
    data = {
    'API_ID': api_id, 
    'API_HASH': api_hash,
    'BOT_TOKEN': bot_token, 
    'CHANEL_ID': chanel_id}
    yml_dump("config.yml", data)
else:
    x = input(FRASS)
    if "si" in x:
        if "session.session" in archv:
            os.remove("session.session")
        if "session.session-journal" in archv:
            os.remove("session.session-journal")
        API_ID = int(input(SOLL + ONE))
        API_HASH = input(SOLL + DO)
        BOT_TOKEN = input(SOLL + TRI)
        CHANEL_ID = int(input(SOLL + CURT))
        api_hash = (f"{API_HASH}")
        bot_token = (f"{BOT_TOKEN}")
        api_id = int(API_ID)
        chanel_id = int(CHANEL_ID)
        data = {
        'API_ID': api_id, 
        'API_HASH': api_hash,
        'BOT_TOKEN': bot_token, 
        'CHANEL_ID': chanel_id}
        yml_dump("config.yml", data)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = os.getenv('API_ID', CONFIG['API_ID'])
API_HASH = os.getenv('API_HASH', CONFIG['API_HASH'])

client = TelegramClient('session', API_ID, API_HASH)
ccs = []

from scrapper import post, proccs

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/hl'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.hl'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/su'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.su'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/sf'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.sf'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/vi'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.vi'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/pl'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.pl'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ca'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ca'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ba'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ba'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/vn'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.vn'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/pg'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.pg'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/cb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.cb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ccy'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ccy'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ady'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ady'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/eww'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.eww'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/smr'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.smr'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ud'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ud'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/br3'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.br3'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/sa'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.sa'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ux'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ux'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/sh'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.sh'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/s5'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.s5'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/gb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.gb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/he'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.he'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ze'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ze'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ho'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ho'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ft'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ft'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/bb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.bb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/li'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.li'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/sp'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.sp'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/sy'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.sy'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/jb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.jb'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/lk'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.lk'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/atr'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.atr'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/mi'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.mi'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ki'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ki'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ztc'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ztc'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/sl'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.sl'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/rei'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.rei'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ep'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ep'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/pf'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.pf'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/sc'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.sc'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/px'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.px'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/str'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.str'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.an'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ha'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ha'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.rem'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/rem'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/an'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.fex'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/fex'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.au'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/au'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.pp'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/pp'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.de'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/de'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.md'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/md'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.lx'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/lx'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.ce'):
        post(text=text)
        
@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/ce'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.cy'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/cy'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.br'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/br'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/chk'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.chk'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('/fv'):
        post(text=text)

@client.on(events.NewMessage())
async def my_event_handler(m: types.Message):
    text = m.text
    if str(text).__contains__('.fv'):
        post(text=text)

print("--|𝙊𝙆, 𝙋𝙍𝙊𝙂𝙍𝘼𝙈𝘼 𝙍𝙐𝙉𝙄𝙂|--\n"), proccs()
client.start()
client.run_until_disconnected()