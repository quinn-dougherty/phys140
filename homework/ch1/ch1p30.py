from utils import print_float3

def m(t: float) -> float: 
	"""t > 0 in seconds, m in grams"""
	return 4.6*t**0.8 - 3.3*t + 22

def mprime(t: float) -> float: 
	"""t > 0 in seconds, m in grams
	first derivative of m"""
	return 0.8*4.6*t**(0.8-1) - 3.3

time_water_mass_greatest = (4.6*0.8/3.3)**5

greatest_mass = mprime(time_water_mass_greatest)

if __name__=="__main__": 
	print_float3("At what time is mass greatest", time_water_mass_greatest)
	print_float3("what is that greatest mass?", greatest_mass)
	print_float3("rate of mass change at 2.1s (kg/min)", 3*mprime(2.1)/5)
	print_float3("rate of mass change at 4.9s (kg/min)", 3*mprime(4.9)/5)
	
