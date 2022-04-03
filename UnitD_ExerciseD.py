'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit D, Exercise D
'''

# 1) Dictionary Basics:
fruitDesserts = {
    'apple' : 'sauce',
    'peach' : 'cobbler',
    'carrot' : 'cake',
    'strawberry' : 'sorbet',
    'banana' : 'cream pie'    
    }
fruitDesserts['mango'] = 'sticky rice'
fruitDesserts['strawberry'] = 'shortcake'
del fruitDesserts['carrot']
print("apple dessert is:", fruitDesserts.get('apple'))
print("banana dessert exists:", 'banana' in fruitDesserts)
print("pear dessert exists:", 'pear' in fruitDesserts)
print(fruitDesserts.keys())
print(fruitDesserts.values())
print(fruitDesserts.items())

# 2) Combining dictionaries:
capitols1 = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas' : 'Little Rock',
    'California' : 'Sacramento'    
    }
capitols2 = {
    'California' : 'Sac.',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford'    
    }
capitols1.update(capitols2)
sortedCapitols = list(capitols1.values())
sortedCapitols.sort()
print("Sorted state capitols:", sortedCapitols)

# 3) Sets Basics:
class1 = set({'Li', 'Audry', 'Jia', 'Migel', 'Tanya'})
class2 = set({'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'})
class1.add('John')
bothClasses = list(class1&class2)
bothClasses.sort()
print("Students in both classes:", bothClasses)
allStudents = list(class1|class2)
allStudents.sort()
print("Sasha is in class1:", allStudents)
print("Sasha is in class1:", 'Sasha' in class1)

'''
Execution results:
apple dessert is: sauce
banana dessert exists: True
pear dessert exists: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
Sorted state capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes: ['Audry', 'Migel', 'Tanya']
Sasha is in class1: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1: False
'''

