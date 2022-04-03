'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit C, Problem C
'''
# Script 2: Bit Operators
a = 9
b = 14
print("binary of a =", bin(a))
print("binary of b =", bin(b))
print("binary of a & b =", bin(a&b))
print("binary of a | b =", bin(a|b))

'''
Examine the results. Can you see how they were arrived at?

I think the results for a&b is the least value for each of the two binary numbers. 
Basically, I think it compares each column of numbers in the binary value.
So it would be 0 and 0 first, and the least value is 0, then b and b and the least value is b
then 1 and 1 and the least value is 1 then 0 and 1 and the least value is 0. So on and so forth 
to get the binary value of 0b1000
0 b 1 0 0 1
| | | | | |
0 b 1 1 1 0
| | | | | |
0 b 1 0 0 0

for a | b, its the same thing expect it is the greatest value per column.
0 b 1 0 0 1
| | | | | |
0 b 1 1 1 0
| | | | | |
0 b 1 1 1 1
'''

'''
Execution results:
binary of a = 0b1001
binary of b = 0b1110
binary of a & b = 0b1000
binary of a | b = 0b1111
'''