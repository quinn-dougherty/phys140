from math import radians, degrees, sin, cos, sqrt

I = 0.0165 # kg * m^2
r = 0.2 # m
theta = radians(27.9)
K_total_init = 7 # J

delta_x = 0.85 # m

M = 3 * I / 2 / r**2
m = 1
K_rot_over_K = 1/3 / (1/2 + 1/3)

K_rot = K_rot_over_K * K_total_init

omega = sqrt(3 * K_rot / M / r**2)

h = delta_x * sin(theta)

g = 9.80665

K_f = K_total_init / M / g / h

omega_f = sqrt(0.4 * 3 * K_f / M) / r

if __name__=="__main__":
	print(K_rot)
	print(r * omega)
	print(K_f)
	print(omega_f * r)
