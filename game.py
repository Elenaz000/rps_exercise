


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

print ("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print ("-------------------------------------------------------")
#ask for input
x=input("what is your choice? rock, paper, or scissors? ").lower()
option = ["rock", "paper", "scissors"]
#validate user's input
if x in option: 
    print ("You chose: '" + x + "'")

else: 
    print ("invalid data")
    exit ()

#computer choice

#could also do in this way 
#from random import choice
#computer_choice = choice (option)
import random
y = (random. choice (option))
print ("The computer chose: '" + y + "'")
print ("------------------------------------------------------")

#determine the winner
#first option you can do nested if statement
#adapted from eugenie from slack

#if user_choice == computer_choice:
#    print(“Both players played”, user_choice, “It’s a tie!“)
#elif user_choice == “paper”:
#    if computer_choice == “rock”:
#        print(“Paper covers rock. You won!“)
#    else:
#        print(“Scissors cuts paper. You lost! It’s ok.“)
#elif user_choice == “scissors”:
#    if computer_choice == “paper”:
#        print(“Scissors cuts paper. You won!“)
#    else:
#        print(“Rock crushes scissors. You lost! It’s ok.“)
#elif user_choice == “rock”:
#    if computer_choice == “scissors”:
#        print(“Rock crushes scissors. You won!“)
#    else:
#        print(“Paper covers rock You lost! It’s ok.“)

if (x == y) :
    print ("Oh, that is a tie.")
elif ((x == "rock") and (y == "paper")) :
    print ("Oh, the computer won. It's ok.")
elif ((x == "rock") and (y == "scissors")) :
    print ("You beat the computer!")

elif ((x == "paper") and (y == "rock")) :
    print ("You beat the computer!")
elif ((x == "paper") and (y == "scissors")) :
    print ("Oh, the computer won. It's ok.")

elif ((x == "scissors") and (y == "rock")) :
    print ("Oh, the computer won. It's ok.")
elif ((x == "scissors") and (y == "paper")) :
    print ("You beat the computer!")
   


#final result
print ("--------------------------------------------------------")
print ("Thanks for playing. Please play again!")