from math import log


delta_S = 39.2 # J/K
expansion_temp = 50.2 # celsius

v0 = 1.34 # L
v1 = 3.19 # L


if __name__=="__main__":
	print(delta_S / 8.31 / log(v1 / v0))
