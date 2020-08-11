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

print()
localPort = int(input("Enter UDP Port Number: "))
startHeader = input("What is the ")
file_out = input("Output Filename(No extension): ")
if file_out == None:
    file_out == "output_INT"
file_out = file_out + ".txt"

#Server
localIP = "127.0.0.1"
# localPort = 20001
bufferSize = 1024
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print()
print("Searching...")
hexStream = ""


#Ethernet
class Ethernet():  

    def __init__(self):
        self.ethernetFrame = hexStream[0:28]
        self.destinationEthernet = self.ethernetFrame[0:12]
        self.sourceEthernet = self.ethernetFrame[12:24]
        self.typeFieldEthernet = self.ethernetFrame[24:28]

    def getTypeFieldIP(self):
        return self.typeFieldEthernet

    def displayEthernet(self):
        outputFile.writelines('\n')
        outputFile.writelines("Ethernet Frame: " + self.destinationEthernet + " " + 
        self.sourceEthernet + " " + self.typeFieldEthernet + '\n')
        outputFile.writelines("   DMAC: " + self.destinationEthernet + '\n')
        outputFile.writelines("   SMAC: " + self.sourceEthernet + '\n')
        outputFile.writelines("   EType: " + self.typeFieldEthernet + '\n')

#IP
class ip():

    def __init__(self):
        self.ipFrame = hexStream[28:68]
        self.version_headerLength = self.ipFrame[0:2]
        self.typeService = self.ipFrame[2:4]
        self.totalLength = self.ipFrame[4:8]
        self.identification = self.ipFrame[8:12]
        self.flags = self.ipFrame[12:16]
        self.timeLive = self.ipFrame[16:18]
        self.ipProtocol = self.ipFrame[18:20]
        self.headChecksum = self.ipFrame[20:24]
        self.sourceIP = self.ipFrame[24:32]
        self.destinationIP = self.ipFrame[32:40]
    
    def getIPProtocol(self):
        return self.ipProtocol
    
    def displayIP(self):
        outputFile.writelines('\n')
        outputFile.writelines("IP Frame: " + self.version_headerLength + " " + self.typeService + " " + self.totalLength 
        + " " + self.identification + " " + self.flags + " " + self.timeLive + " " + 
        self.ipProtocol + " " + self.headChecksum + " " + self.sourceIP + " " + self.destinationIP + '\n')
        outputFile.writelines("   Version: " + self.version_headerLength + '\n')
        outputFile.writelines("   Type of Service: " + self.typeService + '\n')
        outputFile.writelines("   Total Length: " + self.totalLength + '\n')
        outputFile.writelines("   Identification: " + self.identification + '\n')
        outputFile.writelines("   Flags: " + self.flags + '\n')
        outputFile.writelines("   Time to Live: " + self.timeLive + '\n')
        outputFile.writelines("   Protocol: " + self.ipProtocol + '\n')
        outputFile.writelines("   Header Checksum: " + self.headChecksum + '\n')
        outputFile.writelines("   Source: " + self.sourceIP + '\n')
        outputFile.writelines("   Destination: " + self.destinationIP + '\n')

#UDP
class udp():
    
    def __init__(self):
        self.udpFrame = hexStream[68:84]
        self.sourceUDP = self.udpFrame[0:4]
        self.destinationUDP = self.udpFrame[4:8]
        self.lengthUDP = self.udpFrame[8:12]
        self.udpChecksum = self.udpFrame[12:16]
    
    def getDestinationUDP(self):
        return self.destinationUDP
    
    def displayUDP(self):
        outputFile.writelines('\n')
        outputFile.writelines("UDP Frame: " + self.sourceUDP + " " + self.destinationUDP + 
        " " + self.lengthUDP + " " + self.udpChecksum + '\n')
        outputFile.writelines("   Source: " + self.sourceUDP + '\n')
        outputFile.writelines("   Destination: " + self.destinationUDP + '\n')
        outputFile.writelines("   Length: " + self.lengthUDP + '\n')
        outputFile.writelines("   UDP Checksum: " + self.udpChecksum + '\n')

#VXLAN - based on VXLAN GPE Header
class vxlan():
    
    def __init__(self):
        self.vxlanFrame = hexStream[84:100]
        self.vxlan_Flags = self.vxlanFrame[0:2]
        self.vxlan_Reserved1 = self.vxlanFrame[2:6]
        self.nextProtocol = self.vxlanFrame[6:8]
        self.vni = self.vxlanFrame[8:14]
        self.vxlan_Reserved2 = self.vxlanFrame[14:16]
    
    def getNextProtocol(self):
        return self.nextProtocol
    
    def displayVXLAN(self):
        outputFile.writelines('\n')
        outputFile.writelines("VXLAN Frame: " + self.vxlan_Flags + " " + self.vxlan_Reserved1 + " "
        + self.nextProtocol + " " + self.vni + " " + self.vxlan_Reserved2 + '\n')
        outputFile.writelines("   Flags: " + self.vxlan_Flags + '\n')
        outputFile.writelines("   Reserved: " + self.vxlan_Reserved1 + '\n')
        outputFile.writelines("   Next Protocol: " + self.nextProtocol + '\n')
        outputFile.writelines("   VNI: " + self.vni + '\n')
        outputFile.writelines("   Reserved: " + self.vxlan_Reserved2 + '\n')

#INT - 05 value for next protocol
class intHeader():
    
    def __init__(self):
        self.intFrame = hexStream[100:116]
        self.intType = self.intFrame[0:2]
        self.intReserved = self.intFrame[2:4]
        self.intLength = self.intFrame[4:6]
        self.intNextProtocol = self.intFrame[6:8]
        self.intVariableOptionData = self.intFrame[8:16]
   
    def getMetadata(self):
        return self.intVariableOptionData
    
    def displayINT(self):
        outputFile.writelines('\n')
        outputFile.writelines("INT Frame: " + self.intType + " " + self.intReserved + " " + self.intLength + " " + 
        self.intNextProtocol + " "+ self.intVariableOptionData + '\n')
        outputFile.writelines("   Type: " + self.intType + '\n')
        outputFile.writelines("   Reserved: " + self.intReserved + '\n')
        outputFile.writelines("   Length: " + self.intLength + '\n')
        outputFile.writelines("   Next Protocol: " + self.intNextProtocol + '\n')
        outputFile.writelines("   Variable Option Data: " + self.intVariableOptionData + '\n')

#INT Metadata Stack
class INTMetadata():
    
    def __init__(self):
        self.intMetadataHeader = hexStream[116:132]
        
        self.irreg = self.intMetadataHeader[0:4]
        self.inputString = self.irreg
        self.convert = BitArray(hex=self.inputString)
        self.flagBits = self.convert.bin
        self.versionBits = self.flagBits[0:2]
        self.replication = self.flagBits[2:4]
        self.copyBits = self.flagBits[4:5]
        self.maxHopCntExceeded = self.flagBits[5:6]
        self.reservedBits = self.flagBits[6:11]

        self.metaInstrCnt = self.flagBits[11:16]
        self.maxHopCnt = self.intMetadataHeader[4:6]
        self.totalHopCnt = self.intMetadataHeader[6:8]
        self.metaInstrBit = self.intMetadataHeader[8:12]
        self.metaReserved = self.intMetadataHeader[12:16]
    
    def displayINTMetadata(self):
        outputFile.writelines('\n')
        outputFile.writelines("INT Metadata Header: " + " " + self.versionBits + self.replication + 
        self.copyBits + self.maxHopCntExceeded + self.reservedBits + " " + self.metaInstrCnt + 
        " " + self.maxHopCnt + " " + self.totalHopCnt + " " + self.metaInstrBit + " " + self.metaReserved + '\n')
        
        outputFile.writelines("   Flags(Bits): " + self.versionBits + " " + self.replication + " " + self.copyBits + " " + self.maxHopCntExceeded 
        + " " + self.reservedBits + '\n')
        outputFile.writelines("      Version(Bits): " + self.versionBits + '\n')
        outputFile.writelines("      Replication(Bits): " + self.replication + '\n')
        outputFile.writelines("      Copy(Bits): " + self.copyBits + '\n')
        outputFile.writelines("      Max Hop Count Exceeded(Bits): " + self.maxHopCntExceeded + '\n')
        outputFile.writelines("      Reserved Bits(Bits): " + self.reservedBits + '\n') 
        
        outputFile.writelines("   Instruction Count: " + self.metaInstrCnt + '\n')
        outputFile.writelines("   Max Hop Count: " + self.maxHopCnt + '\n')
        outputFile.writelines("   Total Hop Count: " + self.totalHopCnt + '\n')
        outputFile.writelines("   Instruction Bitmap: " + self.intNextProtocol + '\n')
        outputFile.writelines("   Reserved: " + self.metaReserved + '\n')
    
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
    msg = message.decode("utf-8")

    #File for hex stream
    byteFile = open('byte-stream.txt', 'w')
    byteFile.write(msg)
    byteFile.close()
    byteFileRead = open('byte-stream.txt', 'r')
    hexStream = byteFileRead.readline()

    outputFile = open("INT Output Files/"+file_out, "a")
    outputFile.truncate(0)
    outputFile.writelines("Packet: " + hexStream + '\n')

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
                    outputFile.writelines('\n')
                    outputFile.writelines("INT Header exists!" + '\n')
                    newPacket.displayINT()
                    variableOptionData = newPacket.getMetadata()
                    newPacket.displayINTMetadata()
                else:
                    outputFile.writelines('\n')
                    outputFile.writelines("No INT Header!" + '\n')
            else:
                outputFile.writelines('\n')
                outputFile.writelines("Cannot display VXLAN Header" + '\n')
        else:
            outputFile.writelines('\n')
            outputFile.writelines("Cannot display UDP Header!" + '\n')
    else:
        outputFile.writelines('\n')
        outputFile.writelines('Cannot display IP Header!' + '\n')
    print()
    print(file_out + " is ready!")
    outputFile.writelines('\n')
    byteFile.close()
    outputFile.close()