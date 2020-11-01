
aorta_gauge_pressure = 100 # torr
g = 9.80665
centripetal_accel = 3.6 * g # m / s / s

radius = 31 # cm

blood_density = 1.06e3 # kg / m / m / m 

if __name__=="__main__":
	print(
		aorta_gauge_pressure 
		- 
		blood_density * centripetal_accel * (radius * 0.01) / 133
	)
