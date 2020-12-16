x = 14 # cm

force = 360 # N

k = (force / x) * 1e2

xj = 5 # cm
xj *= 1e-2

xs = [d * 1e-2 for d in [3, -3, -5, -9]]

if __name__=="__main__":
    print([k * (xj ** 2 - xi ** 2) / 2 for xi in xs])

