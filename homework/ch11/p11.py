
F_app = 9.2 # newtons
mass = 9.1 # kg
radius = 0.34 # m
acceleration_com = 0.31 # m/s/s

alpha = abs(acceleration_com) / radius

frictional_force = F_app - mass * acceleration_com



if __name__=="__main__": 
	print(frictional_force)
	print(radius * frictional_force / alpha)
