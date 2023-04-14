# rock paper scissors game
import random

def win():
    print("Computer: ", computer)
    print("Player: ", player)
    print("You Win!")
    print("---------------------------------")
def lose():
    print("Computer: ", computer)
    print("Player: ", player)
    print("You Lose!")
    print("---------------------------------")
    
while True:
    choices = ["rock", "paper", "scissors", "lizard", "spock", "chuck norris"]
    computer = random.choice(choices)
    player = None # initialize player before loop
    while player not in choices:
        player = input("Please choose: \nRock, Paper, Scissors, Lizard, or Spock?: \n").lower()
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("It is a tie, try again.\n")
        
    elif player == "rock":
        if computer == "paper" or computer == "spock":
            lose()
        if computer == "scissors" or computer == "lizard":
            win()
            
    elif player == "paper":
        if computer == "scissors" or computer == "lizard":
            lose()
        if computer == "rock" or computer == "spock":
            win()
            
    elif player == "scissors":
        if computer == "rock" or computer == "spock":
            lose()
        if computer == "paper" or computer == "lizard":
            win()
            
    elif player == "lizard":
        if computer == "rock" or computer == "scissors":
            lose()
        if computer == "paper" or computer == "spock":
            win()
            
    elif player == "spock":
        if computer == "paper" or computer == "lizard":
            lose()
        if computer == "rock" or computer == "scissors":
            win()
            
    elif player == "chuck norris":
        print("The computer gets roundhoused kicked in the ram")
        win()
    elif computer == "chuck norris":
        print("He is behind you... there is no hope")
        lose()
            
            
    play_again = input("Play again? (yes/no)\n").lower()
    if play_again != "yes":
        break
print("\nThanks for playing Rock, Paper, Scissors, Lizard, Spock!")  


