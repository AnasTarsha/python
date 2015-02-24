ip_sub = raw_input ("Enter your subnet")

out = ip_sub.split(".")

s = out + ['0']
s_new = ".".join(s)

fb='FIRST_OCTET_BINARY'
fh='FIRST_OCTET_HEX'
n='NETWORK_NUMBER'
print "%-20s %-20s %-20s" %(n,fb, fh)
print "%-20s %-20s %-20s" %(s_new, bin(int(s_new[0])), hex(int(s_new[0]))) 
