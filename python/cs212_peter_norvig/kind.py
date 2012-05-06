# -----------
# User Instructions
# 
# Define a function, kind(n, ranks).

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
     
    ht = {}
    for r in ranks:
        if r not in ht:
            ht[r] = 1
        else:
            ht[r] += 1
    for e in ht:
        if ht[e] == n:
            return e
            
    #peter's solution
#    for r in ranks:
#        if ranks.count(r) == n: return r
#    return None
        
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