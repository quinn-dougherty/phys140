
rest = 15 # celsius
l = 30 # cm

new_temp = 66 # celsius

brass_linearexpansion_coef = 19e-6 # C

if __name__=="__main__":
	print(12 * brass_linearexpansion_coef * l**2 * (new_temp - rest))

