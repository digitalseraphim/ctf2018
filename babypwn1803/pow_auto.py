#!/usr/bin/env python
from __future__ import print_function
import sys
import struct
import hashlib
import socket

# inspired by C3CTF's POW

def pow_hash(challenge, solution):
    return hashlib.sha256(challenge.encode('ascii') + struct.pack('<Q', solution)).hexdigest()

def check_pow(challenge, n, solution):
    h = pow_hash(challenge, solution)
    return (int(h, 16) % (2**n)) == 0

def solve_pow(challenge, n):
    candidate = 0
    while True:
        if check_pow(challenge, n, candidate):
            return candidate
        candidate += 1

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("e4771e24.quals2018.oooverflow.io",31337))
    data = s.recv(2048)
    print(data)
    lines = data.split("\n")
    
    challenge = lines[1].split(" ")[1]
    n = int(lines[2].split(" ")[1])

    print('Solving challenge: "{}", n: {}'.format(challenge, n))

    solution = solve_pow(challenge, n)
    s2 = pow_hash(challenge, solution)
    print('Solution: {} -> {}'.format(solution, s2))
    s.send("" + str(solution)+"\n")
    print(s.recv(2048))
    s.send(str(s2) + "\n")
    print(s.recv(2048))
    s.send(str(s2) + "\n")
    print(s.recv(2048))
    s.send(str(s2) + "\n")
    print(s.recv(2048))
    s.send(str(s2) + "\n")
    print(s.recv(2048))
