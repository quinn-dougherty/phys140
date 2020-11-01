from math import sqrt

m = 1.8
g = 9.80665
L = 0.76

v0 = sqrt(2 * g * L)

v_bottom = sqrt(4 * g * L)
if __name__=="__main__":
	print(v0)
	print(v_bottom)
	print()
