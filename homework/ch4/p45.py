from utils import length, angle
from math import tan, cos, radians, degrees, sqrt, atan

def equation_425(theta0, v0): 
	theta0 = radians(theta0)
	return lambda x: x * tan(theta0) - 9.81 * x**2 / 2 / (v0 * cos(theta0))**2

def x(theta, m, v0): 
	theta = radians(theta)
	return (tan(theta) - m) * 2 * v0**2 * cos(theta)**2 / 9.81

d = [6, 3.6]
slope = d[1] / d[0]


theta0 = 42
v0 = 6

length_ramp = length(d)
angle_ramp = angle(d, "degrees")

my_x = x(theta0, slope, v0)

y = slope * my_x

magnitude = sqrt(y**2 + my_x ** 2)

angle = degrees(atan(slope))

if __name__=="__main__": 
	print(length_ramp)
	print(angle_ramp)
	print(equation_425(theta0, v0))
	print(x(theta0, slope, v0))
	print("magnitude: ", magnitude)
	print("angle: ", angle)
