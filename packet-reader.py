class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

byteFile = open('byte-streamVXLAN.txt', 'r')
hexStream = byteFile.readline()

# print(hexStream)

#Ethernet
print()
ethernetFrame = hexStream[0:28]
destinationEthernet = bcolors.HEADER + ethernetFrame[0:12] + bcolors.ENDC
sourceEthernet = bcolors.OKBLUE + ethernetFrame[12:24] + bcolors.ENDC
typeFieldEthernet = ethernetFrame[24:28]

print(bcolors.BOLD + "Ethernet Frame: " + bcolors.ENDC + destinationEthernet + " " + 
sourceEthernet + " " + bcolors.OKGREEN + typeFieldEthernet + bcolors.ENDC)

print("DMAC: " + destinationEthernet)
print("SMAC: " + sourceEthernet)
print("EType: " + bcolors.OKGREEN + typeFieldEthernet + bcolors.ENDC)


#IP
if (typeFieldEthernet == "0800"):
    print()
    ipFrame = hexStream[28:68]
    version_headerLength = bcolors.HEADER + ipFrame[0:2] + bcolors.ENDC
    typeService = bcolors.OKBLUE + ipFrame[2:4] + bcolors.ENDC
    totalLength = bcolors.OKGREEN + ipFrame[4:8] + bcolors.ENDC
    identification = bcolors.WARNING + ipFrame[8:12] + bcolors.ENDC
    flags = bcolors.FAIL + ipFrame[12:16] + bcolors.ENDC
    timeLive = bcolors.HEADER + ipFrame[16:18] + bcolors.ENDC
    ipProtocol = ipFrame[18:20]
    headChecksum = bcolors.OKGREEN + ipFrame[20:24] + bcolors.ENDC
    sourceIP = bcolors.WARNING + ipFrame[24:32] + bcolors.ENDC
    destinationIP = bcolors.FAIL + ipFrame[32:40] + bcolors.ENDC

    print(bcolors.BOLD + "IP Frame: " + bcolors.ENDC + version_headerLength + " " + typeService + " " + totalLength 
    + " " + identification + " " + flags + " " + timeLive + " " + bcolors.OKBLUE + 
    ipProtocol + bcolors.ENDC + " " + headChecksum + " " + sourceIP + " " + destinationIP)

    print("Version: " + version_headerLength)
    print("Type of Service: " + typeService)
    print("Total Length: " + totalLength)
    print("Identification: " + identification)
    print("Flags: " + flags)
    print("Time to Live: " + timeLive)
    print("Protocol: " + bcolors.OKBLUE + ipProtocol + bcolors.ENDC)
    print("Header Checksum: " + headChecksum)
    print("Source: " + sourceIP)
    print("Destination: " + destinationIP)
else:
    print()
    print('Cannot display IP Header!')


#UDP
if (ipProtocol == '11'):
    print()
    udpFrame = hexStream[68:84]
    sourceUDP = bcolors.HEADER + udpFrame[0:4] + bcolors.ENDC
    destinationUDP = udpFrame[4:8]
    lengthUDP = bcolors.OKGREEN + udpFrame[8:12] + bcolors.ENDC
    udpChecksum = bcolors.WARNING + udpFrame[12:16] + bcolors.ENDC
    
    print(bcolors.BOLD + "UDP Frame: " + bcolors.ENDC + sourceUDP + " " + bcolors.OKBLUE + destinationUDP + 
    bcolors.ENDC + " " + lengthUDP + " " + udpChecksum)

    print("Source: " + sourceUDP)
    print("Destination: " + bcolors.OKBLUE + destinationUDP + bcolors.ENDC)
    print("Length: " + lengthUDP)
    print("UDP Checksum: " + udpChecksum)
else:
    print()
    print("Cannon display UDP Header!")


#VXLAN
if destinationUDP == "12b5":
    print()
    print("Found VXLAN Port!")
else:
    print()
    print("Cannot display VXLAN Header")

print()
byteFile.close()