'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit D, Problem D
'''
from collections import namedtuple
# Part One - List Comprehension
triangleNums = [i*(i+1)/2 for i in range(1, 11)]
print("First 10 Triangle numbers:")
print(triangleNums)

# Part Two - Sets
class1 = set({'Li', 'Audry', 'Jia', 'Migel', 'Tanya'})
class2 = set({'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'})
class3 = set({'Migel', 'Zhang', 'Hiroto', 'Anita', 'Jia'})
bothClasses = list(class1&class2&class3)
bothClasses.sort()
print("Students in all three classes:", bothClasses)
allStudents = list(class1|class2|class3)
allStudents.sort()
print("All students:", allStudents)
class1Only = set()
for student in class1:
    if student not in class2 and not (student in class3):
        class1Only.add(student)
class1Only = list(class1Only)
class1Only.sort()
print("Students in class1 but not class2 or class3:", class1Only)
class2Only = {student for student in class2 if student not in class1}
class2Only = list(class2Only)
class2Only.sort()
print("Students in class2 but not class1:", class2Only)

# Part Three – Tuple Basics
casablanca = ('Casablanca', '1942', 'romantic drama')
title, year, genre = casablanca
print("The genre of my favorite movie is:", genre)

# Part Four – Named Tuple
Movie = namedtuple('Movie', 'title year genre ')
movie = Movie('Casablanca', '1942', 'romantic drama')
print("My favorite movie is:", movie.title)

# Part Five – Named Tuple Containing a List
Moviestars = namedtuple('MovieStars', 'title year genre stars')
favoritemovie = Moviestars('Casablanca', '1942', 'romantic drama', ['Humphrey Bogart', 'Ingrid Bergman'])
favoritemovie.stars.append('Claude Rains')
print("My favorite star is:", favoritemovie.stars[1])
print(favoritemovie)

'''
Execution results:
First 10 Triangle numbers:
[1.0, 3.0, 6.0, 10.0, 15.0, 21.0, 28.0, 36.0, 45.0, 55.0]
Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
Students in class2 but not class1: ['Hiroto', 'Sasha']
The genre of my favorite movie is: romantic drama
My favorite movie is: Casablanca
My favorite star is: Ingrid Bergman
MovieStars(title='Casablanca', year='1942', genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])
'''