from math import radians, sin, cos

force = 0.5
theta = radians(20)

mu_s1 = 0.62
mu_k1 = 0.52

mu_s2 = 0.44
mu_k2 = 0.31

f_s_max_1 = mu_s1 * (1 - mu_k1 * sin(theta))
f_s_max_2 = mu_s2 * (1 - mu_k2 * sin(theta))

def accel(mu_k: float) -> float: 
	return force * 9.80665 * (cos(theta) + mu_k * sin(theta)) - mu_k * 9.80665
if __name__=="__main__": 
	print("a: ", 0 if force * cos(theta) < f_s_max_1 else accel(mu_k1))
	print("b: ", 0 if force * cos(theta) < f_s_max_2 else accel(mu_k2))
