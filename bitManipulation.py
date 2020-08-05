# import numpy as np

# byte = b"3d"

# Bytes = np.fromstring("", dtype= "uint8")
# Bits = np.unpackbits(Bytes, count=8)

# print(Bits)


from bitstring import BitArray

inputString = '05'
c = BitArray(hex=inputString)
print(c.bin)