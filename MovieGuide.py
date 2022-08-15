import os
operation= 0
MovieList = []
def Menu ():
    valid = False
    print("\nCOMMAND MENU\n list - List all movies\n add - Add a movie\n del - Delete a movie\n exit - Exit program")
    
    while valid != True:
        command = input("Command: ")
        print(command)
        
        if command == "list":
            operation = 1
            valid = True
        elif command == "add":
            operation=2
            valid = True
        elif command == "del":
            operation =3
            valid = True
        elif command == "exit":
            operation = 4
            valid = True
        else:
            print("Not a valid command. Please try again.")
    return int(operation)

def populateList(MovieList):
    f = open("movies.txt","r")
    
    for x in f:
        MovieList.append(x)


def displayMovies(MovieList):
    for i in range(len(MovieList)):
        print(str(i+1)+". "+MovieList[i])

def addMovie(MovieList):
    valid = False
    name = input("Name: ")
    while valid ==False:
        if len(name) ==0:
            print("Name cannot be empty")
            name = input("Name: ")
        elif len(name) >0:
            MovieList.append(name)
            valid = True

def writeToFile(MovieList):
    f = open("movies.txt","a+")
    
    for x in MovieList:
        new = True
        for y in f:
            if str(x)==str(y):
                print("Movie already exist in file")
                new = False
                break
        if new == True:
            f.write("%s\n"%x)


def delMovie(MovieList):
    valid = False
    while valid == False:
        num = int(input("Number: "))
        if num > len(MovieList):
            print("\nInvalid movie number")
        else:
            MovieList.pop(num-1)
            valid = True

def delMovieFromFile(MovieList):
    
    os.remove("movies.txt")
    f = open("movies.txt","w")
    for x in MovieList:
        f.write("%s\n"%x)
    

operation = Menu()
populateList(MovieList)

while operation !=4:
    if operation == 1:
        displayMovies(MovieList)
        operation = Menu()
    if operation == 2:
        addMovie(MovieList)
        writeToFile(MovieList)
        displayMovies(MovieList)
        operation = Menu()
    if operation == 3: 
        delMovie(MovieList)
        delMovieFromFile(MovieList)
        displayMovies(MovieList)
        operation = Menu()
print("Bye!")
