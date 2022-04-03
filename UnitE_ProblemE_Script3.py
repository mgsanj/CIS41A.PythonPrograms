'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit E, Problem E
'''
#Third Script – has two parts

#Part One - Looping with String Methods
quote = "Believe you can and you're halfway there."
count = quote.count('a')
strIndex = 0
for i in range(count):
    index = quote.find('a', strIndex)
    print("a found at index {}".format(index))
    strIndex = index + 1

#Part Two – Nested Loops
rows = int(input("Please enter the number of rows for the multiplication table: "))
triangleStr = "{:>4}"
list = []
for i in range(1, rows+1):
    list = []
    string = "{:<2}{:>3}"
    if i == 1:
        string = "{:<2}".format(1) 
    else: 
        for y in range(1, i+1):
            list.append(y*i)
    for x in range(i-2):
        string += triangleStr           
    print(string.format(*list))

'''
Execution results:
a found at index 13
a found at index 16
a found at index 28
a found at index 32
1 
2   4
3   6   9
4   8  12  16
5  10  15  20  25
6  12  18  24  30  36
7  14  21  28  35  42  49
8  16  24  32  40  48  56  64
9  18  27  36  45  54  63  72  81
10 20  30  40  50  60  70  80  90 100
11 22  33  44  55  66  77  88  99 110 121
12 24  36  48  60  72  84  96 108 120 132 144
'''