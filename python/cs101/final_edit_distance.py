#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def rotate(word):
    # add the original word with no change
    res = [word]
    ch = 0
    changes = [0]

    for i in range(1, len(word)):
        new_word = word[i:] + word[0:i]
#        print new_word, 
        res.append(new_word)
        if i <= (len(word)-1) / 2:
            ch += i * 2
            changes.append(ch) # each rotation counts as 2 changes
        else:
            ch += (len(word)-1-i) * 2
            changes.append(ch) # each rotation counts as 2 changes
#        print res, changes
    return res, changes
    
def compare(s, t):
    dist_list = []
    rotations, changes = rotate(s)
    for i in range(len(rotations)):
        dist = changes[i]
        r = rotations[i]
        for i in range(len(s)):
            if r[i] != t[i]:
                dist += 1
        dist_list.append(dist)
    return min(dist_list)
    
def reduce(word, to_cut):
    res = []
    for i in range(len(word)):
        new_word = word[0:i] + word[i+1:]
        res.append(new_word)
    if to_cut == 1:
        return res
    else:
        new_res = []
        for w in res:
            new_res += reduce(w, to_cut-1)
        res += new_res
        return res        

def edit_distance(s,t):
    dist = 0
    if len(s) > len(t):
        short, long = t, s
    else:
        short, long = s, t
        
    diff = abs(len(s) - len(t))
    
    if diff > 0:
        cut_list = reduce(long, diff)
        dist_list = []
        for w in cut_list:
            dist_list.append(compare(short, w))
        dist += diff
        dist += min(dist_list)
    else:
        dist += compare(s, t)

    return dist

#For example:

## Delete the 'a'
#print edit_distance('audacity', 'udacity') 
##>>> 1
#
## Delete the 'a', replace the 'u' with 'U'
#print edit_distance('audacity', 'Udacity') 
##>>> 2
#
## Five replacements
#print edit_distance('peter', 'sarah') 
##>>> 5
#
## One deletion
#print edit_distance('pete', 'peter') 
##>>> 1

#print edit_distance('audacity', 'udacity')
##>>> 1
#print edit_distance('audacity', 'Udacity')
##>>> 2
#print edit_distance('peter', 'sarah')
##>>> 5
#print edit_distance('pete', 'peter')
##>>> 1
#print edit_distance('udc','audacity')
##>>> 5
#print edit_distance('audacity','udc')
##>>> 5
#print edit_distance('audacity', 'udacious')
##>>> 4
#print edit_distance('python', 'pytohn')
##>>> 2
#print edit_distance('udacity', 'university')
##>>> 6
#print edit_distance('university', 'udacity')
##>>> 6 

def Levenshtein(s, t):
    # for all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t;
    # note that d has (m+1)x(n+1) values
    m, n = len(s)+1, len(t)+1
    d = [[0 for col in range(n)] for row in range(m)]
        
    for i in range(m):
        d[i][0] = i  # the distance of any first string to an empty second string
    for j in range(n):
        d[0][j] = j  # the distance of any second string to an empty first string
    
    for j in range(1, n):
        for i in range(1, m):
            p, q = i-1, j-1
            if s[p] == t[q]:
                d[i][j] = d[i-1][j-1] # no operation required
            else:
                term1 = d[i-1][j] + 1 # a deletion
                term2 = d[i][j-1] + 1 # an insertion
                term3 = d[i-1][j-1] + 1 # a substitution
                d[i][j] = min(term1, term2, term3)
                
    return d[m-1][n-1]

def test_driver(s1, s2):
    print edit_distance(s1, s2)
    print Levenshtein(s1, s2)

test_driver('c++sdf', 'c#sdfd')
#print len('smotheredsdfdfdssdfsdfsdsdfsdfsdfsdfsd')
#print len('thereaabdfdsdfsdfsdfsdfsdfsdfsdfsddsdf')
#print edit_distance('smotheredsdfdfdssdfsdfsdsdfsdfsdfsdfsd','thereaabdfdsdfsdfsdfsdfsdfsdfsdfsddf')
#print edit_distance ("A man, a plan, a canal - Panama!", "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.")