from math import pi 

cyl_h = 6.4 # cm

cyl_area_faces = 13 # cm * cm
cyl_area_faces_m = cyl_area_faces / 100**2

cyl_density = 0.286 # g / cm / cm / cm
cyl_density_kg_m = cyl_density * 1000 # kg / m / m / m

h_above_water = 1.8 # cm

water_density = 998 # kg / m / m / m
iron_density = 7900 # kg / m / m / m

V_c = cyl_h * cyl_area_faces / 100**3

V_s = (cyl_h - h_above_water) * cyl_area_faces / 100**3

g = 9.80665

V_b = (water_density * g * V_s - cyl_density_kg_m * g * V_c) / (iron_density * g - water_density)

r = (3 * V_b / 4 / pi) ** (1/3)

if __name__=="__main__":
	print(r)
