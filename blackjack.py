import random
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
playGame = input("Do you want to play a game of BlackJack : Type 'y' or 'n': ")
playerDeck = []
computerDeck = []

def results(playerScore,computerScore):
	pdiff = 21 - playerScore
	cdiff = 21 - computerScore
	if(playerScore == computerScore):
		return "It is a Tie"
	elif(computerScore==21):
		return "You lost, oppenent has the BlackJack"
	elif(playerScore ==21):
		return "You win, You have the BlackJack"
	elif(playerScore > 21):
		return "It's a bust"
	elif(computerScore > 21):
		return "The computer has a bust"
	elif(pdiff < cdiff):
		return "You win"
	else:
		return "You lose"

def calculateScore(list):
	finalScore = sum(list)
	if 11 in list and  finalScore >21:
		list.remove(11)
		list.append(1)
	finalScore = sum(list)
	return finalScore

def sum (list):
	score = 0
	for i in list:
		score += i
	return score
def checkScore(list):
	finalScore = calculateScore(list)
	while(finalScore<=16):
		list.append(random.choice(cards))
		finalScore =  calculateScore(list)
	return finalScore

def inputInList(list,numberOfElements):
	for i in range(0,numberOfElements):
		list.append(random.choice(cards)) 
	return list

if(playGame == "y"):
	playerDeck = inputInList(playerDeck,2)
	computerDeck = inputInList(computerDeck,2)
	playerScore = calculateScore(playerDeck) 
	computerScore = calculateScore(computerDeck)
	print(f"Your cards: {playerDeck}, current score: {playerScore}")
	print(f"Computer's first card is {computerDeck[0]}")
	cont = input("Do you want to continue ? 'y' or 'n' : ")
	if(cont == "y"):
		playerDeck = inputInList(playerDeck,1)
		playerScore = calculateScore(playerDeck)
		print(f"Your cards: {playerDeck}, current score: {playerScore}")
		print(f"Computer's first card is {computerDeck[0]}")
		print(f"Your final cards are: {playerDeck}, current score: {playerScore}")
		computerScore = checkScore(computerDeck)
		print(f"Computer's final cards are: {computerDeck}, computer score = {computerScore}")
			
	else:
		computerScore = checkScore(computerDeck)
		print(f"Your final cards are: {playerDeck}, current score: {playerScore}")
		computerScore = calculateScore(computerDeck)
		print(f"Computer's final cards = {computerDeck}, computer score = {computerScore}")
	print(results(playerScore,computerScore))
	
else:
	print("Have a Nice Day")
