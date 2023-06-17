
**OSI Model**: Conceptual model for creating networks. Comms b/w computing systems are split up into 7 layers.

7 layers: Please Do Not Throw Sausage Pizza Away:

1. Physical: Actual physical medium. Wires, voltages etc. Electrical impulses send data as bits. Wireless can be done via radio waves
2. Data link: Provides logical address, local connection b/w 2 hosts. Realm of switches. Mac address used in header to talk about source and destination
3. network: Network address and best path determination. network address is either applied on the way down or stripped on the way up through OSI stack. IP address layer. IP is needed when you need to get to other networks from your local network.
4. Transport: TCP or UDP layer. Most common protocol. End-to-end connections.
5. Session: Interhost communication. Establishes, manages and terminates sessions b/w applications.
6. Presentation: Data representation layer. DS, ensure data is readable. Translating data into human readable stuff.
7. Application: Provides network services to processes such as email.  
     
**TCP/IP Model**: Clumps OSI layers together.

1. Network Access (levels 1,2)
2. Internet (level 3)
3. Transport (level 4)
4. Application (levels 5,6,7)

OSI model prevalent in industry, lingua franca.

Can't ever skip layers, we need to go sequentially through all 7

### **Encapsulation**
When data travels from app layer to physical, it travels as data stream through 7,6,5. Then made into a segment of data streams at 4. Gets a port number at this point and a protocol header. Then a network header added to it at 3 and it's called a packet/datagram. Layer 2 adds frame header and trailer to this and it's now called a frame. This is then sent to NIC which converts it to binary.
Opposite is called decapsulation. Very critical.

### **IP Addressing**
Has 32 bits divided into 4 octets.
There are 3 defined private IP address ranges: 10.0, 192.168, 172.16 These only used for internal networking. Computer processes these as a string of binary values.
Made of 2 parts: Network portion and host portion. First three come in network portion.
If we say for instance 192.168.16 is network portion, every device in network has IP address starting with this.
The last octet (host portion) is for specific device.
However this breaking isn't universal, we can do different breaks. Hence traditional networking has address classes.

1. Class A: N:H 1:3: Large networks like unis, military
2. Class B: N:H 2:2: Medium sized networks
3. Class C: N:H 3:1: Small networks
4. Class D: N:H 0:4

By 90s we started to run out of IP addresses, hence ipv6.

In a network the first (all host bits 0) and last (all host bits 1) IP addresses are reserved. Called network and broadcast address resp.

How to know N:H split? Subnet masks. Class A: 255.0.0.0. Class B: 255.255.0.0. Class C: 255.255.255.0.

Because we ran out of IP addresses we don't use these classifications anymore. We use CIDR: Classless Inter-Domain Routing. /n is added to each address: n stands for number of bits in prefix. Rest are host number. Leads to more efficient allocation of ipv4 addresses.

TCP/IP hosts use combo of IP addr and subnet mask: to determine if other addresses are local or remote, which impacts the way a packet is formed to send to NIC.

Ipv6 has 128 bits unlike 32 of ipv4. Hex numbering system is used. CIDR also used.


*** bits are fundamental units. packets are made of bits.