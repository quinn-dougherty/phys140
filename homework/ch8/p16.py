from math import sqrt

g = 9.81
m = 738 * 10**-3# kgrams
k = 380
x = 0.192

W_s = -1/2 * k * x**2

h0 = k * x**2 / 2 / (m) / g - x

h0_prime = 3 * h0

x_quadratic_formula = m * g / k + sqrt(m**2 * g**2 + 2 * k * m * g * h0_prime) / k
if __name__=="__main__": 
	print("W_s: ", W_s)
	print("h0: ", h0)
	print("x: ", x_quadratic_formula) 
