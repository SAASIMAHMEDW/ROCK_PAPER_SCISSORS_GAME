
"""
R > S
S > P
P > R

ALL POSIBLE OUTCOMES
X   Rock vs Rock
X   PAPER VS PAPER
X   SCISSORS VS SCISSORS
Rock vs Paper
Rock vs Scissors
Paper vs Rock
Paper vs Scissors
Scissors vs Rock
Scissors vs Paper
"""

from comMoves import pickOne

# function for all possibilities in rock paper scissors game
def rPS(userChoice):
	print("\nYOUR MOVES IS: ", userChoice)
	comChoice = pickOne()
	print("COMPUTER MOVES IS: ", comChoice)
	if userChoice == comChoice:
		print("\nBOTH ARE EQUAL\nTIE IN THIS SITUATION")

	elif userChoice == "ROCK" and comChoice == "SCISSORS":
		print("\nROCK WIN!!!")
		print("ROCK WIN IN THIS SITUATION\nSO USER HAS WON THE GAME")

	elif userChoice == "SCISSORS" and comChoice == "PAPER":
		print("\nSCISSORS WIN!!!")
		print("SCISSORS WIN IN THIS SITUATION\nSO USER HAS WON THE GAME")

	elif userChoice == "PAPER" and comChoice == "ROCK":
		print("\nPAPER WIN!!!")
		print("PAPER WIN IN THIS SITUATION\nSO USER HAS WON THE GAME")

	elif userChoice == "SCISSORS" and comChoice == "ROCK":
		print("ROCK WIN!!!")
		print("FOCK WIN IN THIS SITUATION\nSO COM HAS WON THE GAME")

	elif comChoice == "PAPER" and userChoice == "ROCK":
		print("\nPAPER WIN!!!")
		print("PAPER WIN IN THIS SITUATION\nSO COM WON THE GAME")

	elif comChoice == "SCISSORS" and userChoice == "PAPER":
		print("\nSCISSORS WIN!!!")
		print("SCISSORS WIN IN THIS SITUATION\nSO COM WON THE GAME")

	elif comChoice == "PAPER" and userChoice == "ROCK":
		print("\nPAPER WIN!!!")
		print("PAPER WIN IN THIS SITUATION\nSO COM WON THE GAME")
