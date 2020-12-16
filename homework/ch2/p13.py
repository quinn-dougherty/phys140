v1 = 73 # km / h
v2 = 92 # km / h

there = v1 / 2 + v2 / 2
back = 1 / (1 / 2 / v1 + 1/ 2 / v2)

if __name__=="__main__":
    print(there)
    print(back)
    print(there / 2 + back / 2)
