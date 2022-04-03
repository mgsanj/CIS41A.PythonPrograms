'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit J take-home assignment
'''
import re

#Problem J part 1
data = input("Input text: ")
a = re.search('a', data)
if a:
    print("Found")
else:
    print("Not Found")

#Problem J part 2
data = input("Input text: ")
b = re.findall('b', data)
print(b)

#Problem J part 3
data = input("Input text: ")
space = data.split()
print(space)

#Problem J part 4
data = input("Input text: ")
data = re.sub(r'(th)', 'lore', data)
print(data)

'''
Execution results:
Input text: Dwight D. Eisenhower
Not Found
Input text: Dobby Rebeus Longbottom Gabrielle Albus
['b', 'b', 'b', 'b', 'b', 'b']
Input text: Bill Charlie Percy Fred George Ron Ginny
['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny']
Input text: thlei, th, and folk tales
lorelei, lore, and folk tales
'''
