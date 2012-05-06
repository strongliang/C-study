# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling
import copy
# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 
#print mydeck

def deal(numhands, n=5, deck=mydeck):
    # Your code here.
#    if n*numhands > len(deck):
#        return None
#    copy_deck = copy.deepcopy(deck)
#    return [ [copy_deck.pop(int(random.random()*len(copy_deck))) for i in range(n) if len(copy_deck)>0] for j in range(numhands) ] #need to make a copy of mydeck, otherwise it wipes it out
    
    #Peter
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

print mydeck    
print deal(11)
print mydeck
