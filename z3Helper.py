from z3 import *

# Return the first "M" models of formula list of formulas F 
def get_models(F, M):
	result = []
	s = Solver()
	
	# configure solver
	s.set(unsat_core=True)
	s.set(timeout=50) 
	s.set(':models', True) 
	s.set(':auto-config', False) 
	s.set(':smt.bv.enable_int2bv',True) 
	
	# add F to solver s.
	s.add(F)

	while True:
		if s.check() == sat:
			if len(result) >= M:
				return result
			m = s.model()
			result.append(m)
			# Create a new constraint the blocks the current model
			block = []
			for d in m:
				# d is a declaration
				if d.arity() > 0:
					raise Z3Exception("uninterpreted functions are not supported")
				# create a constant from declaration
				c = d()
				if is_array(c) or c.sort().kind() == Z3_UNINTERPRETED_SORT:
					raise Z3Exception("arrays and uninterpreted sorts are not supported")
				block.append(c != m[d])
			s.add(Or(block))
		else:
			return result
			


# Generate a solution 
def get_model(F):
	result = []
	s = Solver()
	
	# configure solver
	s.set(unsat_core=True)
	s.set(timeout=50) 
	s.set(':models', True) 
	s.set(':auto-config', False) 
	s.set(':smt.bv.enable_int2bv',True) 
	
	# add F to solver s.
	s.add(F)
	
	if s.check() == sat:
		return s.model()
	else:
		return None
	