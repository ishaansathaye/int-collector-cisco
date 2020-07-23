class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

byteFile = open('byte-stream.txt', 'r')
hexStream = byteFile.readline()

# print(hexStream)

ethernetFrame = hexStream[0:28] # Ethernet frame is a 14-byte header: two 6-byte addresses and a 2-byte type field
print(bcolors.WARNING + ethernetFrame[0:12] + bcolors.ENDC + " " + bcolors.OKGREEN + ethernetFrame[12:24] + bcolors.ENDC + " " + bcolors.HEADER + ethernetFrame[24:28] + bcolors.ENDC)

destinationEthernet = ethernetFrame[0:12] # Yellow
print("DMAC: " + bcolors.WARNING + destinationEthernet + bcolors.ENDC)

sourceEthernet = ethernetFrame[12:24] # Green 
print("SMAC: " + bcolors.OKGREEN + sourceEthernet + bcolors.ENDC)

typeFieldEthernet = ethernetFrame[24:28] # Purple
print("EType: " + bcolors.HEADER + typeFieldEthernet + bcolors.ENDC)

byteFile.close()