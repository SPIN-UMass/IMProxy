# IMProxy
IMProxy is a proxy-based obfuscation system built for Instant Messaging (IM) communications. IMProxy combines two obfuscation
techniques: changing the timing of messages (by adding delays), and changing the sizes of events through adding dummy traffic.


## Components
server-proxy.py is a SOCKS5 proxy which lies between the IM client and the IM server. It redirect the IM packets to the server and once it receives a message from client (burst of packets), it produce dummy packets following the actual message and send them to dead-end destination. In such case, the adversary on the client side observes dummy packets but on the server side he only observes the actual IM packets.

## How to Use
Currently IMProxy works with Telegram API, but it can easily be deployed by other IM applications. To use IMProxy, you have to use our SOCKS5 proxy to tunnel the IM packets through this proxy. Usually most IM applications have the option to tunnel their traffic through an specific proxy.   
