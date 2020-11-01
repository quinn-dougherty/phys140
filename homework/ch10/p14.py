
angular_vt1 = 6.3 # revolutions / s
revolutions = 65
angular_vt2 = 16 # revolutions / s

alpha = (angular_vt2 ** 2 - angular_vt1 ** 2) / 2 / revolutions

delta_t2 = 2 * revolutions / (angular_vt1 + angular_vt2)

delta_t1 = angular_vt1 / alpha

theta = angular_vt1 ** 2 / 2 / alpha

if __name__=="__main__":
	print(alpha)
	print(delta_t2)
	print(delta_t1)
	print(theta)
