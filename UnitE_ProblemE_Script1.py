'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit E, Problem E
'''
#First Script – Decision Making

name = input("Please enter the plant name: ")
plantType = input("Please enter the plant type: ")
height = int(input("Please enter the plant height: "))
if plantType == "Vegetable":
    print("A {} can be planted in the Vegetable Garden.".format(name))
elif plantType == "Flower":
    if height <= 6:
        if height <= 3:
            print("A {} can be planted in the Low Garden or the High Garden.".format(name))
        else:
            print("A {} can be planted in the High Garden.".format(name))
    elif height > 6:
        print("A {} can not be planted in any of the gardens.".format(name))
else: 
    print("A {} can not be planted in any of the gardens.".format(name))

'''
Execution results:
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden or the High Garden.
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai can not be planted in any of the gardens.
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
Carrots can be planted in the Vegetable Garden.
Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can be planted in the Vegetable Garden.
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the High Garden.
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower can not be planted in any of the gardens.
'''