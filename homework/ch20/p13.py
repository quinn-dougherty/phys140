from math import log 

L = 309.5 # K
R = 298.5 # Kelvin

energy_transferred_for_equilibrium = 240 # J

specific_heat_copper = 386 # J / kg * K

T_final = (L + R) / 2

m = energy_transferred_for_equilibrium / specific_heat_copper / (T_final - R)

delta_S_L = m * specific_heat_copper * log(T_final / L)

delta_S_R = m * specific_heat_copper * log(T_final / R)

if __name__=="__main__":
	print(delta_S_L)
	print(-delta_S_L)
	print(delta_S_R)
	print(-delta_S_R)
	print(delta_S_L + delta_S_R)
	print(0)
