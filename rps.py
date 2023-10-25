# import sys
# import random
# from enum import Enum
# class RPS(Enum):
#   ROCK = 1
#   PAPER = 2
#   SCISSORS = 3

# print("")
# playerchoice = input("Enter...\n1 for Rocks\n2 for Paper\n3 for Scissors\n\n")


# player = int(playerchoice)

# if player < 1 or player > 3:
#   print("invalid choice")
#   sys.exit("you must enter 1, 2, or 3")

# computerchoice = random.choice("123")


# print("")
# print("You chose: " + str(RPS(player)).replace('RPS.', '') )
# print("Python chose: " + str(RPS(computer)).replace('RPS.', ''))
# print("")



# if player == 1 and computer == 2:
#   print("You lose!")
# elif player == 1 and computer == 3:
#   print("You win!")
# elif player == 2 and computer == 1:
#   print("You win!")
# elif player == 2 and computer == 3:
#   print("You lose!")
# elif player == 3 and computer == 1:
#   print("You lose!")
# elif player == 3 and computer == 2:
#   print("You win!")
# elif player == computer:
#   print("It's a draw!")