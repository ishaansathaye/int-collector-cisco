import socket

print()
udpPort = int(input("Enter UDP Port Number: "))
print()

msgFromClient = b"4e41500000114e415000000108004500004ed9980000ff119af40c0104020c010401200012b5002000000100040500007b00010009030002100390000000000030030000006200003002000002800000300180000505"
serverAddressPort = ("127.0.0.1", udpPort)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(msgFromClient, serverAddressPort)