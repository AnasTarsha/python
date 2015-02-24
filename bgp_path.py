#Python script that prints the network along with the BGP AS path

# Anas Tarsha
# http://anastarsha.com


entry = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"

entry = entry1.split() 

network = entry[1]
as_path = entry[4:-1]
print "%-20s %s" %(network, as_path)
