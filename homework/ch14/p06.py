
tires = 28.6 # psi
blood_pressure_upper = 125
blood_pressure_lower = 92.3

# report both numbers in kPa

if __name__=="__main__":
	print(tires * 1.01e5 / 14.7)
	print(blood_pressure_upper * 1.01e5 / 760)
	print(blood_pressure_lower * 1.01e5 / 760)
