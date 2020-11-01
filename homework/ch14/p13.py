
depth = 10.9 # km
seawater_density = 1024 # kg / m / m / m


if __name__=="__main__":
	print(seawater_density * 9.80665 * depth * 1000 / 1.01e5)
