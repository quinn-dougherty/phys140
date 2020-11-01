mass = 60 # kg
w = 0.4 # m
d = 0.4 # m 
mu_1 = 0.45
mu_2 = 1.10

g = 9.80665
F_N1 = mass * g / (mu_1 + mu_2)

h = (mass * g * (d + w) - mu_1 * F_N1 * w) / F_N1

if __name__=="__main__":
	print(F_N1)
	print(h)
