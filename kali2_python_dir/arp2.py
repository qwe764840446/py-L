#!/user/bin/python
#导入日记包记录运行状态
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
#win系统下没安装scapy 报错 可以通过pip install scapy 解决
from scapy.all import*

#shell语言 py命令后接本文件还有哪一个网卡    不足够参数就报错
if len(sys.argv)!=2:
    print("Usage - ./arp_disc.py [interface]")
    print("Example - ./ arp_disc.py eth0")
    print("Example will perform an ARP scan of the local subnet to which eth0 is assigned")
    sys.exit()


#调用ip地址的文件
filename=str(sys.argv[1])
#open函数打开
file=open(filename,'r')

for addr in file:
    answer=sr1(ARP(psdt=addr.splip()),timeout=0.1,verbose=0)
    if answer == None
        pass
    else:
        print(addr.strip())

file.close()









