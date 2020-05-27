import json
def one():
    with open('Food.json') as f:
        data = json.load(f)
    for i in range(90):
        for j in range(int(data[i]['Quantity'])):
            testfor = data[i]['Food Group']
            if testfor == 'Dessert':
                my_file = open("food/Dessert.nose","a+")
                my_file.write(data[i]['Name']+"\n")
            elif testfor == 'Protein':
                my_file = open("food/Protein.nose","a+")
                my_file.write(data[i]['Name']+"\n")
            elif testfor == 'Breakfast':
                my_file = open("food/Breakfast.nose","a+")
                my_file.write(data[i]['Name']+"\n")
            elif testfor == 'Veggie':
                my_file = open("food/Veggie.nose","a+")
                my_file.write(data[i]['Name']+"\n")
            elif testfor == 'Grain':
                my_file = open("food/Grain.nose","a+")
                my_file.write(data[i]['Name']+"\n")
            else:
                my_file = open("food/HELP.nose","a+")
                my_file.write(data[i]['Name']+"\n")

def two():
    with open('food.nose') as f:
        print(f.read())

one()