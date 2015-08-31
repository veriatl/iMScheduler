SZ=4

def toStrings(MAP):
	map(bin2str, MAP.values())
	
def bin2str(ELEM):
	format(SZ,bin(ELEM.as_long()))[2:]
	
	
x = {"a": 0b00, "b": 0b11}

print toStrings(x)