
head_above_heart = 1.9 # m
heart_above_feet = 2.19 # m 

gauge_pressure_at_heart = 252 # torr

blood_density = 1.06e3 # kg / m / m / m

g = 9.80665

p_brain = gauge_pressure_at_heart - blood_density * g * head_above_heart / 133.33

p_feet = gauge_pressure_at_heart + blood_density * g * heart_above_feet / 133.33



if __name__=="__main__":
	print(p_brain)
	print(p_feet)
	print(p_feet - p_brain)
