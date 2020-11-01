from math import sqrt


m = 2.36 # kg
r = 0.382 # m
L = 2.08 # m
g = 9.80665 # m / s / s

T = m * g * sqrt(L**2 + r **2) / L # N

FN = T * r / sqrt(L**2 + r**2) # N

if __name__=="__main__":
	print(T)
	print(FN)

