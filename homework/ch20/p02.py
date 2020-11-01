from math import log


delta_S = 37.6 # J/K
expansion_temp = 87.4 # celsius

v0 = 1.4 # L
v1 = 3.48 # L


if __name__=="__main__":
	print(delta_S / 8.31 / log(v1 / v0))
