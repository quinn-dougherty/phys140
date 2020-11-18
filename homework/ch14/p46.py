from math import sqrt

depth = 0.57 # m 
ratio = 0.32

g = 9.80665

a = g * (1 / ratio - 1) # m / s / s

v = sqrt(2 * a * depth)

if __name__=="__main__":
	print(v ** 2 / 2 / g)
