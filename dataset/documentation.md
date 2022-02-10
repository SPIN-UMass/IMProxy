#  Practical Traffic Analysis on Secure Messaging Applications

## Trace overview

We release our generated message traces and our collected traffic dataset to benefit future works on traffic analysis, obtainable at [UMass Trace Repository](https://traces.cs.umass.edu/)

## Layout 

Layout of the folder:

```
.
├── signal
│   ├── generated_message_traces
│   │   └── messages_pareto_xm_5000_alpha_0.93_max30delay
│   ├── limited_bw
│   │   ├── 10Mbps_bw
│   │   │   ├── packets
│   │   │   └── timestamps
│   │   ├── 1Mbps_bw
│   │   │   ├── packets
│   │   │   └── timestamps
│   │   └── 5Mbps_bw
│   │       ├── packets
│   │       └── timestamps
│   ├── normal
│   │   ├── binary_flows
│   │   ├── packets
│   │   └── timestamps
│   └── vpn
│       ├── sender_japan
│       │   ├── packets
│       │   └── timestamps
│       ├── sender_south_africa
│       │   ├── packets
│       │   └── timestamps
│       └── sender_turkey
│           ├── packets
│           └── timestamps
├── telegram
│   ├── generated_message_traces
│   ├── normal
│   │   ├── adversary_message_traces
│   │   ├── binary_flows
│   │   └── pcaps
│   └── vpn
│       ├── adversary_message_traces
│       └── pcaps
├── wickr
│   ├── generated_message_traces
│   ├── limited_bw
│   │   ├── 1Mbps_bw
│   │   │   ├── adversary_message_traces
│   │   │   └── pcaps
│   │   └── 5Mbps_bw
│   │       ├── adversary_message_traces
│   │       └── pcaps
│   ├── normal
│   │   ├── adversary_message_traces
│   │   ├── binary_flows
│   │   └── pcaps
│   └── vpn
│       ├── sender_japan
│       │   ├── adversary_message_traces
│       │   └── pcaps
│       ├── sender_south_africa
│       │   ├── adversary_message_traces
│       │   └── pcaps
│       └── sender_turkey
│           ├── adversary_message_traces
│           └── pcaps
└── wire
    ├── countermeasures
    │   └── delayed
    │       ├── 50ms
    │       │   ├── packets
    │       │   └── timestamps
    │       └── 80ms
    │           ├── packets
    │           └── timestamps
    ├── generated_message_traces
    ├── limited_bw
    │   ├── 10Mbps_bw
    │   │   ├── packets
    │   │   └── timestamps
    │   ├── 1Mbps_bw
    │   │   ├── packets
    │   │   └── timestamps
    │   └── 5Mbps_bw
    │       ├── packets
    │       └── timestamps
    ├── normal
    │   ├── binary_flows
    │   ├── packets
    │   └── timestamps
    └── vpn
        ├── sender_japan
        │   ├── packets
        │   └── timestamps
        ├── sender_south_africa
        │   ├── packets
        │   └── timestamps
        └── sender_turkey
            ├── packets

```


## Directory discriptions

* `signal`, `telegram`, `wickr`, `wire` each contain the generated traces and collected traffic dataset of their corresponding Secure Instant Messaging (SIM) service.
* `generated_message_traces` directories, include the generated traces of their corresponding SIM service. The `json` trace files in this directory include the size, path of the attachment files (optional), message text (optional), message type, message id, and the amount of time to wait before sending the next message (in milliseconds).
* `normal` directories include the collected traffic under normal network conditions, while `limited_bw` directories inlcude the collected traffic for different bandwidth limits imposed on the attack target and `vpn` directories inlcude the collected traffic where the attacker is using a VPN server in various locations. 
    * In `signal` and `wire`, `timestamps` subdirectories include `.txt` files, each including timestamps for an hour's worth of messages. Each line in these `.txt` files includes the timestamp and the id of a message sent by the adversary.
      * `packets` subdirectories include the processed captured traffic of target users in the `pickle` format. The names for these files are arbitrary. Each `pickle` file is an array of Python dictionary objects each representing a packet. The keys of this packet dictionary are as follows:
        - `src`: source IP
        - `dst`: destination IP
        - `s_port`: source port
        - `d_port`: destination port
        - `size`: packet size in bytes
        - `timestamp`: packet timestamp
        - `protocol`: IP protocol number
        - `to_amazon`: True when packet is outgoing and False when packet is incoming with respect to the attack target.     
    * In `telegram` and `wickr`, `adversary_message_traces` subdirectories contain the collected traces of target communications by the adversary, and `pcap` subdirectories contain the raw captured traffic of target users. Adversary traces in `adversary_message_traces` subdirectories include a `.txt` file, every line of which has the timestamp, type, and size of a message. Each `.txt` file represents traces for an hour's worth of messages.
    
  * `countermeasures` subdirectory includes traces for traffic when delays drawn fram exponential distribution were added to the packets received by the target with average values of 50ms and 80ms.  
  * `binary_flows` subdirectories inlcude traces used train Deep Learning models. As explained in the paper<!--Section 6.5 of the journal-->, we convert each trace to a set of 0s and 1s for different lengths of observed traffic.

## Contact

Please do not hesitate to contact Ardavan Bozorgi via abozorgi at cs.umass.edu if you need any assistance with using these trace files.