#1 Gold Star

#The built-in <string>.split() procedure works
#okay, but fails to find all the words on a page
#because it only uses whitespace to split the
#string. To do better, we should also use punctuation
#marks to split the page into words.

#Define a procedure, split_string, that takes two
#inputs: the string to split and a string containing
#all of the characters considered separators. The
#procedure should output a list of strings that break
#the source string up by the characters in the 
#splitlist.

#out = split_string("This is a test-of the,string separation-code!", " ,!-")
#print out => ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out."," .")
#print out => ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

# eat up all the separation chars until the next word
def next_start(source, end, splitlist):
    start = end
    while start != len(source):
        if splitlist.find(source[start]) == -1:
            break
        start += 1
    return start

def split_string(source, splitlist):
    split = []
    start = 0
    end = len(source)
    done = False
    while not done:
        done = True
        for e in splitlist:
            tmp_end = source.find(e, start)
            if tmp_end == -1:
                continue
            if tmp_end < end:
                end = tmp_end
                done = False
        if not done:
            split.append(source[start:end])
            start = next_start(source, end, splitlist)
            end = len(source)
        
    return split
    
print split_string("This is a test-of the,string separation-code!", " ,!-")
print split_string("After  the flood   ...  all the colors came out."," .")
