from utils import angle2, length
from math import radians, sin, cos, acos

Fa = 224 # newtons
Fc = 180 # newtons

theta = radians(137-90)

phi = acos(Fa * cos(theta) / Fc)

Fb = Fa * sin(theta) + Fc * sin(phi)
Fb_prime = Fa * sin(theta) + Fc * sin(0 - phi)

if __name__=="__main__": 
	print("magnitude of Fb: ", Fb)
	print("Fa * cos theta: ", Fa * cos(theta))
	print("magnitude of Fb': ", Fb_prime)

