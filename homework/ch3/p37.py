from utils import dot, vecadd, cross

a = [2, -1, -2]
b = [5, -3, 3]
c = [3, -1, -3]

if __name__=="__main__": 
	print("a ", dot(a, cross(b, c)))
	print("b ", dot(a, vecadd(b, c)))
	print("cde ", cross(a, vecadd(b, c)))
