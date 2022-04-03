'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit G, Problem G
'''

#Part One – Reading a data file
fin = open('States.txt', 'rt')
lines = fin.readlines()
fin.close()
greatestPopulation = 0
largestState = ""
for line in lines:
    listState = line.split()
    abbrev = listState[0]
    region = listState[1]
    population = int(listState[2])
    if region == "Midwest":
        if population > greatestPopulation:
            greatestPopulation = population
            largestState = abbrev
print("Highest population state in the Midwest is:", largestState, greatestPopulation)

 
#Part Two - A Dictionary of Lists
fin = open('USPresidents.txt', 'rt')
lines = fin.readlines()
fin.close()
usPresidentDict = dict()
for line in lines:
    s = line.split()
    if s[0] in usPresidentDict:
        usPresidentDict[s[0]].append(s[1])
    else:
        usPresidentDict[s[0]] = [s[1]]
keyVal = ""
length = 0
print(usPresidentDict)
for key in usPresidentDict:
    if (len(usPresidentDict[key])>length):
        length = len(usPresidentDict[key])
        keyVal = key
print("\nThe state with the most presidents is", keyVal, "with", length, "presidents")
for value in usPresidentDict[keyVal]:
    print(value)


#Part Three - Dictionary Keys and Sets
newDict = {state:len(presidentList) for state, presidentList in usPresidentDict.items()}
print(newDict)
mostPopular = ['CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']
newSet = set()
for state in mostPopular:
    if state in newDict:
        newSet.add(state + ' ' + str(newDict[state])) 
print('\n8 of the 10 high population states have had presidents born in them: ')
newSet = list(newSet)
newSet.sort()
for state in newSet:
    print(state)


'''
Execution results:
Highest population state in the Midwest is: IL 12802000

The state with the most presidents is VA with 8 presidents
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor

8 of the 10 high population states have had presidents born in them: 
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2
'''