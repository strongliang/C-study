# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if word.isupper():
        num = ''    
        for i in range(len(word)):
                num += word[i]+'*10**'+str(len(word)-i-1)+'+'
    else:
         return word
        
    return num[:-1]
    
    
# Peter's solution
def compile_word2(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) 
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'        
    else:
        return word
    
print compile_word("HELLO")
print compile_word2("HELLO")