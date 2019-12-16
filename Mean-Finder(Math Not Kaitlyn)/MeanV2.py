a = []
f = 0
t = 0
n = input("How many numbers? ")
for i in range(int(n)):
    a.append(input("Number: "))
for i in range(len(a)):
    t = int(a[i]) + int(t)
f = t / len(a)
print(f)