a = [70, 70, 70, 70, 75, 75, 75, 75, 75, 75, 80, 80, 80, 80, 80, 80, 85, 85, 85, 85, 90, 90, 90, 95, 95, 100]
f = 0
t = 0
for i in range(len(a)):
    t = int(a[i]) + int(t)
f = t / len(a)
print(f)