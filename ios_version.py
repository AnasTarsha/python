ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

sections = ios.split(",")
version = sections[2].split(" ")
print 'IOS version = ' + '"' + version[-1] +'"'
