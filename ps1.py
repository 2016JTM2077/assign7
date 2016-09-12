#!/usr/bin/python

inp=raw_input()
inp2=inp.split( );
l=len(inp)

default_d={}


#--------------------------------------DIctionary--------------------------------------------
for i in inp2:
	p=inp2.count(i)
	default_d.update({i: p})


#-------------------------------------Generating top 3 frequent words------------------------
out= sorted(default_d.iteritems(), key=lambda x:-x[1])[:3]
for field in out :
	print "{0}: {1}".format(*field)


##permutation program

from itertools import permutations
for i in inp2:
	z=len(i)
	if(z<=1):
		print i
	else:
		iteration = [''.join(pic) for pic in permutations(i)]
		print iteration[1]
