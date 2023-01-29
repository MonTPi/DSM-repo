#Check that regular inputs have been collected


#initial support, use strip for string var
email = input('whats your email? ').strip()


if "@" in email:
    print('Valid @ email')
else:
    print('Invalid email')


#Can we improve? 
#josh.lilley98@gmail.com

if "@" in email and "." in email:
    print('Valid @ & . email')
else:
    print('Invalid email')

#Can we improve? 
username, domain = email.split("@")

if username and "." in domain:
    print('Valid username & domain')
else: 
    print('Invalid email')

#Can we improve?

if username and domain.endswith('.com'):
    print('Valid username & .com domain')
else: 
    print('Invalid email')

#Better approuch using re

import re

if re.search("@", email):
    print('Valid @ re.email')
else:
    print('Invalid email')


##Re : Syntax
# .     : any character except a newline
# *     : 0 or more repetitions
# +     : 1 or more repetitions
# ?     : 0 or 1 repetition
# {m}   : m repetitions
# {m,n} : m-n repetitions
# ^     : starts with..
# $     : ..ends with
# []    : Match these charaters
# [^]   : Dont match these charaters
# \d    : decimal digit
# \D    : non-decimal digit
# \s    : white space
# \S    : non-white space
# \w    : word character & numbers + _
# \W    : non-word character & numbers + _


if re.search(".+@.+", email):
    print('Valid simple shape re.email')
else:
    print('Invalid email')

# This is a finite state process that accepts as valid if ends in final state

# Can we improve?
# Backslash breaks the interpreter, the r'' string formats it raw rather than use \ as a function

if re.search(r".+@.+\.com", email):
    print('Valid shape re.email')
else:
    print('Invalid email')

# Can we improve?
# sentances that contain an email still works.. We can make it check just the email:

if re.search(r"^.+@.+\.com$", email):
    print('Valid start & end shape re.email')
else:
    print('Invalid email')

# [^@] : anything but the @ sign is ok.

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print('Valid non-@ repetition re.email')
else:
    print('Invalid email')

# [a-zA-Z] : any letter from a-z is ok.

if re.search(r"^[a-zA-Z1-9_\.]+@[a-zA-Z1-9_]+\.com$", email):
    print('Valid characters re.email')
else:
    print('Invalid email')

# \w : any alphanumeric from a-z is ok. | : or

print(email)

if re.search(r"^\w+.\w+@\w+\.com$", email.lower()):
    print('Valid w re.email')
else:
    print('Invalid email')

# email.lower() or re.IGNORECASE do the same thing.. re.MULTILINE or re.DOTALL
# this is preference but maybe you dont want to risk changing the actual email?

if re.search(r"^\w+(\.)?\w+@\w+\.(com|co\.uk)$", email, re.IGNORECASE):
    print('Valid w re.email')
else:
    print('Invalid email')


# Currently I am getting around josh'.' by using '\w+.'
# this wont work for @something.cognino.com
# (\w+\.)? = (any letter, 1 or more times, a litteral '.'), repeated 0 or 1 time

if re.search(r"^(\w+\.)?\w+@(\w+\.)?\w+\.(com|co\.uk)$", email, re.IGNORECASE):
    print('Valid . re.email')
else:
    print('Invalid email')

# The offcial go to is the regular email:
if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9- ]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9- ]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE):
    print('Valid REAL re.email')
else:
    print('Invalid email')

# Josh.lilley98@gmail.com