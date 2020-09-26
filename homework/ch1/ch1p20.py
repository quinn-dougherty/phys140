from utils import print_float3

volume_in_gallons = 187
rate_in_gallons_per_minute = 2.0

gallon_inchescubed_conversion_factor = 231
water_density_kg_per_meterscubed = 1000

volume_cubic_inches = volume_in_gallons * gallon_inchescubed_conversion_factor

inches_to_cm_conversion_factor = 2.54

volume_cubic_cm = volume_cubic_inches * inches_to_cm_conversion_factor**3
volume_cubic_m = volume_cubic_cm / 100**3

mass_required_to_fill_bottle = volume_cubic_m * 1000

rate_in_kilograms_per_minute = rate_in_gallons_per_minute / water_density_kg_per_meterscubed

minutes_required_to_fill_bottle = mass_required_to_fill_bottle / rate_in_kilograms_per_minute

years_required_to_fill_bottle = minutes_required_to_fill_bottle / 60 / 24 / 365

if __name__=="__main__":
	print_float3("Volume of bottle in cubic inches", volume_cubic_inches) 
	print_float3("Volume of bottle in cubic centimeters", volume_cubic_cm)	
	print_float3("Volume in cubic meters", volume_cubic_m)
	print_float3("Mass required to fill bottle (water)", mass_required_to_fill_bottle)
	print_float3("Rate in kg per minute", rate_in_kilograms_per_minute)
	print_float3("Minutes required to fill bottle", minutes_required_to_fill_bottle)	
	print_float3("Years required to fill bottle", years_required_to_fill_bottle)	
