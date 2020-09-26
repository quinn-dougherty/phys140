from utils import length, angle

u = [-3.1, 2.9-4.4]

if __name__=="__main__": 
	print("length: ", length(u))
	print("angle: ", angle(u, "degrees"))
	print("true angle: ", 180 + (180 - angle(u, "degrees")))
