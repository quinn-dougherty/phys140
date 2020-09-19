from utils import vecadd, length
from math import sin, cos, degrees, radians, acos

a = [2, 3]
b = [4 * cos(radians(65)), 4 * sin(radians(65))]
c = [-4, -6]
d = [5 * cos(radians(-235)), 5 * sin(radians(-235))]

apbpcpd = vecadd(vecadd(a, b), vecadd(c, d))
apbpcpd_mag = length(apbpcpd)
costheta = apbpcpd[0] / apbpcpd_mag
theta = acos(costheta)

if __name__=="__main__": 
	print("a ", apbpcpd)
	print("b ", apbpcpd_mag)
	print("c ", degrees(theta))
