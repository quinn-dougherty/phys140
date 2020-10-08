
mass = 1.9 # kg
v = [23, 32]

gravity = 9.80665

t = 4.1

delta_y = v[1] * t - 0.5 * gravity * t**2



if __name__=="__main__":
	print(mass * gravity * delta_y)
