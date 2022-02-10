from netfilterqueue import NetfilterQueue
from scapy.all import *
from numpy.random import default_rng
import numpy as np
import time

rng = default_rng()

average_delay = 0.08 # seconds

def delay(packet):
    exp_delay = rng.exponential(average_delay)
    time.sleep(exp_delay)
    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, delay)

try:
    print("[*] waiting for data")
    nfqueue.run()
except KeyboardInterrupt:
    print('')


nfqueue.unbind()