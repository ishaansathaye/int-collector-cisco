# __TCP/IP__

### Steps in forwarding an IP datagram from source host to destination host through a router

## TCP/IP Overview
- Term "TCP/IP"
    - Anything related to the specific protocols of TCP and IP
    - Protocols, applications, and network medium
    - Sample protocols: UDP, ARP, and ICMP
    - Sample applications: TELNET, FTP, and rcp
- Structure <p align="center"><img src="structure.png" width="1000"></p>
    - Structure of the layered protocols inside a computer on an internet
    - **Boxes are the processing of the data as it passes through the computer**
    - **Lines connecting the boxes show the path of data**
    - **Horizontal line at bottom is the Ethernet cable**
    - **"o" is the transceiver**
    - **"*" is the IP address and "@" is the Ethernet address.**
- Terms
    - Unit of data on Ethernet -> Ethernet frame
    - Between Ethernet driver and IP module -> IP packet
    - Between IP module and UDP module -> UDP datagram
    - Between IP module and TCP module -> TCP segment (a transport message)
    - In network application -> application message
    - **Driver:** is software that communicates directly with the network
   interface hardware.  
   - **Module:** software that communicates with a
   driver, with network applications, or with another module.
- Flow of Data
    - FTP (FileTransfer Protocol) is a typical application that uses TCP
        - Protocol stack: FTP/TCP/IP/ENET.
    - Multiplexers switch many inputs to one output. De-multi are opposite <p align="center"><img src="multi.png" width="1000"></p>
- Two Network Interfaces <p align="center"><img src="two.png" width="1000"></p>
    - Computers with more than one physical network interface, the IP module is both a multiplexer and de-multiplexer
    - Performs multiplexing in both directions to accommodate incoming and outgoing data: <p align="center"><img src="both.png" width="1000"></p>
    - It can forward data onto the next network and data can arrive on any network interface and be sent out to any other
    - **"Forwarding" an IP Packet** is the process of sending an IP packet out onto another network
    - **"IP-router"** is a computer that has been dedicated the task of forwarding IP packets
- IP creates a Single Logical Network
    - **IP header** contains the IP address, which builds a single logical network from multiple physical networks.
        - This interconnection is called the internet: a set of physical networks that limit the range of an IP packet
- Physical Network Independence
    - Takeaway: IP hides the underlying network hardware form the network applications so they are not vulnerable to changes in hardware tech
- Interoperability
    - **"Interoperate"** is when two computers on an internet communicate
    - **"Interoperability"** is when the implementation of internet tech is good

## Ethernet
- Ethernet frame contains destination address, source address, type field, and data
- Address is 6 bytes, every device has its own address and listens for frames with that destination address
- Also listen for Ethernet frames with a "broadcast" address
- CSMA/CD (Carrier Sense and Multiple Access with Collision Detection)
    - All devices communicate on a single medium, one can transmit at a time, and all receive at the same time

## ARP