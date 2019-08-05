#!/user/bin/python
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *
import time

if len(sys.argv)!=4:
    print("Usage - ./arp_disc.py [interface]")
    print("Example - ./ arp_disc.py eth0")
    print("Example will perform an ARP scan of the local subnet to which eth0 is assigned")
    sys.exit()

ip=sys.argv[1]
start=int(sys.argv[2])
end=int(sys.argv[3])

for port in range(start,end):
    a=sr1(IP()/UDP(),timeout=5,verbose=0)
    time.sleep(1)
    if a==None:
        print(port)
    else:
        pass
