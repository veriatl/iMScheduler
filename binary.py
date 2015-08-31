
from z3 import *

import operator 
		
# Return True if F has exactly one model.
def exactly_one_model(F):
    return len(get_models(F, 2)) == 1			

# return all zero with size [sz]	
def Empty(sz):
	return BitVecVal(0, sz)

# return all one with size [sz]
def All(sz):
    return BitVecVal(2**sz - 1, sz)

def to_int(x):
    return ArithRef(Z3_mk_bv2int(x.ctx_ref(), x.as_ast(), 0), x.ctx)

# query pos in S
def query(S, pos):
    return Extract(pos,pos,S)
	
# bit at [pos] of [S] is 1
def mustOne(S, pos):
    sz = S.size()
    one = BitVecVal(1, sz)
    return S & (1 << pos) != Empty(sz)

# bit at [pos] of [S] is 0
def mustZero(S, pos):
    sz = S.size()
    one = BitVecVal(1, sz)
    return S & (1 << pos) == Empty(sz)
	
# bitwise [or_] the availability strings together, to check is there any [pos] is 0
def orTogether(l, sz):
	return list(padZero(bin(reduce(operator.or_, [int(x, 2) for x in l]))[2:],sz))

# pad binary string with 0 to have length of sz.
def padZero(str,sz):
	return "".join(pad('0',sz-len(str)))+str

# return a list, that padding with [elem] [time] times.	
def pad(elem, time):
	if time > 0:
		return [elem]+pad(elem,time-1)
	else:
		return []

# Natural position to binary position
def toBinPos(sz,i):
	return sz-1-i

# count how many of one in the given number of binary format
def countOnes(num):
	return bin(num).count("1")	
	
	
# the pos at each elem in LIST will 'op' to N, where 'op' could be LT, GT, LE, GE, EQ, NEQ, 	
def opAfterSum(POSLIST, VARLIST, N, OP):
	functor = (lambda x,y: ZeroExt(5, Extract(x,x,y)))
	red = reduce(lambda x, y: x+y, map(functor, POSLIST, VARLIST))
	return map(OP, [red], [N])[0]