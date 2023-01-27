"""
R > S
S > P
P > R
"""

#from comMoves import pickOne
from colorama import Fore as F
from posFunction import rPS


print("\n"+" [ "+F.MAGENTA+"ROCK"+F.WHITE+"--"+F.MAGENTA+"PAPER"+F.WHITE+"--"+F.MAGENTA+"SCISSORS "+F.WHITE+"BY "+F.CYAN+"AHMED"+F.MAGENTA+"-"+F.CYAN+"ORACLE"+F.RESET+" ]")
print("\t<"+"-"*30+">\n")

userScore = None
comScore = None

RPS = ["ROCK","PAPER","SCISSORS"]
dummyListRPS = ["1 || ROCK","2 || PAPER","3 || SCISSORS"]

for options in dummyListRPS:
	print(options)
#print(RPS)

print("—"*20)
#print("ENTER YOUR CHOICE: ")
yourChoice = input("ENTER YOUR MOVES: ").upper()
if yourChoice in RPS:
	rPS(yourChoice)

else:
	print("\nINVALID INPUT\nOR YOUR SPELLING MAYBE WRONG\nIF YOUR SPELL IS WRONG\nTHEN ENTER CORRECT SPELL")

while True:
	print("—"*26)
	print ("\nWOULD YOU LIKE TO PLAY AGAIN\nY FOR YES\nN FOR NO\nE FOR EXIT")
	playAgain=input("ENTER YOUR CHOICE: ").upper()
	if playAgain=="Y":
		#print("ENTER YOUR MOVE: ")
		print("—"*26)
		userMoves=input("\nENTER YOUR MOVES: ").upper()
		if userMoves in RPS:
			rPS(userMoves)
		else:
			print("_"*26)
			print("\nNAHI HAI TERA MOVES")
			break
	elif playAgain=="N":
		print("_"*26)
		print("\nOKAY\nGAME ENDED")
		break
	elif playAgain=="E":
		print("_"*26)
		print("\nYOU HAVE BEEN EDITED SUCCESSFULLY!!!")
		break
	else:
		print("—"*26)
		print("\nSAHI WALA ENTER KAR!!!")
		
	
