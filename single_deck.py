#!/usr/bin/env python
"""single_deck.py": A single deck blackjack simulator": single player, dealer stands on soft 17 and blackjack payout 2x"""
__author__ = "Ivan Hom"

#Limitations
#Splits
#-only allow one level of splits
#-only allow draw up to 4 cards after a split
#-only allow stand or hit after a split


DEBUG = 1

import random
random.seed(999)

MAX_NUMBER_HANDS = 10000 
MAX_NUMBER_DRAWS = 20


#setup deck
#a single deck, 4 suites C, H, S, D and 1/0 not dealt/already dealt
deck = {"C2": 1, "C3": 1, "C4": 1, "C5": 1, "C6": 1, "C7": 1, "C8": 1, "C9": 1, "C10": 1, "CJ": 1, "CQ": 1, "CK": 1, "CA": 1, "S2": 1, "S3": 1, "S4": 1, "S5": 1, "S6": 1, "S7": 1, "S8": 1, "S9": 1, "S10": 1, "SJ": 1, "SQ": 1, "SK": 1, "SA": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1, "D7": 1, "D8": 1, "D9": 1, "D10": 1, "DJ": 1, "DQ": 1, "DK": 1, "DA": 1, "H2": 1, "H3": 1, "H4": 1, "H5": 1, "H6": 1, "H7": 1, "H8": 1, "H9": 1, "H10": 1, "HJ": 1, "HQ": 1, "HK": 1, "HA": 1}  


#cards and their values
cards = {"C2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


#single deck strategy on https://wizardofodds.com/games/blackjack/strategy/1-deck/
#player has hard hand
hard_hand = [[], 
[0 ,0 ,"H", "H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H", "H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H", "H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H", "H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H", "H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H", "H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H", "H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"Dh","Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"Dh","Dh","Dh","Dh","Dh","Dh","Dh","H" ,"H" ,"H" ],
[0 ,0 ,"Dh","Dh","Dh","Dh","Dh","Dh","Dh","Dh","Dh","Dh"],
[0 ,0 ,"H" ,"H" ,"S" ,"S" ,"S" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"H" ,"H" ,"H" ,"Rh","Rh"],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ]]

soft_hand = [[], [], 
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"H" ,"H" ,"Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"Dh","Dh","Dh","Dh","Dh","H" ,"H" ,"H" ,"H" ,"H" ],
[0 ,0 ,"S" ,"Ds","Ds","Ds","Ds","S" ,"S" ,"H" ,"H" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"Ds","S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
[0 ,0 ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ]]

split_hand = [[], [], 
["X" ,"X" ,"Ph","P" ,"P" ,"P" ,"P" ,"P" ,"H" ,"H" ,"H" ,"H" ],
["X" ,"X" ,"Ph","Ph","P" ,"P" ,"P" ,"P" ,"Ph","H" ,"H" ,"H" ],
["X" ,"X" ,"H" ,"H" ,"Ph","Pd","Pd","H" ,"H" ,"H" ,"H" ,"H" ],
["X" ,"X" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ,"H" ],
["X" ,"X" ,"P" ,"P" ,"P" ,"P" ,"P" ,"Ph","H" ,"H" ,"H" ,"H" ],
["X" ,"X" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"Ph","H" ,"Rs","H" ],
["X" ,"X" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ],
["X" ,"X" ,"P" ,"P" ,"P" ,"P" ,"P" ,"S" ,"P" ,"P" ,"S" ,"S" ],
["X" ,"X" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ,"S" ],
["X" ,"X" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ,"P" ]]



#check for split_hand, must only be two cards
def check_if_split_hand(player_hand):
	#check only two cards
	number_cards = 0
	for iter in player_hand:
		number_cards += 1
	if number_cards > 2:
		return(0) #not split
		
	player_hand_0_face = player_hand[0][1:]
	player_hand_1_face = player_hand[1][1:]
	if (player_hand_0_face == player_hand_1_face):
		return(1) #is split
	else:
		return(0) #not split	


#check for soft_hand
def check_if_soft_hand(player_hand):
	for iter in player_hand:
		if ((iter == "HA") or (iter == "SA") or (iter == "CA") or (iter == "DA")) :
			return(1) #is soft_hand
		else:
			return(0) #not soft_hand


#single deck strategy with dealer stands on soft 17
def get_action(player_hand, dealer_hand, ignore_split = 0):
	dealer_card_value = return_value_of_card(dealer_hand[1])
	if DEBUG==1:
		print("inside get_action(), dealer_card_value=", dealer_card_value)

	#check if player_hand is split_hand
	if (check_if_split_hand(player_hand) and (ignore_split ==0)):
		if DEBUG ==1:
			print("inside get_action(), player_hand is split =", player_hand)
		player_card_value = return_value_of_card(player_hand[0])
		return(split_hand[player_card_value][dealer_card_value])

	#check if player_hand is soft_hand
	elif (check_if_soft_hand(player_hand)):
		if DEBUG ==1:
			print("inside get_action(), player_hand is soft hand =", player_hand)
		total_hand_value_low, total_hand_value_high = calc_hand_value(player_hand)
		if (total_hand_value_high <= 21):
			return(soft_hand[total_hand_value_high][dealer_card_value])
		elif (total_hand_value_low <= 21):
			return(soft_hand[total_hand_value_low][dealer_card_value])
		else:
			print("ERROR, player soft hand is out of range") 

	#else it is a hard hand
	if DEBUG ==1:
		print("inside get_action(), player_hand is hard hand =", player_hand)
	total_hand_value_low, total_hand_value_high = calc_hand_value(player_hand)
	return(hard_hand[total_hand_value_low][dealer_card_value])



#draw from deck
def draw_from_deck(deck):
	continue_select = 1 
	while continue_select == 1:
		card = random.choice(list(deck.keys()))	
		if deck[card] == 1:
			deck[card] = 0
			if DEBUG >1:
				print("in draw_from_deck: card =", card)
			return card


#return numerical value of card
def return_value_of_card(card):
	face = card[1:]
	if ((face == 'J') or (face == 'Q') or (face == 'K')):
		return(10)
	elif (face == 'A'):
		return(11)
	else: 
		return(int(face))


#return high/low numerical value of hand (trying to keep it simple by bounding it)
def calc_hand_value(hand):
	total_hand_value_low = 0 
	total_hand_value_high = 0 

	#now go through hand
	for iter in hand:
		value = return_value_of_card(iter)	
		if (value != 11): #Ace
			total_hand_value_low += value
			total_hand_value_high += value
		else:
			total_hand_value_low += 1
			total_hand_value_high += 11

        #adjust hand depending on how many As in the hand
	number_of_As_in_hand = 0
	for card_iter in hand:
		value = return_value_of_card(card_iter)
		if (value == 11):
			number_of_As_in_hand += 1
	if (number_of_As_in_hand >= 2):
		if ((total_hand_value_high > 17) and (total_hand_value_high <= 21)):
			pass
		elif (total_hand_value_high > 21):
			#reduce the use of one Ace
			total_hand_value_high = total_hand_value_high - 10

	if DEBUG >1:	
		print("inside calc_hand_value(), hand=", hand, "total_hand_value_low=", total_hand_value_low, "total_hand_value_high=", total_hand_value_high)
	return(total_hand_value_low, total_hand_value_high)



def check_for_blackjack(hand):
	hand_value_low, hand_value_high = calc_hand_value(hand)

	#check for blackjack
	if (hand_value_high == 21):
		if DEBUG >1:
			print("inside check_for_blackjack() is 21")
		return(1)
	else:
		if DEBUG >1:
			print("inside check_for_blackjack() not 21")
		return(0)
		

def play():
	#STEP0: init and draw hands
	#init
        #a single deck, 4 suites C, H, S, D and 1/0 not dealt/already dealt
	deck = {"C2": 1, "C3": 1, "C4": 1, "C5": 1, "C6": 1, "C7": 1, "C8": 1, "C9": 1, "C10": 1, "CJ": 1, "CQ": 1, "CK": 1, "CA": 1, "S2": 1, "S3": 1, "S4": 1, "S5": 1, "S6": 1, "S7": 1, "S8": 1, "S9": 1, "S10": 1, "SJ": 1, "SQ": 1, "SK": 1, "SA": 1, "D2": 1, "D3": 1, "D4": 1, "D5": 1, "D6": 1, "D7": 1, "D8": 1, "D9": 1, "D10": 1, "DJ": 1, "DQ": 1, "DK": 1, "DA": 1, "H2": 1, "H3": 1, "H4": 1, "H5": 1, "H6": 1, "H7": 1, "H8": 1, "H9": 1, "H10": 1, "HJ": 1, "HQ": 1, "HK": 1, "HA": 1}
	
	if DEBUG >1:
		print(deck)
		print(cards)

	#initial dealing of cards
	player_hand = []	
	player_hand2 = [] #split	
	dealer_hand = []
	
	#player and dealer stats
	player_has_21 = 0
	dealer_has_21 = 0
	player_bust = 0
	player2_bust = 0
	dealer_bust = 0
	player_stand = 0
	player2_stand = 0
	dealer_stand = 0
	player_surrender = 0
	player_double = 0
	player_dealer_draw_21 = 0
	player_split = 0
	result = []

	#draw initial hands 
	player_hand.append(draw_from_deck(deck))	
	dealer_hand.append(draw_from_deck(deck))
	player_hand.append(draw_from_deck(deck))
	dealer_hand.append(draw_from_deck(deck))
	print("player_hand =", player_hand)	
	print("dealer_hand =", dealer_hand)	


	#STEP1: check if dealer has 21
	#check if dealer has 21
	dealer_has_21 = check_for_blackjack(dealer_hand)
	if (dealer_has_21):
		print("dealer has 21")
	

	#STEP2: player draws
	player_has_21 = check_for_blackjack(player_hand)
	if (player_has_21):
		print("player has 21")

	if ((dealer_has_21 ==1) and (player_has_21 ==1)):
		player_dealer_draw_21 = 1
		print("player and dealer draw 21")


	#player draws
	number_draws = 0
	while ((number_draws < MAX_NUMBER_DRAWS) and (dealer_has_21 ==0) and (player_has_21 ==0) and (player_dealer_draw_21 ==0) and (player_bust ==0) and (player2_bust ==0)): 
		if (check_for_blackjack(player_hand)):
			player_stand = 1
			break

		action = get_action(player_hand, dealer_hand)
		print("this is the action=", action)

		if (action == "H"): 
			if DEBUG ==1:
				print("player hit")
			drawn_card = draw_from_deck(deck)
			print("player drawn_card =", drawn_card)
			player_hand.append(drawn_card)
			if DEBUG ==1:
				print("player_hand =", player_hand)
			player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
			if ((player_hand_value_high > 21) and (player_hand_value_low > 21)): #player bust
				player_bust = 1
				break

		if ((action == "P") or (action == "Pd") or (action == "Ph")): #split
			player_split = 1
			if DEBUG ==1:
				print("player split and hit")
			split_card = player_hand.pop(1) #remove card from player_hand
			player_hand2.append(split_card) #append card to player_hand2

			#FIRST hand 
			drawn_card = draw_from_deck(deck)
			print("player_hand drawn_card =", drawn_card)
			player_hand.append(drawn_card)
			if DEBUG ==1:
				print("this is FIRST split player_hand =", player_hand)
			player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)

			#action after first drawn card
			action1 = get_action(player_hand, dealer_hand, 1)
			print("this is the action for hand1 =", action1)

			if ((action1 == "H") or (action1 == "Rh") or (action1 == "Dh")):
				if DEBUG ==1:
					print("player hit")
				drawn_card = draw_from_deck(deck)
				print("player drawn_card =", drawn_card)
				player_hand.append(drawn_card)
				if DEBUG ==1:
					print("player_hand =", player_hand)
				player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
				if ((player_hand_value_high > 21) and (player_hand_value_low > 21)): #player bust
					player_bust = 1
				elif ((player_hand_value_high > 17) or (player_hand_value_low > 17)): #player stand 
					player_stand = 1

			elif (action1 == "S"):
				if DEBUG ==1:
					print("player stand")
				player_stand = 1

			#action after second drawn card
			if ((player_stand ==0) and (player_bust ==0)):
				action1 = get_action(player_hand, dealer_hand, 1)
				print("this is the action for hand =", action1)

				if ((action1 == "H") or (action1 == "Rh") or (action1 == "Dh")):
					if DEBUG ==1:
						print("player hit")
					drawn_card = draw_from_deck(deck)
					print("player drawn_card =", drawn_card)
					player_hand.append(drawn_card)
					if DEBUG ==1:
						print("player_hand =", player_hand)
					player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
					if ((player_hand_value_high > 21) and (player_hand_value_low > 21)): #player bust
						player_bust = 1
					elif ((player_hand_value_high > 17) or (player_hand_value_low > 17)): #player stand
						player_stand = 1

				elif (action1 == "S"):
					if DEBUG ==1:
						print("player stand")
					player_stand = 1
			
			#action after third drawn card
			if ((player_stand ==0) and (player_bust ==0)):
				action1 = get_action(player_hand, dealer_hand, 1)
				print("this is the action for hand1 =", action1)

				if ((action1 == "H") or (action1 == "Rh") or (action1 == "Dh")):
					if DEBUG ==1:
						print("player hit")
					drawn_card = draw_from_deck(deck)
					print("player drawn_card =", drawn_card)
					player_hand.append(drawn_card)
					if DEBUG ==1:
						print("player_hand =", player_hand)
					player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
					if ((player_hand_value_high > 21) and (player_hand_value_low > 21)): #player bust
						player_bust = 1
					elif ((player_hand_value_high > 17) or (player_hand_value_low > 17)): #player stand
						player_stand = 1

				elif (action1 == "S"):
					if DEBUG ==1:
						print("player stand")
					player_stand = 1

			#action after fourth drawn card
			if ((player_stand ==0) and (player_bust ==0)):
				action1 = get_action(player_hand, dealer_hand, 1)
				print("this is the action for hand1 =", action1)

				if ((action1 == "H") or (action1 == "Rh") or (action1 == "Dh")):
					if DEBUG ==1:
						print("player hit")
					drawn_card = draw_from_deck(deck)
					print("player drawn_card =", drawn_card)
					player_hand.append(drawn_card)
					if DEBUG ==1:
						print("player_hand =", player_hand)
					player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
					if ((player_hand_value_high > 21) and (player_hand_value_low > 21)): #player bust
						player_bust = 1
					elif ((player_hand_value_high > 17) or (player_hand_value_low > 17)): #player stand
						player_stand = 1

				elif (action1 == "S"):
					if DEBUG ==1:
						print("player stand")
					player_stand = 1

			
			#SECOND hand
			if DEBUG ==1:
				print("this is the SECOND split hand player_hand2 =", player_hand2)
			drawn_card = draw_from_deck(deck)
			print("player_hand2 drawn_card =", drawn_card)
			player_hand2.append(drawn_card)
			if DEBUG ==1:
				print("player_hand2 =", player_hand2)
			player_hand2_value_low, player_hand2_value_high = calc_hand_value(player_hand2)

			if ((player_hand2_value_high > 21) and (player_hand2_value_low > 21)): #player2 bust
				player2_bust = 1

			#action after first drawn card
			action2 = get_action(player_hand2, dealer_hand, 1)
			print("this is the action for hand2 =", action2)

			if ((action2 == "H") or (action2 == "Rh") or (action2 == "Dh")):
				if DEBUG ==1:
					print("player2 hit")
				drawn_card = draw_from_deck(deck)
				print("player2 drawn_card =", drawn_card)
				player_hand2.append(drawn_card)
				if DEBUG ==1:
					print("player_hand2 =", player_hand2)
				player_hand2_value_low, player_hand2_value_high = calc_hand_value(player_hand2)
				if ((player_hand2_value_high > 21) and (player_hand2_value_low > 21)): #player2 bust
					player2_bust = 1
				elif ((player_hand2_value_high > 17) or (player_hand2_value_low > 17)): #player2 stand
					player2_stand = 1
		

			elif (action2 == "S"):
				if DEBUG ==1:
					print("player2 stand")
				player2_stand = 1
				break

			if ((player2_stand ==0) and (player2_bust ==0)):
				#action after second drawn card
				action2 = get_action(player_hand2, dealer_hand, 1)
				print("this is the action for hand2 =", action2)

				if ((action2 == "H") or (action2 == "Rh") or (action2 == "Dh")):
					if DEBUG ==1:
						print("player2 hit")
					drawn_card = draw_from_deck(deck)
					print("player2 drawn_card =", drawn_card)
					player_hand2.append(drawn_card)
					if DEBUG ==1:
						print("player_hand2 =", player_hand2)
					player_hand2_value_low, player_hand2_value_high = calc_hand_value(player_hand2)
					if ((player_hand2_value_high > 21) and (player_hand2_value_low > 21)): #player2 bust
						player2_bust = 1
					elif ((player_hand2_value_high > 17) or (player_hand2_value_low > 17)): #player2 stand
						player2_stand = 1

				elif (action2 == "S"):
					if DEBUG ==1:
						print("player2 stand")
					player2_stand = 1


			if ((player2_stand ==0) and (player2_bust ==0)):
				#action after third drawn card
				action2 = get_action(player_hand2, dealer_hand, 1)
				print("this is the action for hand2 =", action2)

				if ((action2 == "H") or (action2 == "Rh") or (action2 == "Dh")):
					if DEBUG ==1:
						print("player2 hit")
					drawn_card = draw_from_deck(deck)
					print("player2 drawn_card =", drawn_card)
					player_hand2.append(drawn_card)
					if DEBUG ==1:
						print("player_hand2 =", player_hand2)
					player_hand2_value_low, player_hand2_value_high = calc_hand_value(player_hand2)
					if ((player_hand2_value_high > 21) and (player_hand2_value_low > 21)): #player2 bust
						player2_bust = 1
					elif ((player_hand2_value_high > 17) or (player_hand2_value_low > 17)): #player2 stand
						player2_stand = 1

				elif (action2 == "S"):
					if DEBUG ==1:
						print("player2 stand")
					player2_stand = 1


			if ((player2_stand ==0) and (player2_bust ==0)):
				#action after fourth drawn card
				action2 = get_action(player_hand2, dealer_hand, 1)
				print("this is the action for hand2 =", action2)

				if ((action2 == "H") or (action2 == "Rh") or (action2 == "Dh")):
					if DEBUG ==1:
						print("player2 hit")
					drawn_card = draw_from_deck(deck)
					print("player2 drawn_card =", drawn_card)
					player_hand2.append(drawn_card)
					if DEBUG ==1:
						print("player_hand2 =", player_hand2)
					player_hand2_value_low, player_hand2_value_high = calc_hand_value(player_hand2)
					if ((player_hand2_value_high > 21) and (player_hand2_value_low > 21)): #player2 bust
						player2_bust = 1
					elif ((player_hand2_value_high > 17) or (player_hand2_value_low > 17)): #player2 stand
						player2_stand = 1

				elif (action2 == "S"):
					if DEBUG ==1:
						print("player2 stand")
					player2_stand = 1


		elif (action == "Dh"):
			if DEBUG ==1:
				print("player double and hit")
			drawn_card = draw_from_deck(deck)
			print("player drawn_card =", drawn_card)
			player_hand.append(drawn_card)
			player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
			player_stand = 1
			player_double = 1
			break #can only hit once on a double

		elif (action == "S"):
			if DEBUG ==1:
				print("player stand")
			player_stand = 1
			break		

		elif (action == "Ds"):
			if DEBUG ==1:
				print("player double and stand")
			player_stand = 1
			player_double = 1
			break

		elif ((action == "Rs") or (action == "Rh")):
			#only surrender if first hand of two cards
			if (len(player_hand) == 2):
				if DEBUG ==1:
					print("player surrender")
				player_surrender = 1
				break
			elif (action == "Rs"):
				if DEBUG ==1:
					print("player stand")
				player_stand = 1
				break
			elif (action == "Rh"):
				if DEBUG ==1:
					print("player hit")
				drawn_card = draw_from_deck(deck)
				print("player drawn_card =", drawn_card)
				player_hand.append(drawn_card)
				if DEBUG ==1:
					print("player_hand =", player_hand)
				player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
				if ((player_hand_value_high > 21) and (player_hand_value_low > 21)): #player bust
					player_bust = 1
					break


		number_draws += 1



	#STEP3: dealer draws
	#dealer draws
	if ((player_stand ==1) and (dealer_has_21 ==0)):
		dealer_hand_value_low, dealer_hand_value_high = calc_hand_value(dealer_hand)
		while ((dealer_hand_value_high < 17) or (dealer_hand_value_low < 17)):  
			if DEBUG ==1:
				print("dealer_hand=", dealer_hand, "dealer_hand_value_low=", dealer_hand_value_low, "dealer_hand_value_high=", dealer_hand_value_high)
			if (((dealer_hand_value_low > 17) and (dealer_hand_value_low <= 21)) or ((dealer_hand_value_high > 17) and (dealer_hand_value_high <= 21))): #dealer stand
				break
			drawn_card = draw_from_deck(deck)
			print("dealer drawn_card =", drawn_card)
			dealer_hand.append(drawn_card)
			dealer_hand_value_low, dealer_hand_value_high = calc_hand_value(dealer_hand)
			if DEBUG ==1:
				print("dealer_hand=", dealer_hand, "dealer_hand_value_low=", dealer_hand_value_low, "dealer_hand_value_high=", dealer_hand_value_high)
			if ((dealer_hand_value_low > 21) and (dealer_hand_value_high > 21)): #dealer bust
				dealer_bust =1		
				break
			elif (((dealer_hand_value_low > 17) and (dealer_hand_value_low <= 21)) or ((dealer_hand_value_high > 17) and (dealer_hand_value_high <= 21))): #dealer stand 
				break


	#STEP4: Compare hands
	#compare hands
	if (player_dealer_draw_21 ==1):
		print("DRAW")
		result.append("DRAW")
	elif (dealer_has_21 ==1):
		print("DEALER_HAS_BJ")
		result.append("DEALER_HAS_BJ")
	elif (player_has_21 ==1):
		print("PLAYER_HAS_BJ")
		result.append("PLAYER_HAS_BJ")
	elif (player_bust ==1):
		if (player_double ==1):
			print("DEALER_DOUBLE")
			result.append("DEALER_DOUBLE")
		else:
			print("DEALER")
			result.append("DEALER")
	elif (dealer_bust ==1):
		if (player_double ==1):
			print("PLAYER_DOUBLE")
			result.append("PLAYER_DOUBLE")
		else:
			print("PLAYER")
			result.append("PLAYER")
	elif (player_surrender ==1): 
		print("PLAYER_SURRENDER")
		result.append("PLAYER_SURRENDER")
	if ((player_stand ==1) and (dealer_bust ==0)):
		player_hand_value_low, player_hand_value_high = calc_hand_value(player_hand)
		dealer_hand_value_low, dealer_hand_value_high = calc_hand_value(dealer_hand)
		player_diff = 21 - player_hand_value_high
		if (player_diff < 0):
			player_diff = 21 - player_hand_value_low
		dealer_diff = 21 - dealer_hand_value_high
		if (dealer_diff < 0):
			dealer_diff = 21 - dealer_hand_value_low
		if (player_diff == dealer_diff):
			print("DRAW")
			result.append("DRAW")
		elif (player_diff < dealer_diff):
			if (player_double ==1):
				print("PLAYER_DOUBLE")
				result.append("PLAYER_DOUBLE")
			else:
				print("PLAYER")
				result.append("PLAYER")
		else:
			if (player_double ==1):	
				print("DEALER_DOUBLE")
				result.append("DEALER_DOUBLE")
			else:
				print("DEALER")
				result.append("DEALER")

	#check for split hand
	if (player_split ==1):
		if (player2_bust ==1):
			if (player_double ==1):
				print("DEALER_DOUBLE")
				result.append("DEALER_DOUBLE")
			else:
				print("DEALER")
				result.append("DEALER")
		elif (dealer_bust ==1):
			if (player_double ==1):
				print("PLAYER_DOUBLE")
				result.append("PLAYER_DOUBLE")
			else:
				print("PLAYER")
				result.append("PLAYER")
		if ((player2_stand ==1) and (dealer_bust ==0)):
			player2_hand_value_low, player2_hand_value_high = calc_hand_value(player_hand2)
			dealer_hand_value_low, dealer_hand_value_high = calc_hand_value(dealer_hand)
			player2_diff = 21 - player2_hand_value_high
			if (player2_diff < 0):
				player2_diff = 21 - player2_hand_value_low
			dealer_diff = 21 - dealer_hand_value_high
			if (dealer_diff < 0):
				dealer_diff = 21 - dealer_hand_value_low
			if (player2_diff == dealer_diff):
				print("DRAW")
				result.append("DRAW")
			elif (player2_diff < dealer_diff):
				if (player_double ==1):
					print("PLAYER_DOUBLE")
					result.append("PLAYER_DOUBLE")
				else:
					print("PLAYER")
					result.append("PLAYER")
			else:
				if (player_double ==1):	
					print("DEALER_DOUBLE")
					result.append("DEALER_DOUBLE")
				else:
					print("DEALER")
					result.append("DEALER")
	#return results
	return(result)
	

def main():
	number_hands = 0
	player_won_count = 0
	dealer_won_count = 0
	player_has_bj_count = 0
	dealer_has_bj_count = 0
	player_surrender_count = 0
	player_double_won_count = 0
	dealer_double_won_count = 0
	draw_count = 0

	#assume player $1 bet on each hand and starts with $100, blackjack pays 2X
	player_bet = 1
	player_amount = 500

	while ((number_hands < MAX_NUMBER_HANDS) and (player_amount >0)):	
		result = play()
		for result_iter in result:
			if (result_iter == "PLAYER"): #player won
				player_won_count += 1
				player_amount += player_bet
			elif (result_iter == "PLAYER_DOUBLE"): #player won double
				player_double_won_count += 1
				player_won_count += 1
				player_amount += (2 * player_bet)
			elif (result_iter == "DEALER_DOUBLE"): #dealer won but player lost double
				dealer_double_won_count += 1
				dealer_won_count += 1
				player_amount -= (2 * player_bet)
			elif (result_iter == "DEALER"): #dealer won
				dealer_won_count += 1
				player_amount -= player_bet
			elif (result_iter == "DRAW"): #draw
                        	draw_count += 1
			elif (result_iter == "DEALER_HAS_BJ"): #dealer won blackjack
				dealer_has_bj_count += 1
				dealer_won_count += 1
				player_amount -= player_bet
			elif (result_iter == "PLAYER_HAS_BJ"):  #player won blackjack, payout 2X
				player_has_bj_count += 1
				player_won_count += 1
				player_amount += (2.5 * player_bet)
			elif (result_iter == "PLAYER_SURRENDER"): #player surrender, lose half bet
				player_surrender_count += 1
				dealer_won_count += 1
				player_amount -= (.5 * player_bet) 
			else:
				print("ERROR, do not recognize result=", result)

		print("number_hands =", number_hands)
		print('\n')
		number_hands += 1

		print("INT STATS: total_hands =", number_hands, "player_amount = ", player_amount, "player =", player_won_count, "dealer =", dealer_won_count, "draw =", draw_count, "dealer_has_bj =", dealer_has_bj_count, "player_has_bj =", player_has_bj_count, "player_surrender_count =", player_surrender_count, "player_double_won_count =", player_double_won_count, "dealer_double_won_count =", dealer_double_won_count)
		print('\n' + '\n')


	print("FINAL STATS: total_hands =", number_hands, "player_amount = ", player_amount, "player =", player_won_count, "dealer =", dealer_won_count, "draw =", draw_count, "dealer_has_bj =", dealer_has_bj_count, "player_has_bj =", player_has_bj_count, "player_surrender_count =", player_surrender_count, "player_double_won_count =", player_double_won_count, "dealer_double_won_count =", dealer_double_won_count)


if __name__ == "__main__":
	main()



