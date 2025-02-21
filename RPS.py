#RPS.py
#Name: Megann Wegner
#Date: 02/05/2025
#Assignment: Lab 3 Rock, Paper, Scissors
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  play = "yes"
  while play == "yes":
    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    #Ask the user if they would like to play again.

    player = input("Enter choice (rock, paper, scissors): ")
    
    computer = random.choice(["rock", "paper", "scissors"])

    if player == "rock":
      print("Player chose rock.")
    elif player == "paper":
      print("Player chose paper.")
    elif player == "scissors":
      print("Player chose scissors.")
    else:
      print("Invalid option.")

    if player == "rock":
      if computer == "rock":
        print("TIE!")
        ties = ties + 1
      if computer == "paper":
        print("You Lose.")
        losses = losses + 1
      if computer == "scissors":
        print("You Win!")
        wins = wins + 1
      
    if player == "paper":
      if computer == "paper":
        print("TIE!")
        ties = ties + 1
      if computer == "rock":
        print("You Lose.")
        losses = losses + 1
      if computer == "scissors":
        print("You Win!")
        wins = wins + 1

    if player == "scissors":
      if computer == "scissors":
        print("TIE!")
        ties = ties + 1
      if computer == "rock":
        print("You Lose.")
        losses = losses + 1
      if computer == "paper":
        print("You Win!")
        wins = wins + 1
      
    play = input("Play again? (yes or no): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
