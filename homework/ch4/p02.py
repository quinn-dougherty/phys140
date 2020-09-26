from utils import dot, length, vecadd, smult, angle

v = [-1.1, 1.5] # a z coord of 0
u = [6.6, 0]



if __name__=="__main__": 
	print("length: ", length(v))
	print("angle: ", angle(v, "degrees"))
	w = vecadd(u, smult(-1, v))
	print("length_displacement: ", length(w))
	print("angle_displacement: ", angle(w, "degrees"))


