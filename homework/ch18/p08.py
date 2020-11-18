
rest = 16 # celsius
l = 32 # cm

new_temp = 69 # celsius

brass_linearexpansion_coef = 19e-6 # C

if __name__=="__main__":
	print(12 * brass_linearexpansion_coef * l**2 * (new_temp - rest))

