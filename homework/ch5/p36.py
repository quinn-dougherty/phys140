from math import sin, radians

theta = radians(8.5)
mass = 42.4
accel = 0.148


if __name__=="__main__": 
	print("a: ", mass * 9.81 * sin(theta))
	print("T = ", mass * accel + mass * 9.81 * sin(theta))

