import socket

print()
udpPort = int(input("Enter UDP Port Number: "))
print()

msgFromClient = b"080027f21d8c080027ae4d6208004500004ed998400040116f9ec0a8380bc0a8380c9bf412b5003a00000800000500007b00ffffffffffffba092b6ef8be08060001080006040001ba092b6ef8be0a0000010000000000000a000002"
serverAddressPort = ("127.0.0.1", udpPort)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(msgFromClient, serverAddressPort)

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
# msg = "Message from Server {}".format(msgFromServer[0])
# print(msg)

#Fabricate INT Packet on this
# Packet = 080027f21d8c080027ae4d6208004500004ed998400040116f9ec0a8380bc0a8380c9bf412b5003a00000800000000007b00ffffffffffffba092b6ef8be08060001080006040001ba092b6ef8be0a0000010000000000000a000002
