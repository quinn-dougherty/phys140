from utils import format_float2

acre = 43560 # one acre = 43560 feet^2
rain_inches = 2.7 # inches
rain_feet = rain_inches/12



town_area = 49 # km^2

# 1 km = 39370.08 inches
# 1 km = 3280.84 ft
km_feet_conversion_factor = (1000/0.3048)**2
feet_acre_conversion_factor = 43560 # one acre = 43560 feet^2
town_area_feet = town_area * km_feet_conversion_factor
town_area_acres = town_area_feet / feet_acre_conversion_factor



if __name__=="__main__":
	print(f"Town area in feet: {town_area_feet}")
	print(f"Town area in acres: {town_area_acres}")
	print(f"Rain in feet: {rain_feet}")
	answer = rain_feet * town_area_acres
	print(f"Answer: {format_float2(answer)}")	
	print()
