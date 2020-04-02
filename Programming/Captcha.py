#!/usr/bin/env python3

import requests
import re
import base64
import os

def crackCaptcha():
    pass

def solveCaptchas():
    session = requests.session()
    params = {}

    captchaPage = session.post('http://hso-hacker.space:7790/index.php', data=params).text
    pngSrc = re.findall(r'base64,(.+)">', captchaPage)[0]

    if pngSrc == '':
        return

    print(pngSrc)

    pngBinary = base64.b64decode(pngSrc)
    print(pngBinary)
    print(type(pngBinary))

    with open('/home/carlos/PycharmProjects/CaptchaPNGs/cap.png', 'wb', os.O_CREAT) as f:
        f.write(pngBinary)

    session.close()

if __name__ == '__main__':
    solveCaptchas()
