#Autor Tedezed
import os
listt = []
num = 1
net = raw_input("Network Address: ")
net = net.split(".")
net = net[0]+"."+net[1]+"."+net[2]+"."
while num <= 255 :
	numstr = str(num)
	comand = "ping -c 1 -n -i 0.2 -W 1 " + net + numstr
	comand = os.system(comand)
	if comand == 0:
		comand = net+numstr
		listt.append(comand)
	num = num + 1
print "List of addresses used in the network: "
for x in listt:
	print x

