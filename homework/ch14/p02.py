
A = 65.4 # cm ** 2
A_m = A / 100**2

F = 240 # N 

p0 = 1e5

pi = p0 - F / A_m

if __name__=="__main__":
	print(pi)

