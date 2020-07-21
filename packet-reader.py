byteFile = open('byte-stream.txt', 'rb')
byte = byteFile.readline()


while byte:
    print(byte)
    byte = byteFile.readline()

byteFile.close()
