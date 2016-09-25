#! /usr/bin/python

import random

s = open('occupations.csv').read()
lines = s.split('\r\n')[1:-1]
dic = {}
def genDict():
	global dic
	xd = lines
	for line in xd:
		comma = line.rfind(',')
		key = line[:comma].strip('"')
		value = float(line[comma + 1:])
		dic[key] = value
	
genDict()

def weightedOccupation():

	total = dic.pop('Total')
	r = random.randrange(int(10 * total)) / 10.0
	#print 'Random: ' + str(r)
	cur = 0
  
	for key in dic:
		cur += dic[key]
		#print 'Cur: ' + str(cur) + ' ' + key
		if r < cur:
			return key

    



