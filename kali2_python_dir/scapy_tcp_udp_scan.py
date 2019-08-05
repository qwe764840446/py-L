#!/user/bin/python
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *


if len(sys.argv)!=2:
    print("Usage - ./arp_disc.py [interface]")
    print("Example - ./ arp_disc.py eth0")
    print("Example will perform an ARP scan of the local subnet to which eth0 is assigned")
    sys.exit()


address=str(sys.argv[1])
perfix=address.split('.')[0]+'.'+address.split('.')[1]+'.'+address.split('.')[2]+'.'

for addr in range(1,255):
    response=sr1(IP(dst=perfix+str(addr))/UDP(dport=33333),timeout=0.1,verbose=0)
    try:
        if int(response[IP].proto)==1:
            print(perfix+str(addr))
    except:
        pass




