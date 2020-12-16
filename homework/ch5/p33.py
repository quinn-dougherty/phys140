elevator_load = 2400 # kg
downward_v0 = 11 # m/s
distance = 24 # m

a = - downward_v0 ** 2 / 2 / (- distance)
T = elevator_load * (9.80665 + a)

if __name__=="__main__":
    print(T)

