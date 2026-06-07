#File: bowling.py
#Description: A program that calculates a bowler's Average and handicap after three games.
#Assignment 4

    #Name: Enoch Shamo Abbey
    #Index No: 2425404607
    #Email : 2425404607@live.gctu.edu.gh
    #Grader: Augustus Buckman
    #
    # On my honor,Enoch Shamo Abbey, this programming assignment is my own work
    #and I have not provided this code to any other student.

#THE NAME THAT IS TO BE INPUTTED
name = input("Enter a name: ")
#THE INPUT OF GAME 1 , 2 and 3
game1 = int(input("Enter a Game 1: "))
game2 = int(input("Enter a Game 2: "))
game3 = int(input("Enter a Game 3: "))
#THE FORMULAR FOR FINDING THE AVERAGE OF THE THREE GAMES
average = (game1 + game2 + game3) // 3
#THE FORMULAR FOR FINDING FOR THE HANDICAP
handicap = int((200 - average) * 0.8)

print(name + "'s average is:", average)
print(name + "'s handicap is:", handicap)

