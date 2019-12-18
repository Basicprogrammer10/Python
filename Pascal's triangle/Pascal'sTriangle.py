a = int(input("Number of rows: "))
b = [0, 1, 0]
c =[]
for i in range(a):
    c.append(0)
    for j in range(len(b)-1):
        c.append(b[i]+b[i+1])
    c.append(0)
    print(c)
    b = c
    c = []