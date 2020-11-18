
sample = 2.67 # mol
T_s = 415 # K

S_s = 21 # J/K

AUC = 0.5 * (T_s / 2) * 3/4 * S_s

Q = T_s * S_s * 1e-3
Q = AUC * 1e-3
delta_E = sample * 8.31 * (T_s / 2 - T_s) * 1e-3

if __name__=="__main__":
	print(Q)
	print(delta_E)
	print(Q - delta_E)
