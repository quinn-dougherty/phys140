from math import sqrt

temp = 2.27e6 # kelvin
pressure = 0.0405 # Pa

electron = 9.11e-31 # kg
k = 1.38e-23 # J / K

answer = sqrt(3 * k * temp / electron)

if __name__=="__main__":
	print(answer)
