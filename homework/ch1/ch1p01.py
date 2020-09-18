from ..utils import format_float3
from math import pi 

earth_radius = 6.37e+6 # in meters
earth_radius /= 1000 # in kilometers

circumference = 2 * pi * earth_radius

surface_area = 4 * pi * earth_radius**2

volume = (4/3) * pi * earth_radius**3

if __name__=="__main__": 
	print(f"Circumference: {format_float3(circumference)}")
	print(f"Surface Area: {format_float3(surface_area)}")
	print(f"Volume: {format_float3(volume)}")
