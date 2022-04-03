'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit B, Exercise B
'''
name = input("Enter the name: ")
print(name.upper())
print(len(name))
print(name[3])
name2 = name.replace('o', 'x')
print(name2)
print(name)

quote = "Believe you can and you're halfway there."
print("Count = ", quote.count('a'))
firstA = quote.find('a', 0)
secondA = quote.find('a', (firstA + 1))
thirdA = quote.find('a', (secondA + 1))
fourthA = quote.find('a', (thirdA + 1))
print('a found at ', firstA)
print('a found at ', secondA)
print('a found at ', thirdA)
print('a found at ', fourthA)

'''
Execution results:
nter the name: George Washington
GEORGE WASHINGTON
17
r
Gexrge Washingtxn
George Washington
Count =  4
a found at  13
a found at  16
a found at  28
a found at  32
'''

