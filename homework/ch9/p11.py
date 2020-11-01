from utils import vecadd, smult

olive = 0.14
nut = 0.64

olive_pos = [0, 0]
nut_pos = [0.88, 1.9]

t = 6.6

Fo = (4.7, 1.2)
Fn = (-2.8, -1.9)

total_force = vecadd(Fo, Fn)
a = smult(1 / (olive + nut), total_force)

delta_r = smult(t**2 / 2, a)

if __name__=="__main__": 
	print(delta_r)

