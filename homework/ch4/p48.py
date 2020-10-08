from math import sin, radians, cos
from utils import length, angle, angle2, smult

y0 = 20
y = 0
theta = radians(68)
t = 4.6
v0 = (9.81 * t**2 / 2 - y0) / t / sin(theta)

d = v0 * cos(theta) * 4.6

v0_vec = [v0 * cos(theta), v0 * sin(theta) - 9.81 * 4.6]

if __name__=="__main__": 
	print("distancex: ", d)
	print("magnitude of velocity: ", length(v0_vec))
	print("angle of velocity (tan): ", angle2(v0_vec, "degrees"))
	print("angle of velocity (cos): ", angle(v0_vec, "degrees"))


