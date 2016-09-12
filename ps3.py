#!/usr/bin/python

import sys

house=raw_input("Enter House number: ")
dist=raw_input("Enter District: ")
city=raw_input("Enter City: ")
state=raw_input("Enter State: ")

#-------------------Database--------------------------------

house_d={'a':'000','b':'001','c':'010','d':'011','e':'100'}
dist_d={'jaipur':'000','alwar':'001','sikar':'010','east delhi':'011','khandesh':'100'}
city_d={'jaipur':'000', 'delhi':'001' ,'alwar':'010','jodhpur':'011','bombay':'100'}
state_d={'rajasthan':'000','delhi':'001','maharashtra':'010'}

#-------------------Error generation if data is invalid and MODIFYING------

if dist not in dist_d:
	print "District not present in database"
	up=raw_input("Want to modify data?<yes/no>")
	if(up=='yes'):
		up_d={dist:'111'}
		dist_d.update(up_d)
	else:
		sys.exit()

if city not in city_d:
	print "City not present in database"
	up2=raw_input("Want to modify data?<yes/no>")
	if(up2=='yes'):
		up2_d={city:'111'}
		city_d.update(up2_d)
	else:
		sys.exit()

if state not in state_d:
	print "State not present in database"
	up3=raw_input("Want to modify data?<yes/no>")
	if(up3=='yes'):
		up3_d={state:'111'}
		state_d.update(up3_d)
	else:
		sys.exit()

#-------------------CC_NO---------------------------------

for key in dist_d:
	if (dist == key):
		c1 = dist_d[key]
#		print c1

for key1 in city_d:
	if (city == key1):
		c2 = city_d[key1]
#		print c2

for key2 in state_d:
	if (state == key2):
		c3 = state_d[key2]
#		print c3

ccno=c1+c2+c3

print "CC_NO= %s" %ccno

#-------------------Human readability code-----------------

s1=dist[0:2]+ "_" +city[0:2]+ "_" +state[0:2]
print "Human readability code: %s" %s1.upper()




	




