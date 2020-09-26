from utils import length, angle2, smult, vecadd, angle
from math import cos, sin, radians

thetaC = radians(180+11.1)
thetaA = radians(40.1)
C = smult(16.2, [cos(thetaC), sin(thetaC)])
minus_A = smult(-1, smult(12, [cos(thetaA), sin(thetaA)]))

B = vecadd(C, minus_A)



if __name__=="__main__": 
	print(B)
	print("magnitude: ", length(B))
	print("angle (cos): ", angle(B, "degrees"))
	print("angle (tan): ", angle2(B, "degrees"))
	print("angle (again): ", 180 + angle2(B, "degrees"))
