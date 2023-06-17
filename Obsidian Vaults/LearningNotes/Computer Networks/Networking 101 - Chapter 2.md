### Application Layer: Overview
We just write software for network edges (client, server etc.) and not network core.

#### Client-server paradigm
- Server:
	- always-on host
	- permanent IP
	- often in DCs
- Client:
	- communicate with server
	- may have intermittent connection, dynamic IP address
	- do not communicate directly with each other. Eg - HTTP, FTP

#### Peer-peer architecture
No always-on server. More complex to manage; arbitrary end systems directly talk. Peers intermittently connected, self-scaling and change IP addresses.

***Process***: program running within a host. Within same host, two processes talk using IPC (inter-process comm.) defined by OS. Different hosts' processes communicate by message passing.

***Sockets***: process sends/receives messages to/from socket. Akin to a door. Found between transport and application layer.

#### Protocols 
An application layer protocol defines:
1. Types of messages exchanged e.g. request, response
2. Message syntax
3. Message semantics
4. Rules for when and how processes send & respond to messages

Open protocols: defined in RFCs. E.g. HTTP, SMTP. Proprietary e.g.: Skype, Zoom.

*What transport services do apps need?*
Some apps need data integrity (like file transfer needs 100% reliability), some timing (like games), some throughput, some security.

##### Internet transport protocol services
TCP:
- Reliable transport between sending and receiving process
- flow control
- congestion control: throttle sender when network overloaded
- connection oriented
- does not provide: timing, min throughput guarantee, security

UDP:
- unreliable data transfer
- Does not provide reliability, flow control etc (all TCP stuff)
- Advantage: does not provide a lot so we can build stuff on our own, so less overhead.