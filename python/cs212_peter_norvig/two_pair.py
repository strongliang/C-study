# -----------
# User Instructions
# 
# Define a function, two_pair(ranks).

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
#    pair1 = kind(2, ranks)
#    if pair1 == None: return None
#    
#    pair2 = None
#    for r in ranks:
#        if r!=pair1 and ranks.count(r)==2:
#            pair2 = r
#            
#    if pair2 == None: return None
#    return (pair1, pair2)
    
    # Peter Norvig
    pair1 = kind(2, ranks)
#    pair2 = kind(2, list(reversed(ranks)))
    pair2 = kind(2, reversed(ranks))
    if pair1 and pair2 != pair1:
        return (pair1, pair2)
    else:
        return None

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5s 5D 9H 9C 6S".split() # Two Pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks
    
print test()