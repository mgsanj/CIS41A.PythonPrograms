'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit F, Problem F
'''

#Part One – Keyword Arguments and Default Values

def invoice(unitPrice, quantity, shipping = 10, handling = 5):
    print("Cost (unitPrice x quantity) =", unitPrice*quantity)
    print("Shipping = ", shipping)
    print("Handling =", handling)
    print("Total =", unitPrice*quantity+shipping+handling, "\n")

#Part Two – args (Variable-Length Arguments)

def printGroupMembers(groupName, *studentNames):
    print("Members of", groupName)
    for name in studentNames:
        print(name)

#Part Three – kwargs (Variable-Length Keyword Arguments)
def overseerSystem(**kwargs):
    if 'temperature' in kwargs:
        if kwargs['temperature'] > 500:
            print("Warning: temperature is", kwargs['temperature'])
    if 'CO2level' in kwargs:
        if kwargs['CO2level'] > 0.15:
            print("Warning: CO2level is", kwargs['CO2level'])
    if 'miscError' in kwargs:
        print("Misc error #" + str(kwargs['miscError']))
        
#Part Four – Working with a list of functions

def out():
    print("Out")
    return 0
    
def single():
    print("Single")
    return 1   
    
def double():
    print("Double")
    return 2
    
def triple():
    print("Triple")
    return 3   
    
def homeRun():
    print("homeRun")
    return 4


#Main function
def main():
    #part 1
    invoice(20, 4, shipping = 8)
    invoice(15, 3, handling = 15)
    
    #part 2
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
    printGroupMembers(*groupB)   
    print()
    
    #part 3
    Message1 = {"temperature" : 550}
    Message2 = {"temperature" : 475}
    Message3 = {"temperature" : 450,
                "miscError" : 404}
    Message4 = {"CO2level" : .17}
    Message5 = {"CO2level" : .2,
                "miscError": 418}
    overseerSystem(**Message1)
    overseerSystem(**Message2)
    overseerSystem(**Message3)
    overseerSystem(**Message4)
    overseerSystem(**Message5)
    print()
    
    #part 4
    import random
    
    outcomes = [out, single, double, triple, homeRun]
    probabilities = [70, 18, 5, 1, 6]    
    outs = 0
    while outs < 3:
        outcome = random.choices(outcomes, weights = probabilities, k = 1)
        if outcome[0]() == 0:
            outs += 1    
    
if __name__ == '__main__':
    main()

'''
Execution results:
Cost (unitPrice x quantity) = 80
Shipping =  8
Handling = 5
Total = 93 

Cost (unitPrice x quantity) = 45
Shipping =  10
Handling = 15
Total = 70 

Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto

Warning: temperature is 550
Misc error #404
Warning: CO2level is 0.17
Warning: CO2level is 0.2
Misc error #418

Single
Out
Out
homeRun
homeRun
Out

'''
     
        
    
