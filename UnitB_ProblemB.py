'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit B, Problem B
'''
# First Script - Working with Strings

# 1) String Type Tests
inputString = input("Enter a string: ")
print(inputString.isupper())
print(inputString.isdigit())
print(inputString.isalpha())

# 2) Escape Characters within a string
text = "Type, type, type away. \nCompile. Run. Hip hip hooray! \nNo error today!"
print(text)

# 3) Slicing a string
quote = "And now for something completely different"
print(quote[0:7])
print(quote[-4:])
print(quote[14:16])
print(quote[::2])
print(quote[::-1])

# 4) Using string operators + and *
pattern1 = ".~*'"
pattern2 = pattern1 + pattern1[::-1]
print(pattern2*5)
                    


# Second Script:

# Printing a well formatted invoice
small = 10.20
medium = 8.52
large = 7.98
print()
smallQty = int(input("Boxes of small beads: "))
mediumQty = int(input("Boxes of medium beads: "))
largeQty = int(input("Boxes of large beads: "))
total = "{:.2f}".format(smallQty*small + mediumQty*medium + largeQty*large)
smallCost = "{:.2f}".format(smallQty*small)
mediumCost = "{:.2f}".format(mediumQty*medium)
largeCost = "{:.2f}".format(largeQty*large)

print()
print("SIZE{:>9}{:>16}{:>12}".format("QTY", "COST PER BOX", "TOTALS"))
print("{:<11}{:>2}{:>16}{:>12}".format("Small", smallQty, "{:.2f}".format(small), smallCost))
print("{:<11}{:>2}{:>16}{:>12}".format("Medium", mediumQty, medium, mediumCost))
print("{:<11}{:>2}{:>16}{:>12}".format("Large", largeQty, large, largeCost))
print("TOTAL{:>36}".format(total))

'''
Execution results:
Enter a string: ABC123
True
False
False
Type, type, type away. 
Compile. Run. Hip hip hooray! 
No error today!
And now
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.

Boxes of small beads: 10
Boxes of medium beads: 9
Boxes of large beads: 8

SIZE      QTY    COST PER BOX      TOTALS
Small      10           10.20      102.00
Medium      9            8.52       76.68
Large       8            7.98       63.84
TOTAL                              242.52
----------------- or ---------------------

Boxes of small beads: 5
Boxes of medium beads: 10
Boxes of large beads: 15

SIZE      QTY    COST PER BOX      TOTALS
Small       5           10.20       51.00
Medium     10            8.52       85.20
Large      15            7.98      119.70
TOTAL                              255.90
'''