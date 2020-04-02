#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import re

def factorize(N):
    i = 2
    # since there aren't any efficient ways to factorize big numbers let's just bruteforce!
    while N % i != 0:
        i += 1
    return i

# recursive implementation of the extended euclidean algorithm. This calculates the greatest common divisor of
# the two parameters in order to compute the modular inverse of b.
def eea(a, b):
    if a % b == 0:
        return [1, b]

    values = eea(b, a % b)

    t = values[0]
    gcd = values[1]

    return [(gcd - a * t) // b, gcd]

def calculateKey():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('crypto.hso-hacker.space', 10004))
    data = s.recv(1024).decode('utf-8')

    # Look for the module N and the public key value of e.
    rsaParameters = re.findall(r'[0-9]+', data)

    N = int(rsaParameters[0])
    e = int(rsaParameters[1])

    # to calculate d we need the value of φ(N). We get this number by factoring N in its prime factors p and q
    # and calculate (p - 1)(q - 1) to get φ(N).
    p = factorize(N)
    q = N // p

    phiN = (p - 1) * (q - 1)

    # to finally calculate the private key d we have to determine the modular inverse of e. You can do
    # that by using the extended euclidean algorithm.

    d = eea(phiN, e)[0]

    s.send(str(d).encode())
    data = s.recv(1024).decode('utf-8')
    print(data)

if __name__ == '__main__':
    calculateKey()
