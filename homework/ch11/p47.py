
mass_coef = 2.97 # times m
radius = 0.305
velocity = 0.197

# omega = lambda m: velocity / (mass / m + 1) / radius

omega = velocity / (mass_coef + 1) / radius

if __name__=="__main__":
	print(omega)

