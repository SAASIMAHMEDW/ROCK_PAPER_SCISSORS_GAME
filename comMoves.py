
from random import shuffle,choice


def pickOne():
	gameOptions = ["ROCK",
								 "PAPER",
							"SCISSORS"]
	#print(gameOptions)
	shuffle(gameOptions)
	#print(gameOptions)
	comPicked = choice(gameOptions)
	#print(comPicked)
	return comPicked

#pickOne()
if __name__ == "__main__":
	x = pickOne()
	print(x)