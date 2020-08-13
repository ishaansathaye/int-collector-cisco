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

def bits2hex(bits):
    decimal_representation = int(bits, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string[2:]

def hex2bits(hexString):
    convert = BitArray(hex=hexString)
    bit_string = convert.bin
    return bit_string

def hex2dec(hexCode):
    decimal_string = int(hexCode, 16)
    return decimal_string

print()
startHeader = '0'
# stackEnding = 0
# startingINTHeader = 0
# endingINTHeader = 0
# startingINTMetadataHeader = 0
# endingINTMetadataHeader = 0
# startingStack = 0
transport = input("What mode of transport?(UDP-1, TCP-2, Other-3): ")

if transport == '1':
    print()
    localPort = int(input("Enter UDP Port Number: "))
    startHeader = input("What is the starting header?(Eth-1, IP-2, UDP-3, VXLAN-4, INT-5): ")
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
    if startHeader == '1':
        offset = 0
    elif startHeader == '2':
        offset = 28
    elif startHeader == '3':
        offset = 68
    elif startHeader == '4':
        offset = 85
    elif startHeader == '5':
        offset = 100
    elif startHeader == '0':
        pass
else:
    print()
    print(bcolors.UNDERLINE + "Not Supported!" + bcolors.ENDC)
    print()


#Ethernet
class Ethernet():  

    def __init__(self):
        self.ethernetFrame = hexStream[0:28-offset]
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

        print()
        print(bcolors.UNDERLINE + "Ethernet Frame: " + bcolors.ENDC + bcolors.HEADER + self.destinationEthernet + bcolors.ENDC + " " + 
        bcolors.OKBLUE + self.sourceEthernet + bcolors.ENDC + " " + bcolors.OKGREEN + self.typeFieldEthernet + bcolors.ENDC)
        print("   DMAC: " + bcolors.HEADER + self.destinationEthernet + bcolors.ENDC)
        print("   SMAC: " + bcolors.OKBLUE + self.sourceEthernet + bcolors.ENDC)
        print("   EType: " + bcolors.OKGREEN + self.typeFieldEthernet + bcolors.ENDC)

#IP
class ip():

    def __init__(self):
        self.ipFrame = hexStream[(28-offset):(68-offset)]
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

        print()
        print(bcolors.UNDERLINE + "IP Frame: " + bcolors.ENDC + bcolors.HEADER + self.version_headerLength + bcolors.ENDC 
        + " " + bcolors.OKBLUE + self.typeService + bcolors.ENDC + " " + bcolors.OKGREEN + self.totalLength + bcolors.ENDC 
        + " " + bcolors.WARNING + self.identification + bcolors.ENDC + " " + bcolors.FAIL + self.flags + bcolors.ENDC 
        + " " + bcolors.HEADER + self.timeLive + bcolors.ENDC + " " + bcolors.OKBLUE + self.ipProtocol + bcolors.ENDC + " " 
        + bcolors.OKGREEN + self.headChecksum + bcolors.ENDC + " " + bcolors.WARNING + self.sourceIP + bcolors.ENDC + " " 
        + bcolors.FAIL + self.destinationIP + bcolors.ENDC)
        print("   Version: " + bcolors.HEADER + self.version_headerLength + bcolors.ENDC)
        print("   Type of Service: " + bcolors.OKBLUE + self.typeService + bcolors.ENDC)
        print("   Total Length: " + bcolors.OKGREEN + self.totalLength + bcolors.ENDC)
        print("   Identification: " + bcolors.WARNING + self.identification + bcolors.ENDC)
        print("   Flags: " + bcolors.FAIL + self.flags + bcolors.ENDC)
        print("   Time to Live: " + bcolors.HEADER + self.timeLive + bcolors.ENDC)
        print("   Protocol: " + bcolors.OKBLUE + self.ipProtocol + bcolors.ENDC)
        print("   Header Checksum: " + bcolors.OKGREEN + self.headChecksum + bcolors.ENDC)
        print("   Source: " + bcolors.WARNING + self.sourceIP + bcolors.ENDC)
        print("   Destination: " + bcolors.FAIL + self.destinationIP + bcolors.ENDC)

#UDP
class udp():
    
    def __init__(self):
        self.udpFrame = hexStream[(68-offset):(84-offset)]
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

        print()
        print(bcolors.UNDERLINE + "UDP Frame: " + bcolors.ENDC + bcolors.HEADER + self.sourceUDP + 
        bcolors.ENDC + " " + bcolors.OKBLUE + self.destinationUDP + bcolors.ENDC + " " + 
        bcolors.OKGREEN + self.lengthUDP + bcolors.ENDC + " " + bcolors.WARNING + self.udpChecksum 
        + bcolors.ENDC)
        print("   Source: " + bcolors.HEADER + self.sourceUDP + bcolors.ENDC)
        print("   Destination: " + bcolors.OKBLUE + self.destinationUDP + bcolors.ENDC)
        print("   Length: " + bcolors.OKGREEN + self.lengthUDP + bcolors.ENDC)
        print("   UDP Checksum: " + bcolors.WARNING + self.udpChecksum + bcolors.ENDC) 

#VXLAN - based on VXLAN GPE Header
class vxlan():
    
    def __init__(self):
        self.vxlanFrame = hexStream[(84-offset):(100-offset)]
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

        print()
        print(bcolors.UNDERLINE + "VXLAN Frame: " + bcolors.ENDC + bcolors.HEADER + self.vxlan_Flags + bcolors.ENDC + " " 
        + bcolors.OKBLUE + self.vxlan_Reserved1 + bcolors.ENDC + " " + bcolors.OKGREEN + self.nextProtocol + bcolors.ENDC 
        + " " + bcolors.WARNING + self.vni + bcolors.ENDC + " " +  bcolors.FAIL + self.vxlan_Reserved2 + bcolors.ENDC)
        print("   Flags: " + bcolors.HEADER + self.vxlan_Flags + bcolors.ENDC)
        print("   Reserved: " + bcolors.OKBLUE + self.vxlan_Reserved1 + bcolors.ENDC)
        print("   Next Protocol: " + bcolors.OKGREEN + self.nextProtocol + bcolors.ENDC)
        print("   VNI: " + bcolors.WARNING + self.vni + bcolors.ENDC)
        print("   Reserved: " + bcolors.FAIL + self.vxlan_Reserved2 + bcolors.ENDC)

#INT - 05 value for next protocol
class intHeader():
    
    def __init__(self):
        print()
        print(offset)
        print()

        if stackEnding == 0:
            startingINTHeader = (100-offset)
            endingINTHeader = (116-offset)
        else:
            startingINTHeader = stackEnding
            endingINTHeader = startingINTHeader+16
        self.intFrame = hexStream[startingINTHeader:endingINTHeader]

        self.intType = self.intFrame[0:2]
        self.intReserved = self.intFrame[2:4]
        self.intLength = self.intFrame[4:6]
        self.intNextProtocol = self.intFrame[6:8]
        self.intVariableOptionData = self.intFrame[8:16]
   
    def getINTNextProtocol(self):
        return self.intNextProtocol
    
    def displayINT(self):
        outputFile.writelines('\n')
        outputFile.writelines("INT Frame: " + self.intType + " " + self.intReserved + " " + self.intLength + " " + 
        self.intNextProtocol + " "+ self.intVariableOptionData + '\n')
        outputFile.writelines("   Type: " + self.intType + '\n')
        outputFile.writelines("   Reserved: " + self.intReserved + '\n')
        outputFile.writelines("   Length: " + self.intLength + '\n')
        outputFile.writelines("   Next Protocol: " + self.intNextProtocol + '\n')
        outputFile.writelines("   Variable Option Data: " + self.intVariableOptionData + '\n')

        print()
        print(bcolors.UNDERLINE + "INT Frame: " + bcolors.ENDC + bcolors.FAIL + self.intVariableOptionData 
        + bcolors.ENDC + " " + bcolors.OKBLUE + self.intReserved + bcolors.ENDC + " " + bcolors.OKGREEN 
        + self.intLength + bcolors.ENDC + " " + bcolors.WARNING + self.intNextProtocol + bcolors.ENDC + " " 
        + bcolors.FAIL + self.intVariableOptionData + bcolors.ENDC)
        print("   Type: " + bcolors.HEADER + self.intType + bcolors.ENDC)
        print("   Reserved: " + bcolors.OKBLUE + self.intReserved + bcolors.ENDC)
        print("   Length: " + bcolors.OKGREEN + self.intLength + bcolors.ENDC)
        print("   Next Protocol: " + bcolors.WARNING + self.intNextProtocol + bcolors.ENDC)
        print("   Variable Option Data: " + bcolors.FAIL + self.intVariableOptionData + bcolors.ENDC)

#INT Metadata Stack
class INTMetadata():
    
    def __init__(self):
        if stackEnding == 0:
            startingINTMetadataHeader = (116-offset)
            endingINTMetadataHeader = (132-offset)
        else:
            startingINTMetadataHeader = endingINTHeader
            endingINTMetadataHeader = startingINTMetadataHeader+16
        self.intMetadataHeader = hexStream[startingINTMetadataHeader:endingINTMetadataHeader]
        
        self.irreg = self.intMetadataHeader[0:4]
        self.inputString = self.irreg
        self.convert = BitArray(hex=self.inputString)
        self.flagBits = self.convert.bin
        self.versionBits = self.flagBits[0:2]
        self.replication = self.flagBits[2:4]
        self.copyBits = self.flagBits[4:5]
        self.maxHopCntExceeded = self.flagBits[5:6]
        self.reservedBits = self.flagBits[6:11]

        self.metaInstrCnt = bits2hex(self.flagBits[11:16])
        
        self.maxHopCnt = self.intMetadataHeader[4:6]

        self.totalHopCnt = self.intMetadataHeader[6:8]
        self.totalHopCntDec = hex2dec(self.intMetadataHeader[6:8])

        self.metaInstrBitmapBits = hex2bits(self.intMetadataHeader[8:12])
        self.metaSwitchID = self.metaInstrBitmapBits[0]
        self.metaIngressPortID = self.metaInstrBitmapBits[1]
        self.metaHopLatency = self.metaInstrBitmapBits[2]
        self.metaQueueOcc = self.metaInstrBitmapBits[3]
        self.metaIngressTime = self.metaInstrBitmapBits[4]
        self.metaEgressPortID = self.metaInstrBitmapBits[5]
        self.metaQueueCongestion = self.metaInstrBitmapBits[6]
        self.metaEgressPortTX = self.metaInstrBitmapBits[7]
        self.metaReservedBits = self.metaInstrBitmapBits[8:16]

        self.metaReserved = self.intMetadataHeader[12:16]
    
    def displayINTMetadata(self):
        outputFile.writelines('\n')
        outputFile.writelines("INT Metadata Header:" + " " + self.versionBits + self.replication + 
        self.copyBits + self.maxHopCntExceeded + self.reservedBits + " " + self.metaInstrCnt + 
        " " + self.maxHopCnt + " " + self.totalHopCnt + " " + self.metaInstrBitmapBits + " " + self.metaReserved + '\n')
        
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
        
        outputFile.writelines("   Instruction Bitmap(Bits): " + self.metaSwitchID + self.metaIngressPortID + self.metaHopLatency + self.metaQueueOcc +
        " " + self.metaIngressTime + self.metaEgressPortID + self.metaQueueCongestion + self.metaEgressPortTX + " " + 
        self.metaInstrBitmapBits[8:12] + " " + self.metaInstrBitmapBits[12:16] + '\n')
        outputFile.writelines("      Bit 0 Switch ID: " + self.metaSwitchID + '\n')
        outputFile.writelines("      Bit 1 Ingress Port ID: " + self.metaIngressPortID + '\n')
        outputFile.writelines("      Bit 2 Hop Latency: " + self.metaHopLatency + '\n')
        outputFile.writelines("      Bit 3 Queue Occupancy: " + self.metaQueueOcc + '\n')
        outputFile.writelines("      Bit 4 Ingress Timestamp: " + self.metaIngressTime + '\n')
        outputFile.writelines("      Bit 5 Egress Port ID: " + self.metaEgressPortID + '\n')
        outputFile.writelines("      Bit 6 Queue Congestion Status: " + self.metaQueueCongestion + '\n')
        outputFile.writelines("      Bit 7 Egress Port TX Utilization: " + self.metaEgressPortTX + '\n')
        outputFile.writelines("      Bit 8-16 Reserved Bits: " + self.metaReservedBits + '\n')
        outputFile.writelines("   Reserved: " + self.metaReserved + '\n')

        print()
        print(bcolors.UNDERLINE + "INT Metadata Header:" + bcolors.ENDC + " " + bcolors.HEADER + self.versionBits + bcolors.ENDC 
        + bcolors.OKBLUE + self.replication + bcolors.ENDC + bcolors.OKGREEN + self.copyBits 
        + bcolors.ENDC + bcolors.WARNING + self.maxHopCntExceeded + bcolors.ENDC + bcolors.FAIL 
        + self.reservedBits + bcolors.ENDC + " " + bcolors.HEADER + self.metaInstrCnt + bcolors.ENDC 
        + " " + bcolors.OKBLUE + self.maxHopCnt + bcolors.ENDC + " " + bcolors.OKGREEN + self.totalHopCnt 
        + bcolors.ENDC + " " + bcolors.HEADER + self.metaSwitchID + bcolors.ENDC + bcolors.OKBLUE 
        + self.metaIngressPortID + bcolors.ENDC + bcolors.OKGREEN + self.metaHopLatency + bcolors.ENDC 
        + bcolors.WARNING + self.metaQueueOcc + bcolors.ENDC + bcolors.FAIL + self.metaIngressTime + bcolors.ENDC 
        + bcolors.HEADER + self.metaEgressPortID + bcolors.ENDC + bcolors.OKBLUE + self.metaQueueCongestion 
        + bcolors.ENDC + bcolors.OKGREEN + self.metaEgressPortTX + bcolors.ENDC + bcolors.WARNING 
        + self.metaInstrBitmapBits[8:12] + self.metaInstrBitmapBits[12:16] + bcolors.ENDC + " " + bcolors.WARNING 
        + self.metaReserved + bcolors.ENDC)
        
        print(bcolors.BOLD + "   Flags(Bits): " + bcolors.ENDC+ bcolors.HEADER + self.versionBits 
        + bcolors.ENDC + " " + bcolors.OKBLUE + self.replication + bcolors.ENDC + " " 
        + bcolors.OKGREEN + self.copyBits + bcolors.ENDC + " " + bcolors.WARNING 
        + self.maxHopCntExceeded + bcolors.ENDC + " " + bcolors.FAIL + self.reservedBits + bcolors.ENDC)
        print("      Version(Bits): " + bcolors.HEADER + self.versionBits + bcolors.ENDC)
        print("      Replication(Bits): " + bcolors.OKBLUE + self.replication + bcolors.ENDC)
        print("      Copy(Bits): " + bcolors.OKGREEN + self.copyBits + bcolors.ENDC)
        print("      Max Hop Count Exceeded(Bits): " + bcolors.WARNING + self.maxHopCntExceeded + bcolors.ENDC)
        print("      Reserved Bits(Bits): " + bcolors.FAIL + self.reservedBits + bcolors.ENDC) 
        
        print("   Instruction Count: " + bcolors.HEADER + self.metaInstrCnt + bcolors.ENDC)
        print("   Max Hop Count: " + bcolors.OKBLUE + self.maxHopCnt + bcolors.ENDC)
        print("   Total Hop Count: " + bcolors.OKGREEN + self.totalHopCnt + bcolors.ENDC)
        
        print(bcolors.BOLD + "   Instruction Bitmap(Bits): " + bcolors.ENDC + bcolors.HEADER + self.metaSwitchID + bcolors.ENDC 
        + bcolors.OKBLUE + self.metaIngressPortID + bcolors.ENDC + bcolors.OKGREEN + self.metaHopLatency 
        + bcolors.ENDC + bcolors.WARNING + self.metaQueueOcc + bcolors.ENDC + " " + bcolors.FAIL 
        + self.metaIngressTime + bcolors.ENDC + bcolors.HEADER + self.metaEgressPortID + bcolors.ENDC 
        + bcolors.OKBLUE + self.metaQueueCongestion + bcolors.ENDC + bcolors.OKGREEN + self.metaEgressPortTX 
        + bcolors.ENDC + " " + bcolors.WARNING + self.metaInstrBitmapBits[8:12] + " " + self.metaInstrBitmapBits[12:16] + bcolors.ENDC)
        print("      Bit 0 Switch ID: " + bcolors.HEADER + self.metaSwitchID + bcolors.ENDC)
        print("      Bit 1 Ingress Port ID: " + bcolors.OKBLUE + self.metaIngressPortID + bcolors.ENDC)
        print("      Bit 2 Hop Latency: " + bcolors.OKGREEN + self.metaHopLatency + bcolors.ENDC)
        print("      Bit 3 Queue Occupancy: " + bcolors.WARNING + self.metaQueueOcc + bcolors.ENDC)
        print("      Bit 4 Ingress Timestamp: " + bcolors.FAIL + self.metaIngressTime + bcolors.ENDC)
        print("      Bit 5 Egress Port ID: " + bcolors.HEADER + self.metaEgressPortID + bcolors.ENDC)
        print("      Bit 6 Queue Congestion Status: " + bcolors.OKBLUE + self.metaQueueCongestion + bcolors.ENDC)
        print("      Bit 7 Egress Port TX Utilization: " + bcolors.OKGREEN + self.metaEgressPortTX + bcolors.ENDC)
        print("      Bit 8-16 Reserved Bits: " + bcolors.WARNING + self.metaReservedBits + bcolors.ENDC)
        print("   Reserved: " + bcolors.FAIL + self.metaReserved + bcolors.ENDC)
    
    def displayINTMetadataStack(self):
        outputFile.writelines('\n')
        count = self.metaInstrBitmapBits.count('1', 0, 7)
        totalParsing = (count*self.totalHopCntDec)*8
        
        if self.intNextProtocol != '05':
            startingStack = (132-offset)
            self.endingStack = ((132+totalParsing)-offset)
        else:
            startingStack = endingINTMetadataHeader
            self.endingStack = startingStack+totalParsing
        self.intMetadataHeaderStack = hexStream[startingStack:self.endingStack]
        
        tempStacList = self.intMetadataHeaderStack

        outputFile.writelines("INT Metadata Stack: " + self.intMetadataHeaderStack + '\n')
        print()
        print(bcolors.BOLD + bcolors.UNDERLINE + "INT Metadata Stack: " + self.intMetadataHeaderStack + bcolors.ENDC)
        for i in range(self.totalHopCntDec, 0, -1):
            outputFile.write("   Hop " + str(i) + ":" + '\n')
            print(bcolors.BOLD + "   Hop " + str(i) + ":" + bcolors.ENDC + '\n')
            if self.metaSwitchID == '1':
                outputFile.writelines("      Switch ID: " + tempStacList[0:8] + '\n')
                print("      Switch ID: " + + bcolors.HEADER + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")
            if self.metaIngressPortID == '1':
                outputFile.writelines("      Ingress Port ID: " + tempStacList[0:8] + '\n')
                print("      Ingress Port ID: " + bcolors.OKBLUE + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")
            if self.metaHopLatency == '1':
                outputFile.writelines("      Hop Latency: " + tempStacList[0:8] + '\n')
                print("      Hop Latency: " + bcolors.OKGREEN + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")
            if self.metaQueueOcc == '1':
                outputFile.writelines("      Queue Occupancy: " + tempStacList[0:8] + '\n')
                print("      Queue Occupancy: " + bcolors.WARNING + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")
            if self.metaIngressTime == '1':
                outputFile.writelines("      Ingress Timestamp: " + tempStacList[0:8] + '\n')
                print("      Ingress Timestamp: " + bcolors.FAIL + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")
            if self.metaEgressPortID == '1':
                outputFile.writelines("      Egress Port ID: " + tempStacList[0:8] + '\n')
                print("      Egress Port ID: " + bcolors.HEADER + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")
            if self.metaQueueCongestion == '1':
                outputFile.writelines("      Queue Congestation Status: " + tempStacList[0:8] + '\n')
                print("      Queue Congestation Status: " + bcolors.OKBLUE + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")
            if self.metaEgressPortTX == '1':
                outputFile.writelines("      Egress Port TX Utilization: " + tempStacList[0:8] + '\n')
                print("      Egress Port TX Utilization: " + bcolors.OKGREEN + tempStacList[0:8] + bcolors.ENDC)
                tempStacList = tempStacList.replace(tempStacList[0:8], "")

    def getMetaStackEnding(self):
        return self.endingStack

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
if transport == '1':
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

        outputFile = open("INT Output Files/" + file_out, "a")
        outputFile.truncate(0)
        outputFile.writelines("Packet: " + hexStream[0:80] + '\n')
        outputFile.writelines(hexStream[80:160] + '\n')
        outputFile.writelines(hexStream[160:240] + '\n')
        outputFile.writelines(hexStream[240:320] + '\n')

        #Parsing INT Packet 
        newPacket = Packet()

        def parseEth():
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
                            print()
                            print(bcolors.UNDERLINE + "INT Header exists!" + bcolors.ENDC)
                            newPacket.displayINT()
                            newPacket.displayINTMetadata()
                            newPacket.displayINTMetadataStack()
                        else:
                            outputFile.writelines('\n')
                            outputFile.writelines("No INT Header!" + '\n')
                            print()
                            print(bcolors.UNDERLINE + "No INT Header!" + bcolors.ENDC)
                    else:
                        outputFile.writelines('\n')
                        outputFile.writelines("Cannot display VXLAN Header!" + '\n')
                        print()
                        print(bcolors.UNDERLINE + "Cannot display VXLAN Header!" + bcolors.ENDC)
                else:
                    outputFile.writelines('\n')
                    outputFile.writelines("Cannot display UDP Header!" + '\n')
                    print()
                    print(bcolors.UNDERLINE + "Cannot display UDP Header!" + bcolors.ENDC)
            else:
                outputFile.writelines('\n')
                outputFile.writelines('Cannot display IP Header!' + '\n')
                print()
                print(bcolors.UNDERLINE + "Cannot display IP Header!" + bcolors.ENDC)
            print()
            print(file_out + " is ready!")
            print()
        def parseIP():
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
                        print()
                        print(bcolors.UNDERLINE + "INT Header exists!" + bcolors.ENDC)
                        newPacket.displayINT()
                        newPacket.displayINTMetadata()
                        newPacket.displayINTMetadataStack()
                    else:
                        outputFile.writelines('\n')
                        outputFile.writelines("No INT Header!" + '\n')
                        print()
                        print(bcolors.UNDERLINE + "No INT Header!" + bcolors.ENDC)
                else:
                    outputFile.writelines('\n')
                    outputFile.writelines("Cannot display VXLAN Header!" + '\n')
                    print()
                    print(bcolors.UNDERLINE + "Cannot display VXLAN Header!" + bcolors.ENDC)
            else:
                outputFile.writelines('\n')
                outputFile.writelines("Cannot display UDP Header!" + '\n')
                print()
                print(bcolors.UNDERLINE + "Cannot display UDP Header!" + bcolors.ENDC)
            print()
            print(file_out + " is ready!")
            print()
        def parseUDP():
            newPacket.displayUDP()
            destinationUDP = newPacket.getDestinationUDP()
            if destinationUDP == "12b5":
                newPacket.displayVXLAN()
                nextProtocol = newPacket.getNextProtocol()
                if nextProtocol == "05":
                    outputFile.writelines('\n')
                    outputFile.writelines("INT Header exists!" + '\n')
                    print()
                    print(bcolors.UNDERLINE + "INT Header exists!" + bcolors.ENDC)
                    newPacket.displayINT()
                    newPacket.displayINTMetadata()
                    newPacket.displayINTMetadataStack()
                else:
                    outputFile.writelines('\n')
                    outputFile.writelines("No INT Header!" + '\n')
                    print()
                    print(bcolors.UNDERLINE + "No INT Header!" + bcolors.ENDC)
            else:
                outputFile.writelines('\n')
                outputFile.writelines("Cannot display VXLAN Header!" + '\n')
                print()
                print(bcolors.UNDERLINE + "Cannot display VXLAN Header!" + bcolors.ENDC)
            print()
            print(file_out + " is ready!")
            print()
        def parseVXLAN():
            newPacket.displayVXLAN()
            nextProtocol = newPacket.getNextProtocol()
            if nextProtocol == "05":
                outputFile.writelines('\n')
                outputFile.writelines("INT Header exists!" + '\n')
                print()
                print(bcolors.UNDERLINE + "INT Header exists!" + bcolors.ENDC)
                newPacket.displayINT()
                newPacket.displayINTMetadata()
                newPacket.displayINTMetadataStack()
            else:
                outputFile.writelines('\n')
                outputFile.writelines("No INT Header!" + '\n')
                print()
                print(bcolors.UNDERLINE + "No INT Header!" + bcolors.ENDC)
            print()
            print(file_out + " is ready!")
            print()
        def parseINT():
            outputFile.writelines('\n')
            outputFile.writelines("INT Header exists!" + '\n')
            print()
            print(bcolors.UNDERLINE + "INT Header exists!" + bcolors.ENDC)
            newPacket.displayINT()
            newPacket.displayINTMetadata()
            newPacket.displayINTMetadataStack()
            print()
            print(file_out + " is ready!")
            print()

        if startHeader == '1':
            parseEth()
            # variableOptionData = newPacket.getMetadata()
            # intNextProtocolCheck = newPacket.getINTNextProtocol()
            # if intNextProtocolCheck == '05':
            #     stackEnding = newPacket.getMetaStackEnding()
            #     print()
            #     print(stackEnding)
            #     print()
            #     new2Packet = Packet()
            #     new2Packet.displayINT()
            #     new2Packet.displayINTMetadata()
            #     new2Packet.displayINTMetadataStack()
                # intNextProtocolCheck = newPacket.getINTNextProtocol()
        elif startHeader == '2':
            parseIP()
        elif startHeader == '3':
            parseUDP()
        elif startHeader == '4':
            parseVXLAN()
        elif startHeader == '5':
            parseINT()
        elif startHeader == '0':
            pass
        

        outputFile.writelines('\n')
        byteFile.close()
        outputFile.close()