v1 = 967 # km / h
v2 = v1 / 2 # km / h
d1 = 0.41 # kg / m / m / m at 9.5 km up
d2 = 0.68 # kg / m / m / m at 4.8 km up

if __name__=="__main__":
    print(d1 * v1**2 / d2 / v2**2)

