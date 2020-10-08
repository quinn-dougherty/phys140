from math import sqrt

mass = 90 # kg
height = 5.5 # m 
sandbag = 66 # kg
m_sys = mass + sandbag
gravity = 9.80665

accel = (mass - sandbag) * gravity / (mass + sandbag)

velocity = sqrt(2 * accel * height)


if __name__=="__main__": 
	print(velocity)
