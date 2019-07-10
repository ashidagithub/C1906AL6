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

# ------------------------(max to 80 columns)-----------------------------------
# main program start here

# --------------------------------------------------------
# Phase 1:  make a new deck of playing cards
# --------------------------------------------------------

# initialize var
# red joker-大王 black joker-小王
#cardJokers = ('Red Joker','Black Joker')
#cardJokers = ('RJ','BJ')
cardJokers = ('♚','♛')

# heart-红桃 spade-黑桃 club-梅花 diamond-方块
#cardMarks = ('Heart','Spade','Club','Diamond')
cardMarks = ('♠', '♥', '♣', '♦')
#cardMarks = ('♤', '♡', '♧', '♢')

# 2,3,4,5,6,7,8,9,10,J,Q,K,A
#cardNumbers = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')
cardNumbers = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

# make a deck of playing card
# add jokers first
deck = []
for c in cardJokers:
    deck.append(c)

# add 4x13 card
for cn in cardNumbers:
    for cm in cardMarks:
        card = cm + cn
        deck.append(card)

print('--debug: Create my deck, total cards is %d, detail is : \n%s : '
     % (len(deck), deck))

# write my new deck into a file1
#f = open('new-deck.txt','w')
f = codecs.open("new-deck.txt","w","utf-8")
for card in deck:
    f.write(card)
    f.write('\t')
f.close


# --------------------------------------------------------
# optional - make a deck for DouDiZhu
# method 1:
'''
for pos in range(5):
    del deck[0]

del deck[-1]
'''
# methon 2:
del deck[0:5]
del deck[-1]

print('--debug: Create my deck for DDZ, total cards is %d, detail is : \n%s : '
     % (len(deck), deck))

# write my new deck into a file1
#f = open('new-deck.txt','w')
f = codecs.open("new-deck-DDZ.txt","w","utf-8")
for card in deck:
    f.write(card)
    f.write('\t')
f.close

# --------------------------------------------------------
# Phase 2:  shuffle
# --------------------------------------------------------
shuffledDeck = []
count = len(deck)

for i in range(count):
    pickedCard = random.choice(deck)