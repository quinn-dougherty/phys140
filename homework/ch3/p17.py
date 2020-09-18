from utils import dot, length
from math import cos, acos, sin, degrees, radians, pi

mag = 47
a_direc = radians(33)
b_direc = radians(193)
c_direc = radians(311)

a_ihat = mag * cos(a_direc)
a_jhat = mag * sin(a_direc)

b_ihat = mag * cos(b_direc)
b_jhat = mag * sin(b_direc)

c_ihat = mag * cos(c_direc)
c_jhat = mag * sin(c_direc)

apbpc_ihat = a_ihat + b_ihat + c_ihat
apbpc_jhat = a_jhat + b_jhat + c_jhat

apbpc_mag = length([apbpc_ihat, apbpc_jhat])
apbpc_costheta = apbpc_ihat / apbpc_mag
apbpc_theta = acos(apbpc_costheta)

ambpc_ihat = a_ihat - b_ihat + c_ihat
ambpc_jhat = a_jhat - b_jhat + c_jhat

ambpc_mag = length([ambpc_ihat, ambpc_jhat])
ambpc_costheta = ambpc_ihat / ambpc_mag

ambpc_theta = acos(ambpc_costheta)

apbmc_ihat = a_ihat + b_ihat - c_ihat
apbmc_jhat = a_jhat + b_jhat - c_jhat

apbmc_mag = length([apbmc_ihat, apbmc_jhat])
apbmc_costheta = apbmc_ihat / apbmc_mag
apbmc_theta = acos(apbmc_costheta)


if __name__=="__main__": 
	print("a+b+c magnitude ", apbpc_mag)
	print("a+b+c theta ", degrees(apbpc_theta))
	print("a-b+c magnitude ", ambpc_mag)
	print("a-b+c theta ", degrees(ambpc_theta))
	print("a+b-c magnitude ", apbmc_mag)
	print("a+b-c theta ", degrees(apbmc_theta))
	
