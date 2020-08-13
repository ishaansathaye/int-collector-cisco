# import numpy as np

# byte = b"3d"

# Bytes = np.fromstring("", dtype= "uint8")
# Bits = np.unpackbits(Bytes, count=8)

# print(Bits)


# from bitstring import BitArray

# inputString = '05'
# c = BitArray(hex=inputString)
# print(c.bin)

# class class1():
#     def __init__(self):
#         self.number = 10000
#         # super.__init__()
#     def getNum(self):
#         return self.number
    
# class class2():
#     def __init__(self):
#         self.othernum = 1111
#         # super().__init__()
#     def displaynum(self):
#         return self.othernum

# class class3():
#     def __init__(self):
#         self.numfind = 2222
#         # super().__init__()
#     def shownum(self):
#         return self.numfind

# class class4(class1, class2, class3):
#     pass

# somebody = thing1()
# print(somebody.getNum())

# somebody = nextThing()
# print(somebody.displaynum())

# newperson = class4()
# print(newperson.shownum())

# binary_string = "01110"

# decimal_representation = int(binary_string, 2)
# hexadecimal_string = hex(decimal_representation)

# print(hexadecimal_string[2:])

# sample = 'askrguoyghsofurisalsdjflasdjfowiehgoeihgoasdjfaosjfoiwehfgoejfosjdfjasleihfgoahergoajsdifjalsdjfoaiehrgoasidlasjdlfjoifyhsoeugrigur'
# print(len(sample))
# print(sample[0:80])
# print(sample[80:160])

# def thing():
#     asdf = 1
#     print('hello')
#     return asdf
# def otherthing():
#     pass

import socket
import struct
addr_long = int("c0a8380b",16)
print(socket.inet_ntoa(struct.pack("<L", addr_long)))
