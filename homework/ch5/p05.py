from math import radians, sin, cos
from utils import length, angle2

F1 = 36 # newtons
F2 = 56 # newtons
F3 = 36 # newtons

theta1 = radians(30)
theta2 = radians(0)
theta3 = radians(-60)

mass = 115

coordinates = [
	F1 * cos(theta1) + F2 * cos(theta2) + F3 * cos(theta3), 
	F1 * sin(theta1) + F2 * sin(theta2) + F3 * sin(theta3)
]

if __name__=="__main__": 
	print("in ihat, jhat form: ", coordinates)
	print("length: ", length(coordinates))
	print("accel: ", length(coordinates) / mass)
	print("angle: ", angle2(coordinates, "degrees"))
