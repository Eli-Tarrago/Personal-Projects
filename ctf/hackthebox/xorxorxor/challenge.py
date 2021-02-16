#!/usr/bin/python3
import os
# flag = open('flag.txt', 'r').read().strip().encode()
output = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'


class XOR:
    def __init__(self):
        # Generate random bytes, 4 length. 
        # returned in byte format, hexademical.
        self.key = os.urandom(4)
        print(self.key)
    def encrypt(self, data: bytes) -> bytes:

        # Define a new variable, in byte format.
        xored = b''

        # for i in start: 0, end: len data, step: 1
        for i in range(len(data)):
            # print(data[i])
            print(i % len(self.key))
            # xored variable is string, that recieves "additions" as the loop progresses
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
            # print(bytes([data[i] ^ self.key[i % len(self.key)]]))
            #                                   i = range, i%key will be, 0,1,2,3. Making the key length, 4.
        return xored
    def decrypt(self, data: bytes) -> bytes:
        unhexedData = []
        for x in bytes.fromhex(data):
           unhexedData.append(x)

        self.key = [91, 30, 180, 154]
        unxored = b''

        for ITEM in range(0, len(data), 1):
            unxored += bytes([data[ITEM] ^ self.key[ITEM % len(self.key)]])


def main():
    global flag
    crypto = XOR()
    print ('Flag:', crypto.encrypt(flag).hex())

if __name__ == '__main__':
    main()
