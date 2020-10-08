from utils import vecadd, smult


mass = 3.2
x = 1.3
y = 6.4
F1 = [x, y]
F21 = [-x, -y]
F22 = [-x, y]
F23 = [x, -y]

if __name__=="__main__": 
	print("a: ", smult(1/mass, vecadd(F1, F21)))
	print("b: ", smult(1/mass, vecadd(F1, F22)))
	print("c: ", smult(1/mass, vecadd(F1, F23)))

