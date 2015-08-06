
# remove the char at position of s
def remove(s, pos):
	return s[0:pos]+s[pos+1:]

# remove positions in toDelPos from each element of strings
def removePos(strings, toDelPos):
	toDelPos.sort(reverse=True)
	l = []
	for s in strings :
		for removePos in (toDelPos):
			s = remove(s, removePos)
		l.append(s)
	return l

# which pos are 0 in s
def indexMapping(s):
	r = []
	for i,v in enumerate(s):
		if v == '0':
			r.append(i)
	return r