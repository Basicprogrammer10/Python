a = [34, 25, 24, 35, 40, 32, 41, 27, 37, 32, 21, 30]
f = 0
t = 0
for i in range(len(a)):
    t = int(a[i]) + int(t)
f = t / len(a)
print(f)