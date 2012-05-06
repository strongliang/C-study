import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_pwd(password):
    print password
    return PWD_RE.match(password)
    
def valid_email(email):
    return EMAIL_RE.match(email)
    
#match = valid_username("a1ajsidfjisd")
match = valid_pwd("abcd")
#match = valid_email("abc@gmail.com")
if match:
    print match.group(0)
else:
    print "invalid password, " + str(match)