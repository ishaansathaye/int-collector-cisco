import socket
from bitstring import BitArray, __version__

#Color-coding
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Server
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
# msgFromServer = "Hello UDP Client!"
# bytesToSend = str.encode(msgFromServer)
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print()
print("Searching...")
print()
hexStream = ""


#Ethernet
class Ethernet():  

    def __init__(self):
        self.ethernetFrame = hexStream[0:28]
        self.destinationEthernet = bcolors.HEADER + self.ethernetFrame[0:12] + bcolors.ENDC
        self.sourceEthernet = bcolors.OKBLUE + self.ethernetFrame[12:24] + bcolors.ENDC
        self.typeFieldEthernet = self.ethernetFrame[24:28]

    def getTypeFieldIP(self):
        return self.typeFieldEthernet

    def displayEthernet(self):
        print()
        print(bcolors.BOLD + "Ethernet Frame: " + bcolors.ENDC + self.destinationEthernet + " " + 
        self.sourceEthernet + " " + bcolors.OKGREEN + self.typeFieldEthernet + bcolors.ENDC)
        print("   DMAC: " + self.destinationEthernet)
        print("   SMAC: " + self.sourceEthernet)
        print("   EType: " + bcolors.OKGREEN + self.typeFieldEthernet + bcolors.ENDC)

#IP
class ip():

    def __init__(self):
        self.ipFrame = hexStream[28:68]
        self.version_headerLength = bcolors.HEADER + self.ipFrame[0:2] + bcolors.ENDC
        self.typeService = bcolors.OKBLUE + self.ipFrame[2:4] + bcolors.ENDC
        self.totalLength = bcolors.OKGREEN + self.ipFrame[4:8] + bcolors.ENDC
        self.identification = bcolors.WARNING + self.ipFrame[8:12] + bcolors.ENDC
        self.flags = bcolors.FAIL + self.ipFrame[12:16] + bcolors.ENDC
        self.timeLive = bcolors.HEADER + self.ipFrame[16:18] + bcolors.ENDC
        self.ipProtocol = self.ipFrame[18:20]
        self.headChecksum = bcolors.OKGREEN + self.ipFrame[20:24] + bcolors.ENDC
        self.sourceIP = bcolors.WARNING + self.ipFrame[24:32] + bcolors.ENDC
        self.destinationIP = bcolors.FAIL + self.ipFrame[32:40] + bcolors.ENDC
    
    def getIPProtocol(self):
        return self.ipProtocol
    
    def displayIP(self):
        print()
        print(bcolors.BOLD + "IP Frame: " + bcolors.ENDC + self.version_headerLength + " " + self.typeService + " " + self.totalLength 
        + " " + self.identification + " " + self.flags + " " + self.timeLive + " " + bcolors.OKBLUE + 
        self.ipProtocol + bcolors.ENDC + " " + self.headChecksum + " " + self.sourceIP + " " + self.destinationIP)
        print("   Version: " + self.version_headerLength)
        print("   Type of Service: " + self.typeService)
        print("   Total Length: " + self.totalLength)
        print("   Identification: " + self.identification)
        print("   Flags: " + self.flags)
        print("   Time to Live: " + self.timeLive)
        print("   Protocol: " + bcolors.OKBLUE + self.ipProtocol + bcolors.ENDC)
        print("   Header Checksum: " + self.headChecksum)
        print("   Source: " + self.sourceIP)
        print("   Destination: " + self.destinationIP)

#UDP
class udp():
    
    def __init__(self):
        self.udpFrame = hexStream[68:84]
        self.sourceUDP = bcolors.HEADER + self.udpFrame[0:4] + bcolors.ENDC
        self.destinationUDP = self.udpFrame[4:8]
        self.lengthUDP = bcolors.OKGREEN + self.udpFrame[8:12] + bcolors.ENDC
        self.udpChecksum = bcolors.WARNING + self.udpFrame[12:16] + bcolors.ENDC
    
    def getDestinationUDP(self):
        return self.destinationUDP
    
    def displayUDP(self):
        print()
        print(bcolors.BOLD + "UDP Frame: " + bcolors.ENDC + self.sourceUDP + " " + bcolors.OKBLUE + self.destinationUDP + 
        bcolors.ENDC + " " + self.lengthUDP + " " + self.udpChecksum)
        print("   Source: " + self.sourceUDP)
        print("   Destination: " + bcolors.OKBLUE + self.destinationUDP + bcolors.ENDC)
        print("   Length: " + self.lengthUDP)
        print("   UDP Checksum: " + self.udpChecksum)

#VXLAN - based on VXLAN GPE Header
class vxlan():
    
    def __init__(self):
        self.vxlanFrame = hexStream[84:100]
        self.vxlan_Flags = bcolors.HEADER + self.vxlanFrame[0:2] + bcolors.ENDC
        self.vxlan_Reserved1 = bcolors.OKBLUE + self.vxlanFrame[2:6] + bcolors.ENDC
        self.nextProtocol = self.vxlanFrame[6:8]
        self.vni = bcolors.WARNING + self.vxlanFrame[8:14] + bcolors.ENDC
        self.vxlan_Reserved2 = bcolors.FAIL + self.vxlanFrame[14:16] + bcolors.ENDC
    
    def getNextProtocol(self):
        return self.nextProtocol
    
    def displayVXLAN(self):
        print()
        print(bcolors.BOLD + "VXLAN Frame: " + self.vxlan_Flags + " " + self.vxlan_Reserved1 + " " + bcolors.OKGREEN
        + self.nextProtocol + bcolors.ENDC + " " + self.vni + " " + self.vxlan_Reserved2)
        print("   Flags: " + self.vxlan_Flags)
        print("   Reserved: " + self.vxlan_Reserved1)
        print("   Next Protocol: " + bcolors.OKGREEN + self.nextProtocol + bcolors.ENDC)
        print("   VNI: " + self.vni)
        print("   Reserved: " + self.vxlan_Reserved2)

#INT - 05 value for next protocol
class intHeader():
    
    def __init__(self):
        self.intFrame = hexStream[100:116]
        self.intType = bcolors.HEADER + self.intFrame[0:2] + bcolors.ENDC
        self.intReserved = bcolors.OKBLUE + self.intFrame[2:4] + bcolors.ENDC
        self.intLength = bcolors.OKGREEN + self.intFrame[4:6] + bcolors.ENDC
        self.intNextProtocol = bcolors.WARNING + self.intFrame[6:8] + bcolors.ENDC
        self.intVariableOptionData = self.intFrame[8:16]
   
    def getMetadata(self):
        return self.intVariableOptionData
    
    def displayINT(self):
        print()
        print(bcolors.BOLD + "INT Frame: " + self.intType + " " + self.intReserved + " " + self.intLength + " " + 
        self.intNextProtocol + " " + bcolors.FAIL + self.intVariableOptionData + bcolors.ENDC)
        print("   Type: " + self.intType)
        print("   Reserved: " + self.intReserved)
        print("   Length: " + self.intLength)
        print("   Next Protocol: " + self.intNextProtocol)
        print("   Variable Option Data: " + bcolors.FAIL + self.intVariableOptionData + bcolors.ENDC)

#INT Metadata Stack
class INTMetadata():
    
    def __init__(self):
        self.intMetadataHeader = hexStream[116:132]
        
        self.irreg = self.intMetadataHeader[0:4]
        self.inputString = self.irreg
        self.convert = BitArray(hex=self.inputString)
        self.flagBits = self.convert.bin
        # metaFlags = bcolors.HEADER + flagBits[0:11] + bcolors.ENDC
        self.versionBits = bcolors.OKBLUE + self.flagBits[0:2] + bcolors.ENDC
        self.replication = bcolors.OKGREEN + self.flagBits[2:4] + bcolors.ENDC
        self.copyBits = bcolors.WARNING + self.flagBits[4:5] + bcolors.ENDC
        self.maxHopCntExceeded = bcolors.FAIL + self.flagBits[5:6] + bcolors.ENDC
        self.reservedBits = bcolors.HEADER + self.flagBits[6:11] + bcolors.ENDC

        self.metaInstrCnt = self.flagBits[11:16]
        self.maxHopCnt = bcolors.OKGREEN + self.intMetadataHeader[4:6] + bcolors.ENDC
        self.totalHopCnt = self.intMetadataHeader[6:8]
        self.metaInstrBit = bcolors.FAIL + self.intMetadataHeader[8:12] + bcolors.ENDC
        self.metaReserved = bcolors.HEADER + self.intMetadataHeader[12:16] + bcolors.ENDC
    
    def displayINTMetadata(self):
        print(bcolors.BOLD + "INT Metadata Header: " + bcolors.ENDC + " " + self.versionBits + self.replication + 
        self.copyBits + self.maxHopCntExceeded + self.reservedBits + " " + bcolors.OKBLUE + self.metaInstrCnt + 
        bcolors.ENDC + " " + self.maxHopCnt + " " + bcolors.WARNING + self.totalHopCnt + bcolors.ENDC + " " + 
        self.metaInstrBit + " " + self.metaReserved)
        
        print("   Flags(Bits): " + self.versionBits + " " + self.replication + " " + self.copyBits + " " + self.maxHopCntExceeded 
        + " " + self.reservedBits)
        print("      Version(Bits): " + self.versionBits)
        print("      Replication(Bits): " + self.replication)
        print("      Copy(Bits): " + self.copyBits)
        print("      Max Hop Count Exceeded(Bits): " + self.maxHopCntExceeded)
        print("      Reserved Bits(Bits): " + self.reservedBits) 
        
        print("   Instruction Count: " + bcolors.OKBLUE + self.metaInstrCnt + bcolors.ENDC)
        print("   Max Hop Count: " + self.maxHopCnt)
        print("   Total Hop Count: " + bcolors.WARNING + self.totalHopCnt + bcolors.ENDC)
        print("   Instruction Bitmap: " + self.intNextProtocol)
        print("   Reserved: " + self.metaReserved)
    
    def displayINTMetadataStack(self):
        pass

#Packet Class inheriting
class Packet(Ethernet, ip, udp, vxlan, intHeader, INTMetadata):
    
    def __init__(self):
        Ethernet.__init__(self)
        ip.__init__(self)
        udp.__init__(self)
        vxlan.__init__(self)
        intHeader.__init__(self)
        INTMetadata.__init__(self)

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    print()
    msg = message.decode("utf-8")
    print()

    #File for hex stream
    byteFile = open('byte-stream.txt', 'w')
    print()
    byteFile.write(msg)
    byteFile.close()
    byteFileRead = open('byte-stream.txt', 'r')
    hexStream = byteFileRead.readline()

    #Parsing INT Packet   
    newPacket = Packet()
    typeField = newPacket.getTypeFieldIP()
    newPacket.displayEthernet()
    if typeField == '0800':
        ipProtocol2 = newPacket.getIPProtocol()
        newPacket.displayIP()
        if ipProtocol2 == '11':
            newPacket.displayUDP()
            destinationUDP = newPacket.getDestinationUDP()
            if destinationUDP == "12b5":
                newPacket.displayVXLAN()
                nextProtocol = newPacket.getNextProtocol()
                if nextProtocol == "05":
                    print()
                    print(bcolors.BOLD + "INT Header exists!" + bcolors.ENDC)
                    newPacket.displayINT()
                    print()
                    variableOptionData = newPacket.getMetadata()
                    newPacket.displayINTMetadata()
                else:
                    print()
                    print("No INT Header!")
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