# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def is_palindrome(s):
    if s == '' or len(s) == 1:
        return True
    elif s[0].lower() != s[-1].lower():
        return False
    else:
        return is_palindrome(s[1:-1])  
        
def longest_subpalindrome_slice2(text):
    if text == '': return (0, 0)
    res = []
    res.append([])
    for i in range(len(text)):
        for j in range(i, len(text)):
            if is_palindrome(text[i:j+1]): # use j+1 to include text[j]
                res[-1] = [j-i, i, j+1] # the end idx is j + 1, not j
        res.append([])
#    print res
    slice = max(res)            
    return (slice[1], slice[2])
            
def find_next_center(str):
    if str=='': yield ['', 0, 0]
    else:
        start = 0
        res = ['', start, 0]
        prev = str[0]
        for i in range(len(str)):
            if str[i]==prev:
                res = [res[0]+str[i], res[1], i+1]
            else:
                prev = str[i]
                yield res
                res = [prev, i, i+1]
        yield res
        
def expand(text, start, end):
    if start==0 or end==len(text): 
        return None
    else:
        return [text[start-1:end+1], start-1, end+1]
        
def longest_subpalindrome_slice(text):
    text = str(text)
    if text=='': return (0, 0)
    res = []
    res.append([])
    for new_slice in find_next_center(text):
#        print new_slice
        while new_slice and is_palindrome(new_slice[0]):
            start, end = new_slice[1], new_slice[2]
            res[-1] = [start, end]
            new_slice = expand(text, start, end)
        res[-1] = [start, end]
        res.append([])
#    print res
#    print res[:-1]
    longest = max(res[:-1], key = lambda a: a[1]-a[0])
    print text[longest[0]:longest[1]]
    return (longest[0], longest[1])

        
            
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()