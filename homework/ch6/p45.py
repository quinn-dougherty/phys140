
weight = 648 # newtons
F_N = 569 # newtons

F_c = weight - F_N # newtons

F_N_bottom = weight + F_N # newtons

F_c_prime = 4 * F_c



if __name__=="__main__": 
	print(F_c + weight)
	print(weight - F_c_prime)
	print(weight + F_c_prime)
