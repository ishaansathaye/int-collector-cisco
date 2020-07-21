byteFile = open('byte-stream.txt', 'rb')
byte = byteFile.read(1)


while byte:
    print(byte)
    byte = byteFile.readline()

byteFile.close()
