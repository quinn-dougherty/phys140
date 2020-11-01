from math import pi 

depth = 56.6 # m 
radius = 2.16 # m
height = 3.26 # m

seawater_density = 1040 # kg / m / m / m

surface_temperature = 23.6 # celsius

submerged_water_temperature = -32.1 # celsius

air_volume = pi * radius**2 * height # m^3

new_h = 56.6

p0 = 1

g = 9.80665

p = p0 + seawater_density * g * new_h / 1.01e5

surface_temperature_kelvin = 296.75 # 295.05 # kelvin
submerged_water_temperature_kelvin = 241.05 # 245.85 # kelvin

p1 = p0

V2 = air_volume * p1 * submerged_water_temperature_kelvin / p / surface_temperature_kelvin


moles_released = p * 1.01e5 * (air_volume - V2) / 8.31 / submerged_water_temperature_kelvin

if __name__=="__main__":
	print(air_volume)
	print(V2)
	print(moles_released)
