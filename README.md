# Traffic Analysis of Secure (E2E encrypted) Messaging Apps (E.g., WhatsApp, Signal, Telagram)


[Paper, slides, and video (NDSS'2020)](https://www.ndss-symposium.org/ndss-paper/practical-traffic-analysis-attacks-on-secure-messaging-applications/)


## Abatract:

Instant Messaging (IM) applications like Telegram, Signal, and WhatsApp have become tremendously popular in recent years.
Unfortunately, such IM services have been  targets of continuous  governmental surveillance and censorship, as these services are home to public and private communication channels on socially and politically sensitive topics.
To protect their clients,
  popular IM services deploy state-of-the-art encryption mechanisms.
In this work, we show that despite the use of advanced encryption, popular IM applications leak sensitive information about their clients to adversaries who merely monitor their encrypted IM traffic, with no need for leveraging any software vulnerabilities of IM applications.
Specifically, we devise traffic analysis attacks that enable an adversary to identify  participants of target IM communications (e.g., forums) with  high accuracies.
We believe that our study demonstrates  a significant, real-world threat to the users of such services
given the increasing attempts by oppressive governments at cracking down controversial IM channels.


We demonstrate the practicality of  our traffic analysis attacks through extensive experiments on real-world IM communications. We show that standard  countermeasure techniques such as adding cover traffic  can degrade the effectiveness of the attacks we introduce in this paper.
We hope that our study will encourage IM providers to integrate effective  traffic obfuscation countermeasures into their software.
In the meantime, we have designed
a proof of concept countermeasure system, called  IMProxy, that can be used by IM clients  with no need for any support from IM providers. We demonstrate the effectiveness of IMProxy through simulation and experiments.

## Summary of our key findings: 

- We devise traffic analysis attacks against encrypted Instant Messaging (IM) applications that shows these apps leak sensitive information about their users to an adversary monitoring the encrypted traffic resulting in reliable identification of users in sensitive communications. These attacks are not due to buggy software implementations of the target services and also do not require the adversary to cooperate with the target IM providers.
- We perform extensive experiments on popular IM providers including Signal, Telegram, Wire, Wickr, and WhatsApp to demonstrate the real-world effectiveness of the attacks.
- We show that our attack outperform Deep Learning techniques for all applications except for Signal and Wire which we believe to be a result of deploying obfuscation techniques.
- We study potential countermeasures and design and evaluate IMProxy, a proxy-based countermeasure system which does not require any support from the IM providers.
- In our experiments, we show that an adversary can deploy the attacks with hierarchical observation intervals to improve its accuracy and optimize computation.
- The proposed shape-based detector outperforms the proposed event-based detector for smaller values of false positive rates. Yet, the event-based detector is up to two orders of magnitude faster than the shape-based detector and it performs stronger against our countermeasures.
- The experiments to evaluate the effect of the bandwidth of the target user's device show that lower bandwidths result in reduced accuracy of the attacks, but the reduction comes with a compromise in the usability of the service. Therefore, we can say as long as the target has enough bandwidth to use the service comfortably, the attacks are still viable.
- The experiments to evaluate the effect of the adversary's location show that if the location of the adversary is too far from the target, the attack would have a lower accuracy, yet still would be viable as long as the adversary has enough bandwidth to execute the attacks.
- We show that for apps that have weaker obfuscation mechanisms in place, our attacks outperform DeepCorr, a recent Deep Learning classifier. But, in case of the apps for which our attack methods have lower accuracies possibly as a result of better obfuscation, we see that DeepCorr outperforms our statistical attack methods.
- We see that using Tor with no additional obfuscation as well as using a VPN does not significantly counter our attacks, however, adding background traffic when tunneling through Tor and VPN reduces the accuracy of the attack and the most reduction is when Tor's obsf4 obfuscator is used.

## Components

- The attack algorithms can be found in [`attack algorithms`](./attack%20algorithms) directory.
- The details of IMProxy countermeasure can be found in [`IMProxy`](./IMProxy) directory.
- Our dataset of collected traffic and message traces is obtainable at [UMass Trace Repository](https://traces.cs.umass.edu/). The documentation for the dataset can be found in [`dataset`](./dataset/).
- The code for the NDSS Symposium 2020 paper is now available in [`NDSS Symposium 2020 Paper`](NDSS%20Symposium%202020%20Paper) directory.
