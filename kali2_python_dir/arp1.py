#!/user/bin/python
#导入日记包记录运行状态
import logging
import subprocess
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
#win系统下没安装scapy 报错 可以通过pip install scapy 解决
from scapy.all import*


#shell语言 py命令后接本文件还有哪一个网卡    不足够参数就报错
if len(sys.argv)!=2:
    print("Usage - ./arp_disc.py [interface]")
    print("Example - ./ arp_disc.py eth0")
    print("Example will perform an ARP scan of the local subnet to which eth0 is assigned")
    sys.exit()

#获取命令中的网卡
interface=str(sys.argv[1])


#通过调用ifconfig+eth 获取本网络号，准备进行一个网段的扫描
ip=subprocess.check_output('ifconfig'+interface+"grep 'inet addr' | cut -d' ' -f 1",shell=True).strip()

#获取将提取的出来的ip地址拼凑成网络号前缀
perfix=ip.split('.'[0])+ip.split('.')[1]+ip.split('.')[2]+'.'


'''
sr1是scapy里面用来发包的函数
timeout超时操作
verbose是否显示报错详细信息

'''
for addr in range(0,254):
    answer=sr1(ARP(pdst=perfix+str(addr)),timeout=0.1,verbose=0)
    if answer==None:
        pass
    else:
        print(perfix+str(addr))


