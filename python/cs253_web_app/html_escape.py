def escape(str):
    res = ''
    for s in str:
        if s == '<': res += '&lt;'
        elif s == '>': res += '&gt;'
        elif s == '&': res += '&amp;'
        elif s == '\"': res += '&quot;'
        else: res += s
    return res
    
#Steve Huffman's solution
def escape2(s):
    for (i, a) in (('&', '&amp;'), 
                   ('>', '&gt;'), 
                   ('"', '&quot;'), 
                   ('<', '&lt;')):
        s = s.replace(i, a)
    return s
    
import cgi
def escape3(s):
    return cgi.escape(s, quote=True)
    
#Peter Norvig's solution
#import string
#def escape4(s):
#    table = string.maketrans(('&', '&amp;'), 
#                       ('>', '&gt;'), 
#                       ('"', '&quot;'), 
#                       ('<', '&lt;'))
#    return s.translate(table)
    
    
    
print escape('&=&amp;')
print escape2('&=&amp;')
print escape3('&=&amp;')
#print escape4('&=&amp;')
    