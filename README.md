# CIS41A: Python Programs
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
_________________________
## Unit C
### Exercise C
**List Script**
- Create a list called list1 that has elements 2, 4.1, 'hello'.
- Copy list1 to list2 so that list2 is an alias of list1 (shallow copy).
- Copy list1 to list3 so that list3 is a new list (true deep copy).
- Using ==, compare list1 to list2, list1 to list3, and list2 to list3.
- Using is, compare list1 to list2, list1 to list3, and list2 to list3.
- Print the ids of list 1, list2, and list3.
- Append a new element with value 8 to list1.
- After the first element of list2, insert an element 'goodbye'.
- Remove the first element from list3.
- Print each of the three lists. Do the results match what you expected?

### Problem C
#### First Script – Working with Lists
**All print output should include descriptions as shown in the example output below.**
- Create an empty list called list1
- Populate list1 with the values 1,3,5
- Swap the second and third elements of list1.
- Iterate over list1 and print its items.
- Create list2, initialized with the values 1,2,3,4
- Create list3 by combining list1 and list2 (use the + operator).
- Print list3.
- Use sequence operator in to test list3 to see if it contains a 3, print True/False result (do with one line of code).
- Count the number of 3s in list3, print the result.
- Determine the index of the first 3 in list3, print the result.
- Pop this first 3 and assign it to a variable called first3, print first3.
- Create list4, populate it with list3's sorted values, using the sorted built-in function.
- Print list3.
- Print list4.
- Slice list3 to obtain a list of the values 1,2,3 from the middle of list3, print the result.
- Determine the length of list3, print the result.
- Determine the max value of list3, print the result.
- Sort list3 (use the list sort method), print list3.
- Create list5, a list of lists, using list1 and list2 as elements of list5.
- Print list5.
- Print the value 4 contained within list5.

Example output:
<pre>
d) Items in list1:
1
5
3
g) list3 is: [1, 5, 3, 1, 2, 3, 4]
h) list3 contains a 3: True
i) list3 contains 2 3s
j) The index of the first 3 contained in list3 is 2
k) first3 = 3
m) list3 is now: [1, 5, 1, 2, 3, 4]
n) list4 is: [1, 1, 2, 3, 4, 5]
o) Slice of list3 is: [1, 2, 3]
p) Length of list3 is 6
q) The max value in list3 is 5
r) Sorted list3 is: [1, 1, 2, 3, 4, 5]
t) list5 is: [[1, 5, 3], [1, 2, 3, 4]]
u) Value 4 from list5: 4
</pre>

#### Second Script – Bit Operators
- Assign the values 9 and 14 to variables a and b respectively.
- Print the binary values of a and b (use the bin built-in function).
- Calculate the value of a and b, print the result in binary.
- Calculate the value of a or b, print the result in binary.
- Examine the results. Can you see how they were arrived at?

Example output:
<pre>
a) binary of a =  0b1001
b) binary of b =  0b1110
c) binary of a & b =  0b1000
d) binary of a | b =  0b1111
</pre>
_______________________
## Unit D
### Exercise D
**1) Dictionary Basics:**
- Create a dictionary of fruit and desserts made from the fruit. The fruit should be the key and the dessert should be the value. Use these key value pairs:

apple:sauce\
peach:cobbler\
carrot:cake\
strawberry:sorbet\
banana:cream pie
- Add the mango fruit to the dictionary. Its dessert is sticky rice.
- Change the strawberry dessert to shortcake.
- Carrot is not a fruit, so remove carrot from the dictionary.
- Print the apple dessert.
- See if a banana dessert exists.
- See if a pear dessert exists.
- Print the keys in the dessert dictionary.
- Print the values in the dessert dictionary.
- Print the key-value pairs in the dessert dictionary.
**2) Combining dictionaries:**
- Create a dictionary named capitols1 and populate it with these key value pairs:

Alabama:Montgomery\
Alaska:Juneau\
Arizona:Phoenix\
Arkansas:Little Rock\
California:Sacramento
- Create a dictionary named capitols2 and populate it with these key value pairs:

California:Sac.\
Colorado:Denver\
Connecticut:Hartford
- Be sure that the California capitol is Sac. and not Sacramento.
- Using the dictionary update() method, update capitols1 with capitols2.
- Print the sorted capitols (values). Note the updated value of California's capitol.
**3) Sets Basics:**
- Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
- Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
- Add John to class1.
- Print a sorted list of students who are in both classes.
- Print a sorted list of all students.
- Test to see if Sasha is in class1.

### Problem D
**Part One - List Comprehension**

Using a list comprehension, generate a list of the first 10 Triangle numbers. If you've never learned about Triangle numbers, this site has everything you need to know. As detailed on the website, the formula to calculate the nth term in the sequence is n*(n+1)/2.

**Part Two - Sets**
- Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
- Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
- Create a set named class3 and populate it with the students Migel, Zhang, Hiroto, Anita, Jia.
- Using set operators or set methods, generate a set of students who are in all three classes. Print a sorted list of these students.
- Using set operators or set methods, generate a set of all students. Print a sorted list of these students.
- Using set operators or set methods, generate a set of students in class1 but not class2 or class3. Print a sorted list of these students.
- Using a set comprehension, generate a set of all students who are in class2 but not in class1. Print a sorted list of these students.

**Part Three – Tuple Basics**

For Parts Three, Four and Five, you will be working with data about the movie Casablanca.

- Create a tuple that contains the elements Casablanca, 1942, romantic drama.
- Unpack the tuple into variables title, year, genre.
- Print the genre.

**Part Four – Named Tuple**

- Define a named tuple called Movie that contains the fields title, year, genre.
- Create a Movie tuple that contains the elements Casablanca, 1942, romantic drama.
- Print the title.

**Part Five – Named Tuple Containing a List**
- Define a named tuple called Moviestars that contains the fields title, year, genre, stars.
- Create a Moviestars tuple called favoritemovie that contains the elements Casablanca, 1942, romantic drama, and a list containing elements Humphrey Bogart, Ingrid Bergman.
- Append Claude Rains to the stars list. Hint: Use the syntax favoritemovie.stars.append
- Print star Ingrid Bergman.
- Print favoritemovie.
- Note that, even though a tuple is immutable, we are able to change a list that is contained by a tuple.
__________________________
## Unit E
### Exercise E
**Part One - If Logic**

- Create a list called scifi that contains the elements Alien, Solaris, Inception, Moon.
 -Create a list called comedy that contains the elements Borat, Idiocracy, Superbad, Bridesmaids.
- Ask the user for the name of a movie.
- Using if/elif/else, determine and print the genre of the movie.
- Test three times: first with Moon, then Superbad, then Dunkirk.
**Part Two - Using Range**

- Use a for loop to print the even integers in descending order from 10 to 0 inclusive.

**Part Three - Looping Through Dictionary Items**
- Create a dictionary named movies and populate it with these key value pairs:

The Wizard of Oz:1939\
The Godfather:1972\
Lawrence of Arabia:1962\
Raging Bull:1980
- Loop through the dictionary items and print the year in which each movie was made. Output should be alpha sorted by movie title.

### Problem E





