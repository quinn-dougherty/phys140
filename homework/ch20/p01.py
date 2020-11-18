from math import log


gas = 4 # mol

ratio = 7

T = 480 # kelvin

work = gas * 8.31 * T * log(ratio)

if __name__=="__main__":
	print(work) # Joules
	print(work / T) # J / K 
	print(0) # J / K 
