'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit H, Problem H
'''

#Part One - Operator Overloading
class BritCoins():
    def __init__(self, **kwargs):
        __coinValues = {"pound":240, "shilling":12, "penny":1} #value of each type of coin in pennies
        self.totalPennies = 0
        for k in kwargs.keys():
            for k2 in __coinValues.keys():
                if k == k2:
                    self.totalPennies += kwargs[k]*__coinValues[k2]
        
    def __add__(self, other):
        return BritCoins(penny=(self.totalPennies + other.totalPennies))
          
    def __sub__(self, other):
        return BritCoins(penny=(self.totalPennies - other.totalPennies))

    def __str__(self):
        pounds = self.totalPennies // 240
        shillings = (self.totalPennies % 240) // 12
        pennies = (self.totalPennies % 240) % 12
        return ("{} pounds {} shillings {} pennies".format(pounds, shillings, pennies))
        
dic = {"pound":4, "shilling":24, "penny":3}
c1 = BritCoins(**dic)
c2 = BritCoins(pound=3, shilling=4, penny=5)
c3 = c1 + c2
c4 = c1 - c2
print(c1)
print(c2)
print(c3)
print(c4)
print()

#Part Two - Pickling
import pickle
pickled = pickle.dumps(c4)
c4 = pickle.loads(pickled)
print(c4)

'''
Execution results:
5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies

1 pounds 19 shillings 10 pennies
'''