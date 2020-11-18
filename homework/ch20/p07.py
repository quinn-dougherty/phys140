from math import log

m_copper = 35.4 # g
t_copper = 428 # kelvin

m_lead = 108 # g
t_lead = 122 # kelvin

equilibrium_temp = (m_copper * 386 * t_copper + m_lead * 128 * t_lead) / (m_copper * 386 + m_lead * 128)

delta_S = m_copper * 386 * log(equilibrium_temp / t_copper) + m_lead * 128 * log(equilibrium_temp / t_lead)
if __name__=="__main__":
	print(equilibrium_temp)
	print(0)
	print(delta_S)
