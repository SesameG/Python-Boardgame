# python3 finalProjectCopy.py
import math
import random

# variables
userCount = 0
computerCount = 0
answer = 'play'

# -----------------------------functions ----------------------------------------
# text for beginning of every game
def instructions():
    print("\nhello, welcome to \"Apology\"!")
    print(" ~the python boardgame inspired by Sorry!~")
    print("the rules of the games are simple:")
    print("     - you and the computer are competing")
    print("     - whoever reaches 100 points first wins ")
    print("     - press the ENTER BAR during your turn to roll the dice")
    print("     - depending on the number rolled, you can lose or gain points")
    print("     - you can exit the game at any time")
    print("\n")

def intro_text():
    print(" -----------------------------------------------------")
    print("|      [type ENDGAME at any time to end the game]      |")
    print("|                        NEW GAME                      |")
    print(" -----------------------------------------------------")

# rule three function
def pickcard(count, x):
    cards = ["move up 5 spaces", "move back 5 spaces", "move up 2 spaces", "move back 2 spaces", "if you’re below 50pts, double ur score, if your above, divide ur score by two"]
    pickcard = input("\n" + x + "on a multiple of 10, press enter to see the card ")
    if pickcard == '':
        cardnum = random.randint(0,4)
        print(cards[cardnum])
        if cardnum == 0:
            count += 5
        elif cardnum == 1:
            count -= 5
        elif cardnum == 2:
            count += 2
        elif cardnum == 3:
            count -= 2
        elif cardnum == 4:
            if count < 50:
                count = count * 2
            elif count > 50:
                count = count / 2
    return count

# -------------------------proper code starts now-------------------------------

instructions()
intro_text()
while answer != 'ENDGAME': #lets you keep playing until you say EXIT
    answer = input("\npress ENTER to roll dice ")
    if answer == '': #rolls the dice
        userDice = random.randint(2,12) #what you land on
        print("\nyou rolled a", userDice)
        userCount= userCount + userDice
        print("your total score is:", userCount)

        computerDice = random.randint(2,12) #what the computer lands on
        print("\nthe computer rolled a", computerDice)
        computerCount= computerCount + computerDice
        print("the computer total score is:", computerCount)

# RULE ONE -------------------------------------
        if userCount==computerCount: #you and computer are equal
            if random.randint(1,2) == 1:
                print("\nyou have the same number as the computer, you've been randomly selected to go back to 0")
                userCount = 0
                print("your total score is:", userCount)
                # return userCount
            else:
                print("\nyou have the same number as the computer, the computer has been randomly selected to go back to 0")
                computerCount = 0
                print("the computer total score is:", computerCount)
                # return computerCount

# RULE TWO -------------------------------------
        elif userCount%7 == 0: #you are on multiple of 7
            print("\nyour score is a multiple of 7, you get 4 free points!")
            userCount = userCount+4
            print("your new total is:", userCount)

# RULE TWO.1 -------------------------------------
        elif computerCount%7== 0: #computer is on multiple of 7
            print("\nyour opponent's score is a multiple of 7, they get 4 free points!")
            computerCount = computerCount+4
            print("your opponents new total is:", computerCount)

# RULE THREE -------------------------------------
        elif userCount%10==0:
            name = "you are "
            userCount = pickcard(userCount, name)
            print("the new total is:", userCount)

# RULE THREE.1 -------------------------------------
        elif computerCount%10==0:
            name = "the computer is "
            computerCount = pickcard(computerCount, name)
            print("the new total is:", computerCount)

# RULE FOUR; WHEN SCORE IS 42 CAN SWITCH WITH OPPONENT
        if userCount == 42:
            switch = input("do you want to change spaces with the computer? Enter YES or NO: ")
            if switch.lower() == "yes":
                userCount = computerCount
                computerCount = 42
# RULE FOUR.1 -------------------------------------
        if computerCount == 42:
            switch = input("do you want to change spaces with the computer? Enter YES or NO: ")
            if switch.lower() == "yes":
                computerCount = userCount
                computerCount = 42


# -------------------------AFTER GAME-------------------------------
    # WIN OR LOOSE -------------------------------------
        elif userCount>= 100:
            print("\n")
            print("CONGRATS YOU WON THE GAME!!!")
            answer = input("type PLAY AGAIN to restart or ENDGAME to exit: ")
            if answer.lower() == 'play again':
                print("\n")
                intro_text()
                userCount = 0
                computerCount = 0

        elif computerCount > 100:
            print("           YOU LOST ... :( ")
            answer = input("type PLAY AGAIN to restart or ENDGAME to exit: ")
            if answer.lower() == 'play again':
                print("\n")
                intro_text()
                userCount = 0
                computerCount = 0
            else:
                break

    else:
        print("       ERROR")
        print("please press [ENTER] to roll dice")
        print("or type ENDGAME to exit, \nor type PLAY AGAIN to great a new game")
print("\nthank you for playing! see you next time.")
