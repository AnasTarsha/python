#Python script that convers the first octet of an IP address from decimal to binary

# Anas Tarsha
# http://www.anastarsha.com

ip_addr = raw_input ("Enter your IP address")
octets = ip_addr.split(".")

print "%10s %10s" %(bin(int(octets[0])),bin(int(octets[1]))) 
