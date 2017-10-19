from multiprocessing import Pool
from socket import *
import os,random

udpSocket = socket(AF_INET, SOCK_DGRAM)
def worker():
	senddata = "1:123456:老王:machine:32:你好啊"

	for lastip in range(1,255):#（起始主机号，结束主机号）注意结束主机号为开区间
		destIP = "192.168.25." + str(lastip)
		destPort = 2425
		udpSocket.sendto(senddata.encode("GB2312"), (destIP, destPort))

pool = Pool(30)
for i in range(0,10):#（0，发送次数10）
	pool.apply_async(worker,())
	
print("----start----")
pool.close() 
pool.join() 
print("-----end-----")