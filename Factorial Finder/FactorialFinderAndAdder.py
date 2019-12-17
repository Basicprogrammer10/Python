a = int(input("Number: "))
b = a
c = a
e = 0
while b > 1:
    a = a * b
    b = b - 1
print(c, "Factorial is", a)
d = list(str(a))
for i in range(len(d)):
    e = e + int(d[i])
print("The sum of the digets in", a, "is", e)