'''
Sanjana Gadaginmath
CIS 41A   Fall 2022
Unit A, Problem A 
'''
import math
#Basic numeric operations
a = 3 ** 2.5
b = 2
b += 3
c = 12
c /= 4
d = 5 % 3
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

#Built-in functions abs, round, and min
print(abs(5-7))
print(round(3.14159, 4))
print(round(186282, -2))
print(min(6, -9, -3, 0))

#Functions from the math module
num = float(input("Give me a number: "))
sqrt = round(math.sqrt(num), 2)
log = round(math.log10(num), 2)
print("Square root:", sqrt)
print("Base-10 logarithm:", log)

'''
Execution results:
a = 15.588457268119896
b = 5
c = 3.0
d = 2
2
3.1416
186300
-9
Give me a number: 7.6
Square root: 2.76
Base-10 logarithm: 0.88
'''
