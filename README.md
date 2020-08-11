# Cisco Internship Inband-Network Telemetry Collector

### What is this program?

To understand this program, one needs to have an understanding of traditional packet routing. The Control Plane is responsible for managing and populating the Routing Table which contains mapping between packet’s destinations and ports. It consists of programs running routing protocols that decipher the protocol packets exchanged between routers and switches in the network and fill the Routing Table. Information from the Routing Table is fed into the Forwarding Table in Data plane over a programming interface that connects the Control Plane with Data Plane. The Data Plane is primarily responsible to transfer packets from an input port to an output port by looking up entries/rules in Forwarding table based on packet’s destination.

<p align="left"><img src="TraditionalSwitch.png" width="1000"></p>

In-Band Network Telemetry (INT) allows for the routing of the packet to take place completely in the data plane without any intervention from the control plane. This, in effect, allows for the packet to travel much faster than traditional routing methods allow. 




The INT Collector is a program that parses an example packet that is sent from client to server. The client-UDP program sends the packet to the packet-reader program and then parses it and isolates its various headers including the INT header which tells the packet where to go without any interference from a control plane. 


### Installation Instructions

Only One module is required for the Collector program to run

to install it, run these commands:

```sh

pip install bitstring

```

### Running Information

to run the program, go to the directory in your terminal and type in:

```sh

python packet-reader.py

```
