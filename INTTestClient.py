import socket
import argparse

parser = argparse.ArgumentParser(description='INT Test Client Input Parameter:')
parser.add_argument('-p', type=int, help='transport port number: (default: 20001)', default=20001)
args = parser.parse_args()
udpPort = args.p

msgFromClient = b"4e41500000114e415000000108004500004ed9980000ff119af40c0104020c010401200012b5002000000100040500007b00010009050002100390000000000030030000006200003002000002800000300180000505010009030002100388000000000030030010d012000030020010e010000030018010e21a"
serverAddressPort = ("127.0.0.1", udpPort)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(msgFromClient, serverAddressPort)