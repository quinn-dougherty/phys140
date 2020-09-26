from utils import length, vecadd, angle, smult
from math import pi, sin, cos, radians, degrees

theta1 = 35 
theta2 = theta1 + 109

uplusv = smult(11, [
	cos(radians(theta1)) + cos(radians(theta2)), 
	sin(radians(theta1)) + sin(radians(theta2))
])

if __name__=="__main__": 
	print(uplusv)
	print(length(uplusv))
	print(angle(uplusv, "degrees"))
