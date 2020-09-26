from math import sqrt

g = 9.81 

h = 0.589
t = 0.180

initial_speed = sqrt((h/t)**2 + 2 * g * h)



if __name__=="__main__": 
	print("initial speed: ", initial_speed)
	print("")
