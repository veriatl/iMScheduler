# TODO: 
# DECTECT CONFLICT WITHIN PERSON
# MAP REDUCED SZ TO ORG SIZE


# Imports
from z3 import *
from binary import *
from z3Helper import *
from string import *




# Global Configuration
SZ=8
# students' availability, 1 for could attend, 0 for a firm not able to attend.
cfg1 = '10001000'
cfg2 = '10000000'
cfg3 = '10111100'
cfg4 = '11000010'

cfgs = [cfg1,cfg2,cfg3,cfg4]


		
def _prettyPrint(list):
	for key in list: 
		print "%s -> \t %s" % (key, padZero(bin(list[key].as_long())[2:],SZ))


# return a list of list, each list (a,b,c...) specifies X is not available for a,b,c...
def readAvailablity(l):
	r = []
	for e in l:
		temp = []
		for id, c in enumerate(e):
			if c == '0':
				temp.append(toBinPos(SZ, id))
		r.append(temp)
	return r

# generate the constrains for non availability	
def genNonAvailCond(nonAvail, candidate):
	r = []
	for i, v in enumerate(candidate):
		r.append(zip(pad(v, len(nonAvail[i])), nonAvail[i]))
	return r

# a course, identified by POS, require N student from STUDLIST
def courseRequire(POS, STUDLIST, N):
	posList = [POS] * len(STUDLIST)
	return opAfterSum(posList, STUDLIST, N)
	
# a student (STUD) can chose up to N courses from mutual exclusion list (EXLIST) 
def personalConflict(EXLIST, STUD, N):
	studList = [STUD] * len(EXLIST)
	return opAfterSum(EXLIST, studList, N)

	

	
def main():
	# SAFE STATE STARTS, FUN STAFF
	global cfg
	
	zerosPos = (indexMapping(orTogether(cfgs, SZ)))
	GHOST = BitVec('__GHOST',SZ)	# To fulfil non availability, make sure a partial solution can be generated
	
	A = BitVec('A', SZ)
	B = BitVec('B', SZ)
	C = BitVec('C', SZ)
	D = BitVec('D', SZ)	
	
	# put constrains into a formula
	F = []

	# hard constrains: 
	F.append(A|B|C|D|GHOST == All(SZ))
	
	# GHOST construction
	for i in range(0, SZ):
		if i in zerosPos:
			F.append(mustOne(GHOST, toBinPos(SZ, i)))
		else:
			F.append(mustZero(GHOST, toBinPos(SZ, i)))
	

	# non availability for each student processing
	nonAvail = readAvailablity(cfgs)
	conds = genNonAvailCond(nonAvail, [A,B,C,D])
	for cand in conds:
		for tuple in cand:
			F.append(mustZero(tuple[0],tuple[1]))
	
	# soft constrains: 
	F.append(courseRequire(7, [A,B,C,D], 4))
	F.append(personalConflict([7,3],A,1))
	_prettyPrint(get_models(F,100)[0]);

	
	





	




	# iterate solutions
	


	
	
	
	
	
if __name__ == '__main__':
    main()