
length1 = 10.992 # cm

temp1 = 19 # C

length2 = 11.032 # cm

temp2 = 100 # C

length3 = 11.017 # cm

alpha = (length2 - length1) / (length1 * (temp2 - temp1))

delta_L = length2 * alpha * (0 - 100)

delta_T = (length3 - length1) / alpha / length1

if __name__=="__main__":
	print(length1 + delta_L) # cm
	print(temp1 + delta_T) # celsius
