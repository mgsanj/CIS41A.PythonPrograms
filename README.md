# PythonPrograms
This contains all of the programs I've written for the Python Programming class I took at De Anza College. These are all my original work and I've also included descriptions of the problems below. 
___________________________________
## Unit A
### Exercise A
In this exercise, you will write some simple code.
Look at lab instructions and use the Wing Interactive Develoment Environment.
1) Create rectangle height and width variables and initialize them with the values 2.9 and 7.1 respectively.
2) Calculate the area of the rectangle and save it in an area variable.
3) Print the height, width, and area of the rectangle as shown below.
Note: Use the sample code shown below to print - we will learn more about printing in the next Unit.
print("Height:", height)
4) Use floor division to modify the values in the height and width variables by dividing them by 2.
Note: floor division is the prefered name in Python. Elsewhere it is commonly called integer division.
5) Print the data for this smaller rectangle.
Did you get the answers you expected?

### Problem A
**Basic numeric operations**
1) Calculate and print the final value of each variable.
- a equals 3 to the power of 2.5
- b equals 2
- b equals b + 3 (use +=)
- c equals 12
- c = c divided by 4 (use /=)
- d equals the remainder of 5 divided by 3
**Built-in functions abs, round, and min**
2) Use abs, round, and min to calculate some values. These are all Python built in functions (see: BIF).
- Print the absolute difference between 5 and 7 (the answer should always be a positive number).
- Print 3.14159 rounded to 4 decimal places.
- Print 186282 rounded to the nearest hundred.
- Print the minimum of 6, -9, -3, 0
**Functions from the math module**
3) Use some functions from Pythons math module to perform some calculations. (see: Mathematical functions).
- Ask the user for a number (test with the value 7.6).
- Print the square root of the number, rounded to two decimal places (include an appropriate description).
- Print the base-10 log of the number, rounded to two decimal places (include an appropriate description)
_________________________
## Unit B
### Exercise B
1) String methods
- Ask the user for a name (test with George Washington).
- Print the name in all uppercase letters.
- Print the length of the name.
- Print the 4th character of the name (r).
- Create a variable called name2. Assign to name2 the name with all "o" characters replaced with "x"s.
- Print name2.
- Print the original name.
2) Counting and Finding
- Assign the text "Believe you can and you're halfway there." to a variable called quote (this is a quote from Theodore Roosevelt).
- Count how many "a" characters there are, print the result.
- Print the index of all the "a" characters.
- Hint: Except for the first find, set the start location for the next find as the previous location found index + 1. The second argument in the find method is the index where the find starts looking.

### Problem B
#### First Script - Working with Strings
This script contains four parts.

**1) String Type Tests**
- Ask the user for a string (test with "ABC123").
- Use method isupper to test the string, print the result.
- Use method isdigit to test the string, print the result.
- Use method isalpha to test the string, print the result.

**2) Escape Characters within a string**
Use newline escape characters within a line of haiku

- Assign the text "Type, type, type away. Compile. Run. Hip hip hooray! No error today!" to a single variable (be sure to add newline escape characters). This should be done in a single line of code.
- Print, so that the output appears as follows:
<pre>
Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!
</pre>
Haiku by Samantha W.

**3) Slicing a string**
- Assign the text "And now for something completely different" to a variable called quote.
- Slice quote to obtain the text "And no" from the beginning of the quote, print the results.
- Slice quote to obtain the text "rent" from the end of the quote, print the results.
- Slice quote to obtain the text "me" from the middle of the quote, print the results.
- Slice quote to obtain the text "Adnwf..." by extracting every other letter, print the results.
- Slice quote to obtain the text "tnere..." by reversing the quote, print the results.
**4) Using string operators + and ***
- Assign the text ".\~*'" to a variable called pattern1.
- Create a variable called pattern2, assign to it pattern1 combined with pattern1 reversed. pattern2 should now contain the string ".\~*''*\~."
Print pattern2 repeated five times. The output should appear as follows:
.\~*''*\~..\~*''*\~..\~*''*\~..\~*''*\~..\~*''*\~.
      
#### Second Script:
**Printing a well formatted invoice**

Use three named "constants" for the following prices:
Small beads have a price of 10.20 dollars per box.
Medium beads have a price of 8.52 dollars per box.
Large beads have a price of 7.98 dollars per box.

Ask the user how many boxes of small beads, how many boxes of medium beads, and how many large beads they need (use the int Built-in Function to convert these values to int).

Print the invoice in the following format:
<pre>
SIZE      QTY    COST PER BOX      TOTALS
Small       n            x.xx       xx.xx
Medium      n            x.xx       xx.xx
Large       n            x.xx       xx.xx
TOTAL                              xxx.xx
</pre>

Replace the n and x placeholders with actual numeric data values. Right align all numeric values. All dollar amounts should have two decimal places and should align on the decimal point.

Test your script twice, first with user input of 10 boxes of small beads, 9 boxes of medium beads, and 8 boxes of large beads, and then a second time with user input of 5 boxes of small beads, 10 boxes of medium beads, and 15 boxes of large beads.



