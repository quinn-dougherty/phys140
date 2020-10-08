from math import sin, cos, degrees, radians

theta = radians(18)
sled = 60 # newtons

mu_s = 0.25
mu_k = 0.13

g = 9.80665

m = sled / g

F_n = m * g * cos(theta)

f_s_max = mu_s * F_n

F_min_1 = m * g * sin(theta) - f_s_max


if __name__=="__main__": 
	print("a in newtons: ", F_min_1 - m*g*(sin(theta) + mu_s*cos(theta)))
	print("b in newtons: ", m*g*(sin(theta) + mu_s * cos(theta)))
	print("c in newtons: ", m*g*sin(theta) + mu_k * F_n)
