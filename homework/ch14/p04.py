V1 = 0.666 # L 
rho1 = 3.34 # g/cm /cm /cm

V2 = 0.891 # L 
rho2 = 1.11 # g / cm / cm / cm

V3 = 0.453 # L
rho3 = 0.697 # g / cm / cm / cm

one_liter = 1000 # cm * cm * cm

g = 9.80665

if __name__=="__main__":
	print(g * (V1 * rho1 + V2 * rho2 + V3 * rho3))
