from math import pi 


r_o = 9.79e-2 # m
r_i = 8.62e-2 # m
rho = 783 # kg / m / m / m

V = 4 * pi * r_o ** 3 / 3

m = V * rho / 2

V2 = 4 * pi * (r_o**3 - r_i**3) / 3

if __name__=="__main__":
	print(m)
	print(m / V2)
