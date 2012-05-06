import cgi
def escape(s):
    return cgi.escape(s, quote=True)
    
def rev_esc(s):
    for (a, i) in (('>', '&gt;'), 
                   ('"', '&quot;'), 
                   ('<', '&lt;'),
                   ('&', '&amp;')):
        s = s.replace(i, a)
    return s    
    
    
def rot13_char(c):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    size = len(alphabet)
    if c.lower() not in alphabet:
        return c
    up = False
    
    if c.isupper():
        up = True
        c = c.lower()
        
    rank = alphabet.index(c)
    res = alphabet[(rank+size/2) % (size)]
    return res if not up else res.upper()
    
def rot13_str(s):
    res = ''
    s = rev_esc(s)
    for c in s:
        res += rot13_char(c)
    res = escape(res)
    return res
       

print rot13_str('<Hello!> <b>hello<b/>')
print rev_esc(rot13_str('&lt;Uryyb!&gt; &lt;o&gt;uryyb&lt;o/&gt;'))
#print rot13_str('Uryyb!')
    