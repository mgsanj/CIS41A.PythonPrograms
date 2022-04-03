'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit C, Problem C
'''
# Script 1: Working with Lists
list1 = []
list1.append(1)
list1.append(3)
list1.append(5)
def swapPos(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
swapPos(list1, 1, 2)
print("Items in list1:")
for i in range(len(list1)):
    print(list1[i])
list2 = [1, 2, 3, 4]
list3 = list1 + list2
print("list3 is:", list3)
print("list3 contains a 3:", 3 in list3)
print("list3 contains {} 3s".format(list3.count(3)))
print("The index of the first 3 contained in list3 is", list3.index(3))
first3 = list3.pop(list3.index(3))
print("first3 =", first3)
list4 = sorted(list3)
print("list3 is now:", list3)
print("list4 is:", list4)
print("Slice of list3 is:", list3[2:5])
print("Length of list3 is", len(list3))
print("The max value in list3 is", max(list3))
list3 = sorted(list3)
print("Sorted list3 is:", list3)
list5 = [list1] + [list2]
print("list5 is:", list5)
print("Value 4 from list5:", list5[1][3])


'''
Execution results:
Items in list1:
1
5
3
list3 is: [1, 5, 3, 1, 2, 3, 4]
list3 contains a 3: True
list3 contains 2 3s
The index of the first 3 contained in list3 is 2
first3 = 3
list3 is now: [1, 5, 1, 2, 3, 4]
list4 is: [1, 1, 2, 3, 4, 5]
Slice of list3 is: [1, 2, 3]
Length of list3 is 6
The max value in list3 is 5
Sorted list3 is: [1, 1, 2, 3, 4, 5]
list5 is: [[1, 5, 3], [1, 2, 3, 4]]
Value 4 from list5: 4
'''



