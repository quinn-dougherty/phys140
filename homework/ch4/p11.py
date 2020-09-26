from utils import call, angle2

r = [lambda t: 2*t**3 - 4 * t, lambda t: 4 - t**4]

v = [lambda t: 2 * 3 * t**2 - 4, lambda t: - 4 * t**3]

a = [lambda t: 2 * 3 * 2 * t, lambda t: - 4 * 3 * t**2]


if __name__=="__main__": 
	print(call(r, 3))
	print(call(v, 3))
	print(call(a, 3))
	print(angle2(call(v, 3), "degrees"))
