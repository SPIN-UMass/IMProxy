# IMProxy

- To obfuscate the packets arriving to an Instant Messaging (IM) application, we can add a small delay to each packet. To do this, we use an Ubuntu machine to run a proxy server and add the (IP, port) of that server to our IM setup.

    First, install [dante](https://www.inet.no/dante/) and configure it to run a SOCKS5 proxy on the Ubuntu machine. Then use the following command to add an iptables rule:
    ```
    iptables -I INPUT -d <your machine's IP> -p tcp --dport <your proxy port> -j NFQUEUE --queue-num 1
    ```
    The `average_delay` parameter in `delay_packets.py` determines the mean of the exponential distribution from which the delay values are drawn. The unit for this value is in seconds.

    Finally, run `delay_packets.py`. Now the Ubuntu machine can be used to add delays to arriving packets.

- `IMProxy_simulation.ipynb` includes the implementation for simulating IMProxy by padding packets as well as adding delays to packets. 