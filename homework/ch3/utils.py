from math import sqrt 

def dot(u: list, v: list) -> float: 
	assert len(u) == len(v)
	return sum(ui * vi for ui, vi in zip(u, v))

def length(u: list) -> float: 
	return sqrt(sum(ui**2 for ui in u))

def vecadd(u: list, v: list) -> list: 
	assert len(u) == len(v)
	return [ui + vi for ui, vi in zip(u, v)]

def cross(u: list, v: list) -> list: 
	assert len(u) == 3
	assert len(v) == 3
	return [
		u[1]*v[2] - u[2]*v[1], 
		- (u[0]*v[2] - u[2]*v[0]), 
		u[0]*v[1] - u[1]*v[0]
	]

def smult(k: float, u: list) -> list: 
	return [k*ui for ui in u]

