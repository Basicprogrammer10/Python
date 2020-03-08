num = [1, 1, 5, 3, 3, 3]
final = []
low = 0
high = 0

for i in range(len(num)):
    if num[i]>high:
        high = num[i]

low = high
for i in range(len(num)):
    if num[i]<low:
        low = num[i]

for i in range(1, len(num)):
    if i == num[i]:
        final.append(num[i])
        

print(final)