from utils import vecadd, smult 

a = [4, -3, 1]
b = [-1, 1, 4]

if __name__=="__main__": 
	print("a ", vecadd(a, b))
	print("b ", vecadd(a, smult(-1, b)))
	print("c ", vecadd(b, smult(-1, a)))

