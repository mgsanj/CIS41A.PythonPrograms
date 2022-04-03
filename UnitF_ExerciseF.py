'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit F, Exercise F
'''

#Part One – Using a main function, Docstrings
def hello():
    'This function prints Hello World'
    print("Hello World")
def main():
    hello()
    print("Help on function hello in module", __name__, ":\n")    
    print("hello()\n", hello.__doc__)
    main.myList = [i for i in range(3)]
    main.myInt = 3
if __name__ == '__main__':
    main()


#Part Two – Error Handling
def printListElement(list1, index):
    try: 
        print(list1[index])
    except:
        print("\nError: bad index number.\n")

printListElement(main.myList, 3)


#Part Three – How Python function arguments are treated
print("Original ID of myInt in main is", id(main.myInt))
print("Original ID of myList in main is", id(main.myList))
print("Original ID of myList's last element in main is", id(main.myList[-1]))
def byVal(arg):
    print("Original ID of parameter in byVal", id(arg))
    arg += 7
    print("ID of parameter in byVal after change", id(arg))
def byRef(arg1):
    print("Original ID of parameter in byRef", id(arg1))
    print("Original ID of parameter's last element in byRef", id(arg1[-1]))
    arg1[-1] += 7
    print("ID of parameter in byRef after change", id(arg1))
    print("ID of parameter's last element in byRef after change", id(arg1[-1]))
    
byVal(main.myInt)
byRef(main.myList)
print("ID of myInt in main after call to byVal is", id(main.myInt))
print("ID of myList in main after call to byRef is", id(main.myList))
print("ID of myList's last element in main after call to byRef is", id(main.myList[-1]))
print("myInt is now:", main.myInt) 
print("myList is now:", main.myList)

'''
The results are like this because Python functions treat their arguments by their values. So when a function has an argument, the variable in which it refers to changes
based on what the function wants to do to the variable.
'''

'''
Execution results:
Hello World
Help on function hello in module __main__ :

hello()
 This function prints Hello World

Error: bad index number.

Original ID of myInt in main is 4553662192
Original ID of myList in main is 4566086664
Original ID of myList's last element in main is 4553662160
Original ID of parameter in byVal 4553662192
ID of parameter in byVal after change 4553662416
Original ID of parameter in byRef 4566086664
Original ID of parameter's last element in byRef 4553662160
ID of parameter in byRef after change 4566086664
ID of parameter's last element in byRef after change 4553662384
ID of myInt in main after call to byVal is 4553662192
ID of myList in main after call to byRef is 4566086664
ID of myList's last element in main after call to byRef is 4553662384
myInt is now: 3
myList is now: [0, 1, 9]

'''