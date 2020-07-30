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
global hexStream
hexStream = byteFile.readline()


#Ethernet
class Ethernet():   
    ethernetFrame = hexStream[0:28]
    destinationEthernet = bcolors.HEADER + ethernetFrame[0:12] + bcolors.ENDC
    sourceEthernet = bcolors.OKBLUE + ethernetFrame[12:24] + bcolors.ENDC
    typeFieldEthernet = ethernetFrame[24:28]
    def getTypeFieldIP(self):
        return self.typeFieldEthernet
    def displayEthernet(self):
        print()
        print(bcolors.BOLD + "Ethernet Frame: " + bcolors.ENDC + self.destinationEthernet + " " + 
        self.sourceEthernet + " " + bcolors.OKGREEN + self.typeFieldEthernet + bcolors.ENDC)
        print("DMAC: " + self.destinationEthernet)
        print("SMAC: " + self.sourceEthernet)
        print("EType: " + bcolors.OKGREEN + self.typeFieldEthernet + bcolors.ENDC)

#IP
class IP():    
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
    def getIPProtocol(self):
        return self.ipProtocol
    def displayIP(self):
        print()
        print(bcolors.BOLD + "IP Frame: " + bcolors.ENDC + self.version_headerLength + " " + self.typeService + " " + self.totalLength 
        + " " + self.identification + " " + self.flags + " " + self.timeLive + " " + bcolors.OKBLUE + 
        self.ipProtocol + bcolors.ENDC + " " + self.headChecksum + " " + self.sourceIP + " " + self.destinationIP)
        print("Version: " + self.version_headerLength)
        print("Type of Service: " + self.typeService)
        print("Total Length: " + self.totalLength)
        print("Identification: " + self.identification)
        print("Flags: " + self.flags)
        print("Time to Live: " + self.timeLive)
        print("Protocol: " + bcolors.OKBLUE + self.ipProtocol + bcolors.ENDC)
        print("Header Checksum: " + self.headChecksum)
        print("Source: " + self.sourceIP)
        print("Destination: " + self.destinationIP)




#UDP
class UDP():
    udpFrame = hexStream[68:84]
    sourceUDP = bcolors.HEADER + udpFrame[0:4] + bcolors.ENDC
    destinationUDP = udpFrame[4:8]
    lengthUDP = bcolors.OKGREEN + udpFrame[8:12] + bcolors.ENDC
    udpChecksum = bcolors.WARNING + udpFrame[12:16] + bcolors.ENDC
    def getDestinationUDP(self):
        return self.destinationUDP
    def displayUDP(self):
        print()
        print(bcolors.BOLD + "UDP Frame: " + bcolors.ENDC + self.sourceUDP + " " + bcolors.OKBLUE + self.destinationUDP + 
        bcolors.ENDC + " " + self.lengthUDP + " " + self.udpChecksum)
        print("Source: " + self.sourceUDP)
        print("Destination: " + bcolors.OKBLUE + self.destinationUDP + bcolors.ENDC)
        print("Length: " + self.lengthUDP)
        print("UDP Checksum: " + self.udpChecksum)


#VXLAN - based on VXLAN GPE Header
class VXLAN():
    vxlanFrame = hexStream[84:100]
    vxlan_Flags = bcolors.HEADER + vxlanFrame[0:2] + bcolors.ENDC
    vxlan_Reserved1 = bcolors.OKBLUE + vxlanFrame[2:6] + bcolors.ENDC
    nextProtocol = vxlanFrame[6:8]
    vni = bcolors.WARNING + vxlanFrame[8:14] + bcolors.ENDC
    vxlan_Reserved2 = bcolors.FAIL + vxlanFrame[14:16] + bcolors.ENDC
    def getNextProtocol(self):
        return self.nextProtocol
    def displayVXLAN(self):
        print()
        print(bcolors.BOLD + "VXLAN Frame: " + self.vxlan_Flags + " " + self.vxlan_Reserved1 + " " + bcolors.OKGREEN
        + self.nextProtocol + bcolors.ENDC + " " + self.vni + " " + self.vxlan_Reserved2)
        print("Flags: " + self.vxlan_Flags)
        print("Reserved: " + self.vxlan_Reserved1)
        print("Next Protocol: " + bcolors.OKGREEN + self.nextProtocol + bcolors.ENDC)
        print("VNI: " + self.vni)
        print("Reserved: " + self.vxlan_Reserved2)

#INT - 05 value for next protocol
class INT():
    intFrame = hexStream[100:116]
    intType = bcolors.HEADER + intFrame[0:2] + bcolors.ENDC
    intReserved = bcolors.OKBLUE + intFrame[2:4] + bcolors.ENDC
    intLength = bcolors.OKGREEN + intFrame[4:6] + bcolors.ENDC
    intNextProtocol = bcolors.WARNING + intFrame[6:8] + bcolors.ENDC
    intVariableOptionData = intFrame[8:16]
    def getMetadata(self):
        return self.intVariableOptionData
    def displayINT(self):
        print()
        print(bcolors.BOLD + "INT Frame: " + self.intType + " " + self.intReserved + " " + self.intLength + " " + 
        self.intNextProtocol + " " + bcolors.FAIL + self.intVariableOptionData + bcolors.ENDC)
        print("Type: " + self.intType)
        print("Reserved: " + self.intReserved)
        print("Length: " + self.intLength)
        print("Next Protocol: " + self.intNextProtocol)
        print("Variable Option Data: " + bcolors.FAIL + self.intVariableOptionData + bcolors.ENDC)

class INTMetadata():
    intMetadataHeader = hexStream[116:132]
    # metaFlags = bcolors.HEADER + intMetadataHeader[0:2] + bcolors.ENDC
    # metaInstrCnt = bcolors.HEADER + intMetadataHeader[0:2] + bcolors.ENDC
    # maxHopCnt = bcolors.OKBLUE + intMetadataHeader[2:4] + bcolors.ENDC
    # totalHopCnt = bcolors.OKGREEN + intMetadataHeader[4:6] + bcolors.ENDC
    meaInstrBit = bcolors.HEADER + intMetadataHeader[12:14] + bcolors.ENDC
    metaReserved = bcolors.HEADER + intMetadataHeader[14:16] + bcolors.ENDC
    def getMetadataStack():
        pass
    def displayINTMetadata():
        pass

#Packet Class inheriting
class Packet(Ethernet, IP, UDP, VXLAN, INT, INTMetadata):
    pass
    
newPacket = Packet()
typeField = newPacket.getTypeFieldIP()
newPacket.displayEthernet()
if typeField == '0800':
    newPacket.displayIP()
    ipProtocol = newPacket.getIPProtocol()
    if ipProtocol == '11':
        newPacket.displayUDP()
        destinationUDP = newPacket.getDestinationUDP()
        if destinationUDP == "12b5":
            newPacket.displayVXLAN()
            nextProtocol = newPacket.getNextProtocol()
            if nextProtocol == "05":
                newPacket.displayINT()
                variableOptionData = newPacket.getMetadata()
            else:
                print()
                print("Cannot display INT Header!")
        else:
            print()
            print("Cannot display VXLAN Header")
    else:
        print()
        print("Cannot display UDP Header!")
else:
    print()
    print('Cannot display IP Header!')

print()
byteFile.close()