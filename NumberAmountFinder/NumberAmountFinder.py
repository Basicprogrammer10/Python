from statistics import median
num = [1, 1, 5, 3, 3, 3]
final = []
low = 0
high = 0
for i in range(len(num)):
    if num[i] > high:
        high = num[i]
low = high
for i in range(len(num)):
    if num[i] < low:
        low = num[i]
num.sort()
print(num)
# prints the Min of the dataset to the Command Line
print("Min:    " + str(low))
# prints the Max of the dataset to the Command Line
print("Max:    " + str(high))
# print("Q1:     " + str(int())) #prints Q1 to the Command Line
# prints the median to the Command Line
print("Median: " + str(int(median(num))))
# print("Q3:     " + str(int())) #prints Q3 to the command Line
