m = 74 # kg
vt = 64 # m/s
F_snow = 1.3e5 # N
g = 9.80665 # m/s/s

d = m * vt**2 / 2 / (F_snow - m * g)



if __name__=="__main__":
	print(d)
	print(- m * vt)
