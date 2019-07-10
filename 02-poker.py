# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 完成一副扑克牌的发牌模拟程序
# ------------------------(max to 80 columns)-----------------------------------

# import some external moduls
import random
import codecs
import copy

# ------------------------(max to 80 columns)-----------------------------------
# main program start here

# --------------------------------------------------------
# Phase 1:  make a new deck of playing cards
# --------------------------------------------------------

# initialize var
# red joker-大王 black joker-小王
#cardJokers = ('Red Joker','Black Joker')
#cardJokers = ('RJ','BJ')
cardJokers = ('♞', '♘')

# heart-红桃 spade-黑桃 club-梅花 diamond-方块
#cardMarks = ('Heart','Spade','Club','Diamond')
cardMarks = ('♠', '♥', '♣', '♦')
#cardMarks = ('♤', '♡', '♧', '♢')

# 2,3,4,5,6,7,8,9,10,J,Q,K,A
#cardNumbers = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')
cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')

# make a deck of playing card
# add jokers first
deck = []
for c in cardJokers:
    deck.append(c)

# add 4x13 cards
for cn in cardNumbers:
    for cm in cardMarks:
        card = cm + cn
        deck.append(card)

print('\n-----------cutting line(1)---------------')
print('--debug: Create my deck, total cards is %d, detail is : \n%s : '
      % (len(deck), deck))

# write my new deck into a file
#f = open('new-deck.txt','w')
f = codecs.open("deck-new-54.txt", "w", "utf-8")
for card in deck:
    f.write(card)
    f.write('\t')
f.close

'''
# --------------------------------------------------------
# optional - make a deck for DouDiZhu
# method 1:

for pos in range(5):
    del deck[0]

del deck[-1]

# methon 2:
del deck[0:5]
del deck[-1]

print('--debug: Create my deck for DDZ, total cards is %d, detail is : \n%s : '
     % (len(deck), deck))

# write my new DDZ deck into a file1
#f = open('new-deck.txt','w')
f = codecs.open("deck-DDZ-48.txt","w","utf-8")
for card in deck:
    f.write(card)
    f.write('\t')
f.close
'''

# --------------------------------------------------------
# Phase 2:  shuffle
# --------------------------------------------------------
# methon 1:
'''
shuffledDeck = []
count = len(deck)
for i in range(count):
    pickedCard = random.choice(deck)
    shuffledDeck.append(pickedCard)
    deck.remove(pickedCard)
'''
# method 2:
shuffledDeck = copy.copy(deck)
random.shuffle(shuffledDeck)

print('\n-----------cutting line(2)---------------')
print('--debug: Shuffled my deck , remained cards is %d, detail is : \n%s : '
      % (len(deck), deck))
print('--debug: Shuffled my deck , new deck cards is %d, detail is : \n%s : '
      % (len(shuffledDeck), shuffledDeck))

# write my new deck into a file
#f = open('new-deck.txt','w')
f = codecs.open("deck-shuffled.txt", "w", "utf-8")
for card in shuffledDeck:
    f.write(card)
    f.write('\t')
f.close

# --------------------------------------------------------
# Phase 3:  deal
# --------------------------------------------------------
print('\n-----------cutting line(3)---------------')
numOfPlayers = 3
cardsOfPlayer = int(len(shuffledDeck) / numOfPlayers)
print('--debug: %d players, every one has %d cards.'
      % (numOfPlayers, cardsOfPlayer))

# methon 1: one by one
player1Cards = []
for i in range(cardsOfPlayer):
    pickedCard = random.choice(shuffledDeck)
    player1Cards.append(pickedCard)
    shuffledDeck.remove(pickedCard)
print('\n--debug: Player1''s %d cards is --  %s: '
      % (len(player1Cards), player1Cards))
print('--debug: Remained %d cards in shuffled deck is %s: '
      % (len(shuffledDeck), shuffledDeck))

player2Cards = []
for i in range(cardsOfPlayer):
    pickedCard = random.choice(shuffledDeck)
    player2Cards.append(pickedCard)
    shuffledDeck.remove(pickedCard)
print('\n--debug: Player2''s %d cards is --  %s: '
      % (len(player2Cards), player2Cards))
print('--debug: Remained %d cards in shuffled deck is %s: '
      % (len(shuffledDeck), shuffledDeck))

player3Cards = []
for card in shuffledDeck:
    player3Cards.append(card)
shuffledDeck = []
print('\n--debug: Player3''s %d cards is --  %s: '
      % (len(player3Cards), player3Cards))
print('--debug: Remained %d cards in shuffled deck is %s: '
      % (len(shuffledDeck), shuffledDeck))
