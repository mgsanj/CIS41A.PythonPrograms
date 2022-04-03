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
**First Script – Decision Making**

Write a script that can determine where different plants can be planted.

Each plant has a name, a type (Flower, Vegetable, Tree, etc.), and a maximum height.
There are three gardens as follows:

- The Vegetable Garden can have only Vegetables, and there is no maximum height.
- The Low Garden can have only Flowers, and there is a maximum height of 3.
- The High Garden can have only Flowers, and there is a maximum height of 6.

Print ONE line that identifies the one or more gardens that a given plant can be planted in. If a plant does not match the criteria for any of the gardens, then say so.

Test the script six times with the following test data:

1. Name: Lily, Type: Flower, Height 3
2. Name: Bonsai, Type: Tree, Height 2
3. Name: Carrots, Type: Vegetable, Height 1
4. Name: Corn, Type: Vegetable, Height 8
4. Name: Rose, Type: Flower, Height 5
5. Name: Sunflower, Type: Flower, Height 8

Example output:
<pre>
Please enter the plant name: Lily 
Please enter the plant type: Flower 
Please enter the plant height: 3 
A Lily can be planted in the Low Garden or the High Garden.
and so on...
</pre>

**Second Script – Guessing Game**

Write a script that plays a simple guessing game.
The script will generate a secret number from 1 to 100, inclusive, and the user will have to guess the number.
After each guess, the script will tell the user if they are high, low, or correct.
If they are correct, the script will congratulate the user, tell them how many guesses they took, and then end the script.

Hint: most of the game code will be in a loop that repeats until the correct number is guessed.

To generate the secret number, you will need to use the randint function from Python's Random module

Example output:
<pre>
Welcome to the guessing game.
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too low.
What is your guess? 75
Guess is too low.
What is your guess? 87
Guess is too high.
What is your guess? 81
Guess is too low.
What is your guess? 84
Guess is too low.
What is your guess? 85
Congratulations!
You guessed the secret number in 6 guesses!
</pre>

**Third Script – has two parts**

_Part One – Looping with String Methods_

Update the Unit B Counting and Finding In-Class exercise to use a loop.

- Assign the text "Believe you can and you're halfway there." to a variable called quote (this is a quote from Theodore Roosevelt).
- Loop through the quote to find and print the index of all the "a" characters.

Hint: One way is to loop a fixed number of times, based on the count of the "a" characters.
Another way is to loop until you have searched the entire string.
It can be convenient to initialize the location variable before starting the loop.

_Part Two – Nested Loops_

Write a script using nested for loops to generate a triangular multiplication table as illustrated below.
Ask the user how many rows they would like in their table.
Generate formatted output where each number is right justified within a fixed field size, so that the numbers in each column are aligned.

Test with a user value of 12 rows.

Example output:
<pre>
a found at index 13
a found at index 16
a found at index 28
a found at index 32

Please enter the number of rows for the multiplication table: 12
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   and so on...
</pre>
___________________
## Unit F
### Exercise F
**Part One – Using a main function, Docstrings**

Write a function called hello. The function has no arguments and no return value. It simply prints the text "Hello World". Include a docstring that describes the function.

Write a main function, as described by the Python main function reading.

Call main, as described by the Python main function reading.

From main, call hello and then print hello’s docstring.

**Part Two – Error Handling**

Write a function called printListElement. The function has two arguments and no return value. The first argument is a list, and the second argument is a list index. The function will print an element from the list as determined by the list index. If the list index is invalid, print an error message.

We could accomplish this with a logic test, but instead, we will manage this with error handling.

Write a try block that attempts to print the list element. Catch any errors with an except block, print an error message.

From main, create a myList list with elements 0, 1, 2 by using the list and range commands.

Then, call printListElement with your list and a list index value of 3.

**Part Three – How Python function arguments are treated**

There can be some confusion as to how Python functions treat their arguments - is it by reference or by value? Explore this for yourself.

From main, create a myInt variable and give it the value 3. Also create a myList list with elements 0, 1, 2.

Print the IDs of myInt and myList. Also print the ID of the last element of myList.

Now create a function called byVal which has one argument. In the function, add 7 to the argument. Print the ID of the argument before and after the change.

Create a second function called byRef which has one argument. In the function, add 7 to the last element in the list. Print the ID of the argument and the ID of the last element of the argument before and after the change.

Now call byVal with myInt and then call byRef with myList. Next, again print the IDs of MyInt, myList, and the last element of myList. Finally, print myInt and MyList from main. Can you explain the results?

### Problem F
**Part One – Keyword Arguments and Default Values**

Write an invoice function.\
The function will generate a simple invoice and will have two required arguments and two keyword arguments.\
The two required arguments are unitPrice and quantity.\
The first keyword argument is shipping, and it has a default value of 10.\
The second keyword argument is handling, and it has a default value of 5.

Test it twice from main:\
First test: unitPrice 20, quantity 4, and shipping 8 (handling is not specified).\
Second test: unitPrice 15, quantity 3, and handling 15 (shipping is not specified).\
Don't worry about making the formatting pretty.

**Part Two – args (Variable-Length Arguments)**

Write a printGroupMembers function.\
The function prints a list of students who are working together on a group project, as well as the group name.\
The function has one required argument, the group name, and one variable-length argument that contains the student names.

Test it twice from main:\
First test: Call as follows:\
printGroupMembers("Group A", "Li", "Audry",\ "Jia")\
Second test: Create a list as follows:
groupB = \["Group B", "Sasha", "Migel", "Tanya", "Hiroto"\]
and then call the function using this list.\

**Part Three – kwargs (Variable-Length Keyword Arguments)**

For this problem, imagine that there is a complex piece of equipment, perhaps a car or a spacecraft, and that all of its various subsystems periodically send out status messages to be read and evaluated by an overseer system. Each message contains just a small amount of data - perhaps only one or two keywords out of the hundreds of things that overseer system must monitor. However, we will restrict ourselves to only three things: temperature, CO2level, and miscError.

Write an overseerSystem function that has a kwargs argument.

Within the function, see if the keyword temperature exists in kwargs. If it does, and the temperature is greater than 500, print a warning with the temperature.\
Also see if the keyword CO2level exists in kwargs. If it does, and the CO2level is greater than .15, print a warning with the CO2level.\
Lastly, see if the keyword miscError exists in kwargs. If it does, print a warning with the miscError number.

Test from main by creating five messages and calling the overseerSystem function with each message.

<pre>
Message1 is temperature:550
Message2 is temperature:475
Message3 is temperature:450, miscError:404
Message4 is CO2level:.17
Message5 is CO2level:.2, miscError:418
</pre>

**Part Four – Working with a list of functions** 
We will be building a very basic baseball simulation, one that simulates one half inning of play.\
Note: you don't have to know the rules of baseball in order to complete this problem - everything you need to know will be explained here.

In our simulation, there will be five possible outcomes - out, single, double, triple, home run, each with it's own probability of occuring.

Each of these outcomes will be represented by a short function that you will need to write. Each function does nothing but print the outcome and return a numeric value. Function out returns 0, single returns 1, double rteturns 2, triple returns 3, and homerun returns 4. For example, here's the out function:
<pre>
def out():
    print("Out")
    return 0
</pre>
Our simulation will generate outcomes within a loop until three outs have occured, at which time the simulation is complete.

Outcomes will be randomly generated one at a time with the help of Pythons random.choices() method. The sequence parameter used by the choices method is a list of the outcome functions. Parameter weights is a list of probabilities, as given below. The k parameter value will be one, as we only want one outcome at a time. Here's some starter code:
<pre>
import random

outcomes = list of functions - ***you need to write this - list should be in this order: out, single, double, triple, homerun***
probabilities = [70, 18, 5, 1, 6]  #chance of an out is 70%, single is 18% and so on.

#Start loop here - ***you need to write this***
    outcome = random.choices(outcomes, weights = probabilities, k = 1)
    ...
</pre>

Note that outcome is a list containing a single element.
______________________
## Unit G
### Exercise G
**Part One – Working with Files**

Create a new file called ZenOfPython.txt and write the first two lines of the Zen of Python to the file. Close the file.

Reopen the file and append the 7th and the 17th lines. Then close the file.

Open the file again and read and print the entire contents of the file (there shouldn't be any blank lines between the text).
Then close the file.

Sample Execution Results:
<pre>
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.
</pre>

**Part Two – CSV Files**

For this exercise, you will need to download the file Cities.csv from Canvas and save it into the same directory as your Python script. To do this, login to Canvas, select CIS 41A, select Files, select Cities.csv, select Download, and save into the same directory with your unit G in-class Python script.

The file contains a list of cities, their state, and their population. The file starts with a header row of field names, which are City, State, Population.

You will need to save this data (but not the header data) into a dictionary. The dictionary key will be a tuple consisting of the name of the city and the name of the state. The dictionary value will be the population.
The reason for this structure is that there are a number of duplicate city names within the file, but no duplicate city/state pairs.

Hint: When you create your reader object, you should use the DictReader from the csv module. Because the file contains a header row of field names, we don’t have to explicitly define them when creating the reader object. However, you should use these field names instead of numerical indexes when working with the row data.

After reading the csv file, iterate through the dictionary and print the data.

Then, ask the user for a city and state, then print that city’s population, if it exists.
Test with Dublin, California.

Sample Execution Results:
<pre>
Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
and so on...

Please enter a city: Dublin
Please enter a state: California
Dublin California has a population of 46036
</pre>

### Problem G
**Part One – Reading a data file**

For this exercise, you will need to download the file States.txt from Canvas and save it into the same directory as your Python script.

The file has 50 lines of data, one for each state in the Unites States. Each line of data contains three pieces of data separated by a space: the two letter abbreviation of the state's name, the region that the state is in, and the 2016 population of the state.

You need to find and print the state with the highest population in the Midwest region.

Note: file States.txt is not a csv file - don't try to read it with a csv reader.

Example output:
<pre>
Highest population state in the Midwest is: IL 12802000
</pre>

**Part Two – A Dictionary of Lists**

Download the file USPresidents.txt from from Canvas and save it into the same directory as your Python script.

The file has 44 lines of data, one for each president in the history of the Unites States. Each line of data contains two pieces of data separated by a space: the two letter abbreviation of the name of the state where the president was born, and the name of the president (for your convenience, the president's name has been converted to a single string – George Washington has been converted to George_Washington).

Using the data from the file, you need to build a dictionary of states and the presidents born in those states. Each key will be a state abbreviation and each value will be a list of presidents. Use defaultdict to initialize the dictionary so that its default values are empty lists.

After building the dictionary, determine the state with the most presidents and how many presidents were born there. Print their names.

Example output:
<pre>
The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
And so on...
</pre>

**Part Three – Dictionary Keys and Sets**

Using a dictionary comprehension, build a new dictionary from the data in the Part Two dictionary. Each key will again be a state abbreviation, however, the value will be the count of presidents from that state.

Create a set of the ten most populous US states (CA, TX, FL, NY, IL, PA, OH, GA, NC, MI).
Note - take this a a given - you do not have to find these ten states on your own.

Then, using a set operator, create a new set that represents a set of populous US states that have had presidents born in them.

Print a count of this new set along with an alpha-sorted listing of these states and how many presidents have been born in them.

Example output:
<pre>
8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2 
And so on...
</pre>
__________________________________
## Unit H
### Exercise H
**Part 1 - A Basic Class - State Data**

Create a StateData class with the following methods: __init__, __str__, displayState.\
Note: __ is two underline characters (dunder).

The __init__ method should have the parameters self, name, abbreviation, region, and population and should store the name, abbreviation, region, and population as attributes.

The __str__ method has the parameter self and should return the state's name.

The displayState method has the parameter self and should print formatted state data as shown below.

Test the class by creating an instance of the class (instantiating) called s1 with the following data: "California", "CA", "West", 39250000. Print your state object (this will call the __str__ method). Then call displayState. This test code should be after your class code - don't worry about calling from main.

Sample Execution Results:
<pre>
California
California (CA) is in the West region and has population of 39250000
</pre>

**Part 2 - Different ways of working with Attributes**

Here we explore different ways to work with Python attributes. Note that, while one of the approaches we are using is set/get, this approach is generally deprecated in favor of the simpler dot notation.

Create a StateData2 class with the following methods: __init__, setRegion, getRegion.

The __init__ method should have the parameters self, name and should store the name as an attribute.

The setRegion should have the parameters self, region and should store the region as an attribute.

The getRegion should have the the parameter self and should return the the value of the region data variable.

Test the class by creating an instance of the class called s2 with the following data: "California". Then call setRegion with the argument "West". Then set the population attribute with the following line of code: s2.pop = 39250000

Then print four lines: s2.name, s2.getRegion(), s2.region, s2.pop

Again, this test code should be after your class code.

Sample Execution Results:
<pre>
California
West
West
39250000
</pre>

**Part 3 - Data Hiding**

Data hiding within Python is achieved with the use of special naming conventions: beginning an attribute name with either a single underscore (protected) or a double underscore (private).

Create a StateData2 class with the following method: __init__.

The __init__ method should have the parameter self. It should store the value "Public" in an attribute called public, the value " Protected" in an attribute called _protected (use a single underscore), and the value " Private" in an attribute called __private (use a double underscore).

Test the class by creating an instance of the class called test.

Try to print three lines: test.public, test._protected, test.__private

Sample Execution Results:
<pre>
Public
Protected
Traceback error
</pre>

### Problem H

**Part One - Operator Overloading**

We will be building a BritCoins class that allows you to work with British money as it was denominated up to 1971. While there were a variety of types of coins, we will only be concerned with pounds, shillings, and pennies. A shilling was worth 12 pennies, and a pound was worth 20 shillings. Therefore, a pound was worth 240 pennies.

The class will allow you to initialize a BritCoins object with any given amount of pounds, shillings and pennies, add and subtract BritCoins objects, and to print a string that represents the value of the coins used to initialize a BritCoins object.

Certain aspects of the BritCoins class will parallel the Length class example shown here: [magic methods](https://www.python-course.eu/python3_magic_methods.php)(scroll down to the Example class: Length section). However, there will be some significant differences.

The idea of the BritCoins class is that you will pass the class a dictionary of coinTypes (keys) and the quantities of each coinType (values). In other words, we will be using kwargs as we did in the third exercise of the Lab H Takehome. The class will then calculate how many pennies these coins represent and save this totalPennies value. The totalPennies value will later be used for addition and subtraction as well as for generating the coin value string.

Building the class:

Create a BritCoins class with the following methods: __init__, __add__ , __sub__ , __str__. There will also be a private class dictionary called \__coinValues as follows (this is similar to the \__metric variable in the Length example).

\__coinValues = {"pound":240, "shilling":12, "penny":1} #value of each type of coin in pennies

The __init__ method should have the parameters self, and \**kwargs. Start by initializing a self.totalPennies attribute to zero. Then iterate through the kwargs. For each coinType in kwargs, add the value in pennies of that type and quantity of coin to a self.totalPennies. Determine this value by multiplying the number of coins (get this from kwargs) by the coin value (get this from \__coinValues - do not hardcode the values!). As an example, if init receives 4 pound, 3 shilling and 2 penny, totalPennies should be 998 (4*240+3*12+2*1).

The __add__ method should have the parameters self and other. Calculate a local total by adding self.totalPennies to other.totalPennies. Then return this value. However, there are two crucial considerations here. The first is that when we add two BritCoins objects, the result of this addition should also be a BritCoins object. Therefore, what we want to return isn't the total, but is instead a new BritCoins object that has been initialized with the appropriate coinage. So, we need to create and return an instance of the class. We can do this within the class itself! The second consideration is that when we create this instance, we need to provide an appropriate argument for BritCoins. We can't just pass the total (of say, 998) - we need to pass a dictionary like {"penny":998}. Further, we need to use appropriate notation when making this BritCoins call (as you did when testing the overseerSystem function in the Lab H Takehome).

The __sub__ method should have the parameters self and other. It is similar to the add method except that you subtract other from self instead of adding it.

The __str__ method has the parameter self and should return a string that represents the value of the BritCoins object. The string should be formatted as shown below, showing pounds, shillings and pennies. From self.totalPennies, you will need to calculate how many of each coin type there are using floor division or some other technique. Note that this string representation won't necessarily be the coins used to initialize the BritCoins object - it will be the value of the BritCoins object. For example, if the BritCoins object was initialized with 25 shillings, the return should be 1 pounds 5 shillings 0 pennies.

For this script, the test code should be after your class code – don't worry about calling from main.

Test the BritCoins class with the following data:

c1 = 4 pound, 24 shilling, 3 penny\
c2 = 3 pound, 4 shilling, 5 penny\
c3 = c1 + c2\
c4 = c1 - c2

Then print c1, c2, c3 and c4.

**Part Two - Pickling**

Here, we will pickle (save/serialize) a Python object structure to a file and then unpickle (retrieve/de-serialize) it.

Pickle Britcoin c4, then unpickle and print it.

Sample Execution Results:
<pre>
5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies

1 pounds 19 shillings 10 pennies
</pre>
_______________________________
## Unit I
### Exercise I
**Part 1 of 1 - Basic Inheritance - Circle & Cylinder**

You will be creating a Circle base (parent) class and a Cylinder class that inherits from it (child).\
Both classes and the code to test the classes will be contained within a single script.

The Circle class has the following methods: __init__, getArea.\
Circle's __init__ method should have the parameters self and radius, and should store the radius as an attribute.\
The getArea method has the parameter self and should return the circle's area (use the pi constant from the math module when calculating the area).

The Cylinder class inherits from the Circle class and has the following methods: __init__, getVolume.\
Cylinder's __init__ method should have the parameters self, radius and height. From within Cylinder's __init__, call Circle's __init__ to store the radius. The height should be stored as an attribute of the Cylinder.\
The getVolume method has the parameter self and should use the getArea method and calculate and return the cylinder's volume. See: volume of a cylinder

Test by creating an instance of the Circle class with a radius of 4. Print the area of the circle, rounded to 2 places.\
Then, create an instance of the Cylinder class with a radius of 2 and a height of 5. Print the volume of the cylinder, rounded to 2 places.

### Problem I
**Part 1 of 1 - Inheritance with Multiple Children**

We will be building a suite of three classes to manage library patrons and the books that they check out (a library patron is someone who has a library account).\
All three classes and the code to test the classes will be contained within a single script.

The library has two types of patrons, adult and juvenile, and two types of books, adult and juvenile. Juvenile patrons can only check out juvenile books, while adult patrons can check out any type of book. Additionally, juvenile patrons have a limit of 2 books that they may have checked out at one time, while adult patrons have a limit of 4 books that they may have checked out at one time.

We will write three classes: a parent LibraryPatron class, and AdultPatron and JuvenilePatron child classes. Ideally, we would also have a Book class, but we will simplify things here by making a book be a list with two elements: the title, and the book type - adult or juvenile (see the testing code below).

**LibraryPatron class:**

The LibraryPatron class has the following four methods: __init__, checkOutBook, returnBook, and printCheckedOutBooks.

The __init__ method should have the parameters self and name, and should store the name as an attribute (name is the name of the patron). There should also be an additional attribute called booksCheckedOut which should be initialized as an empty list. This attribute will store a list of the book titles that the patron currently has checked out.

The checkOutBook method should have the parameters self, checkOutLimit and bookTitle. If the patron is at their checkout limit, print a "Sorry" message to the patron. Otherwise, append the bookTitle to the patron's booksCheckedOut list and print a "Checkout" message, as shown below.

The returnBook method should have the parameters self and book. Here, book is a book list object - you will need to extract the book title from the list. Remove the book title from the patron's list of checked out book titles and print a "returned" message.

The printCheckedOutBooks method should have the parameter self. Print a message along and print all the patron's checked out book titles, as shown below.

**AdultPatron class:**

The AdultPatron class inherits from the LibraryPatron class and has the following two methods: __init__, checkOutBook.

The __init__ method should have the parameters self and name. Call LibraryPatron's __init__ to store the name. There should also be an additional attribute called checkOutLimit which should be initialized with a value of 4.

The checkOutBook method should have the parameters self and book. Here again, book is a book list object. Call LibraryPatron's checkOutBook method, using the patron's checkOutLimit and the book title as arguments.

**JuvenilePatron class:**

The JuvenilePatron class inherits from the LibraryPatron class and has the following two methods: __init__, checkOutBook.

The __init__ method should have the parameters self and name. Call LibraryPatron's __init__ to store the name. There should also be an additional attribute called checkOutLimit which should be initialized with a value of 2.

The checkOutBook method should have the parameters self and book. Here again, book is a book list object. If the book is not a a juvenile book, print a "Sorry" message as shown below. Otherwise, call LibraryPatron's checkOutBook method, using the patron's checkOutLimit and the book title as arguments.

Test with the following code:
<pre>
    book1 = ["Alice in Wonderland", "Juvenile"]
    book2 = ["The Cat in the Hat", "Juvenile"]
    book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
    book4 = ["The Hobbit", "Juvenile"]
    book5 = ["The Da Vinci Code", "Adult"]
    book6 = ["The Girl with the Dragon Tattoo", "Adult"]
    
    patron1 = JuvenilePatron("Jimmy")
    patron2 = AdultPatron("Sophia")

    patron1.checkOutBook(book6)
    patron1.checkOutBook(book1)
    patron1.checkOutBook(book2)
    patron1.printCheckedOutBooks()
    patron1.checkOutBook(book3)
    patron1.returnBook(book1)
    patron1.checkOutBook(book3)
    patron1.printCheckedOutBooks()
    patron2.checkOutBook(book5)
    patron2.checkOutBook(book4)
    patron2.printCheckedOutBooks()
</pre>
__________________________________
## Unit J
### Exercise J
In this exercise we will be working with regular expressions that can be used to match something in a string.
In the subsequent Problem J, we will write Python code that uses regular expressions in functions imported from the re module .

**1. Write Regular Expressions that match:**
- zero or more A
- one or more A
- zero or one A
- two or three A

**2. What do these Regular Expressions match?**
- AB{3}
- (AB){3}

**3. Given the following regular expression: [^A-G] which of the following strings contain a match for this regular expression**
- A
- AB
- ADBC
- D

**4. Write a regular expression that matches a string containing exactly three characters.**

### Problem J

**Problem J part 1**

Read text input into a variabale named data.\
Write a raw sting containing a regular expression that matches a lower case a.\
Use the search function to see if the variable data contains a match. Print found if found, otherwise print not found.\
Test twice: with two presidents of the United States: "Harry S. Truman" and then "Dwight D. Eisenhower".

**Problem J part 2**

Read text input into a variabale named data.\
Write a raw sting containing a regular expression that contains a lower case b followed by a dot: 'b.'\
Use the findall function obtain a list of matching substrings. Print the resulting list.\
Test once with the string:\
"Dobby Rebeus Longbottom Gabrielle Albus"

**Problem J part 3**

Read text input into a variabale named data.\
Write a raw sting containing a regular expression that matches a space.\
Use the split function obtain a list of substrings seperated by a space. Print the resulting list.\
Test once with the string:\
"Bill Charlie Percy Fred George Ron Ginny"

**Problem J part 4**

Read text input into a variabale named data.\
Write a raw sting containing a regular expression that matches a lower case th\
Us the sub function to change 'th' to 'lore'. Print the resulting string.\
Test once with the string:\
"thlei, th, and folk tales"

