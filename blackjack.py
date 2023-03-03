import random
from blackjack_art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
playGame = input("Do you want to play a game of BlackJack : Type 'y' or 'n': ")
playerDeck = []
computerDeck = []
def results(playerDeck,computerDeck):
	playerScore =  calculateScore(playerDeck)
	computerScore = calculateScore(computerDeck)
	pdiff = 21 - playerScore
	cdiff = 21 - computerScore
	if(playerScore == computerScore):
		return "It is a Tie"
	elif(playerScore==21):
		return "You have won"
	elif(playerScore > 21):
		return "It's a bust"
	elif(computerScore>21):
		return "You lose"
	elif(pdiff < cdiff):
		return "You win"
	else:
		return "You lose"

def calculateScore(list):
	score = 0
	for i in list:
		score += i
	return score

def checkScore(list):
	finalScore = 0
	while(calculateScore(list)<=16):
		list.append(random.choice(cards))
		finalScore =  calculateScore(list)
	return finalScore
	
if(playGame == "y"):
	pcard1 = random.choice(cards)
	pcard2 = random.choice(cards)
	ccard1 = random.choice(cards)
	ccard2 = random.choice(cards)
	playerDeck.append(pcard1)
	playerDeck.append(pcard2)
	computerDeck.append(ccard1)
	computerDeck.append(ccard2)
	playerScore = calculateScore(playerDeck) 
	computerScore = calculateScore(computerDeck)
	print(f"Your cards: {playerDeck}, current score: {playerScore}")
	print(f"Computer's first card is {computerDeck[0]}")
	cont = input("Do you want to continue ? 'y' or 'no' : ")
	if(cont == "y"):
		pcard3 = random.choice(cards)
		playerDeck.append(pcard3)
		playerScore = calculateScore(playerDeck)
		print(f"Your cards: {playerDeck}, current score: {playerScore}")
		print(f"Computer's first card is {computerDeck[0]}")
		print(f"Your final cards are: {playerDeck}, current score: {playerScore}")
		computerScore = calculateScore(computerDeck)
		print(f"Computer's final cards are: {computerDeck}, computer score = {computerScore}")
		computerScore = checkScore(computerDeck)
			
	else:
		computerScore = checkScore(computerDeck)
		print(f"Your final cards are: {playerDeck}, current score: {playerScore}")
		computerScore = calculateScore(computerDeck)
		print(f"Computer's final cards = {computerDeck}, computer score = {computerScore}")
	print(results(playerDeck,computerDeck))
	
else:
	print("Have a Nice Day")
