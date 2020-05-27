import csv

with open('Food.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(f'\t{row[0]},{row[1]},{row[2]},{row[6]},{row[7]}')
        num = row[2]
        #num = num[:-3]
        print(float(num))