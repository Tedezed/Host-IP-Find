#Autor Tedezed
import os
import commands

print "Network interface: "
print commands.getoutput("/sbin/ifconfig | egrep -o '^[a-z].......'")
intfz = raw_input('Enter the interface to use: ')
comand = "/sbin/ifconfig "+intfz+" | egrep -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | egrep -v '*(0|255)$'"
iphost = commands.getoutput(comand)
print "Your IP is: ", iphost
raw_input('Press to continue...')

net = iphost.split(".")
listt = []
num = 1
while num <= 255 :
	numstr = str(num)
	comand = "ping -c 1 -n -i 0.2 -W 1 " + net[0]+"."+net[1]+"."+net[2]+"." + numstr
	comand = os.system(comand)
	if comand == 0:
		comand = net[0]+"."+net[1]+"."+net[2]+"."+numstr
		listt.append(comand)
	num = num + 1
print "List of addresses used in the network: "
for x in listt:
	print x

