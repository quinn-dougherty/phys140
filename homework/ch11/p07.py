from math import sin, cos, degrees, radians, sqrt
r = 15 # cm
r *= 1e-2 # m
m = 9 # kg
L = 6.6 # m
theta = radians(38) # degrees
H = 4 # m
g = 9.80665

omega = sqrt(4 * g * H / 3) / r

v0 = r * omega

v0x = v0 * cos(theta)
v0y = v0 * sin(theta)

t = (-v0y + sqrt(v0y**2 + 2 * g * H)) / g

x = v0x * t

if __name__=="__main__":
	print(omega)
	print(x)
