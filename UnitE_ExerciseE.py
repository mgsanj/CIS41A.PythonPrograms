'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit E, Exercise E
'''

#Part One - If Logic
scifi = ["Alien", "Solaris", "Inception", "Moon"]
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"]
for i in range(3):
    movie = input("Please enter a movie title: ")
    if movie in scifi:
        print(movie, "is a scifi movie.")
    elif movie in comedy:
        print(movie, "is a comedy movie.")
    else:
        print("Sorry, I don't know what kind of movie {} is.".format(movie))
print()

#Part Two - Using Range
for i in range(10, -1, -2):
    print(i)
print()

#Part Three - Looping Through Dictionary Items
movies = {
    "The Wizard of Oz" : 1939,
    "The Godfather" : 1972,
    "Lawrence of Arabia" : 1962,
    "Raging Bull" : 1980,
}
for movie in sorted(movies):
    print(movie, "was made in", movies.get(movie))
    
'''
Execution results:
Please enter a movie title: Moon
Moon is a scifi movie.
Please enter a movie title: Superbad
Superbad is a comedy movie.
Please enter a movie title: Dunkirk
Sorry, I don't know what kind of movie Dunkirk is.

10
8
6
4
2
0

Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939
'''
    

