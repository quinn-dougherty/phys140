def a(v, v_s, L):
	return v * L / v_s - L

def b(v, v_s, L): 
	d = a(v, v_s, L)
	x = v_s / (v - v_s) * 2 * d
	t = x / v_s
	return (x - L) / t

if __name__=="__main__": 
	print(a(28, 5.1, 13))
	print(b(28, 5.1, 13))
