
mass = 60
mu_s = 0.53
gravity = 9.80665

F = mu_s * mass * gravity
mass -= 35

if __name__=="__main__": 
	print("F: ", F)
	print("F2: ", mu_s * mass * gravity)
