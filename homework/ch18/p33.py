
heater = 56 # kW
volume = 130 # L
from_cels = 23 # celsius
to_cels = 35 # celsius

specific_heat_water = 4186 # J / kg / K
density_of_water = 1 # g / cm / cm / cm

answer = specific_heat_water * 1000 * volume * (1 / 1000) * (to_cels - from_cels) / (heater * 1000) / 60

if __name__=="__main__":
	print(answer * 60)
