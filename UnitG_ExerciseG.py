'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit G, Exercise G
'''

#Part One - Working with Files
fout = open('ZenOfPython.txt', 'wt')
print("Beautiful is better than ugly.", file = fout)
print("Explicit is better than implicit.", file = fout)
fout.close()
fout = open('ZenOfPython.txt', 'at')
print("Readability counts.", file = fout)
print("If the implementation is hard to explain, it's a bad idea.", file = fout)
fout.close()
fin = open('ZenOfPython.txt', 'rt')
lines = fin.readlines()
for line in lines:
    print(line, end='')
fin.close()
print()


#Part Two - CSV Files
import csv
with open("Cities.csv", 'rt') as fin:
    cin = csv.DictReader(fin)
    cities = [row for row in cin]  
newLine = 0
for city in cities:
    for key, city in city.items():
        if newLine == 2:
            print(city, end = "\n")
            newLine = 0
        else:
            print(city, end = " ")
            newLine += 1
print()
userCity = input("Please enter a city: ")
userState = input("Please enter a state: ")
for city in cities:
    tuple_list = list(city.items())
    city_value = tuple_list[0]
    state_value = tuple_list[1]
    population  = tuple_list[2]
    if city_value[1] == userCity:
        if state_value[1] == userState:
            print("{} {} has a population of {}".format(city_value[1], state_value[1], population[1]))

'''
Execution results:
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064

Please enter a city: Dublin
Please enter a state: California
Dublin California has a population of 46036

'''
    