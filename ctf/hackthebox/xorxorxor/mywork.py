#!/usr/bin/python3
import os
import math 

data = []

output = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'
print(bytes.fromhex(output))

for x in bytes.fromhex(output):
    data.append(x)

print(data)

key = [91, 30, 180, 154]
unxored = b''
for ITEM in range(0, len(data), 1):
    unxored += bytes([data[ITEM] ^ key[ITEM % len(key)]])

print(unxored)

for i in range(0, 255):
    answer = 123 ^ i
    if answer == 225:
        print("123 ^ {} = 225".format(i))

def hexToBinary(Hex2Bin):
    # Python code to demonstrate 
    # conversion of hex string 
    # to binary string 
    n = int(Hex2Bin, 8) 
    bStr = '' 
    while n > 0: 
        bStr = str(n % 2) + bStr 
        n = n >> 1	
    res = bStr 

    # Print the resultant string 
    return(res)


def decToBinary(num):
    if num > 1:
        decToBinary(num // 2)
        return(num % 2)


# from output.txt

# transform output var to hexadecimal
fromhex = int(output, 16)



# lst = []
# # get every 4'th item
# for ITEM in range(0, len(output), 4):
#     lst.append(output[ITEM])

# for ITEM in lst:
#     print(hexToBinary(hex(ITEM)))

# lst.sort()
# unique = list(set(lst))
# lst = unique
#print(lst)

# for x in range(0, 256):
#     print(str(x).hex())


# key = os.urandom(256)
# print(type(key[0]))
# print(key[0])
# for i in range(len(key)):
#     print(key[i])

def checkKey(dict, key, value): 
      
    if key in dict.keys(): 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 

# possiblekey = []
# for z in range(0, 255):
#     for y in range(0, 255):
#         # print(z)
#         # xorvalue = b''
#         # type(z)
#         xorvalue = z ^ y
#         # xorvalue += bytes(hex(z.encode()), encoding='utf8') ^ bytes(hex(y), encoding='utf8')
#         # print(xorvalue)
#         # print(xorvalue)
#         if xorvalue in lst:
#             possiblekey.append(xorvalue)

# possiblekey.sort()
# unique = list(set(possiblekey))
# print(possiblekey)
# for item in range(len(unique)):
#     print(unique[item])
#     print(possiblekey.count(unique[item]))

 

