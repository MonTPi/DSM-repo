#format inputs


#initial support, use strip for string var
name = input('whats your name? ').strip()


print(f'Hello, {name}')

# Josh Lilley


# can we solve for ','
if "," in name:
    first, last = name.split(",")
    name = f'{first} {last}'


print(f'Hello, {name}')  

# Can we use re search to clean the input if , involved?

import re

match = re.search(r'^(.+) ?, ?(.+)$', name)
if match:
    name = match.group(1) + ' ' + match.group(2)

print(f'Hello, {name} re')  


# Simplify?
# := assigns a variable in the right side of th logic. 
# Walrus is used to assign & ask a bool, aka if & : simplification

if match := re.search(r'^(.+) ?, ?(.+)$', name):
    name = match.group(1) + ' ' + match.group(2)

print(f'Hello, {name} re:=')  


#### new task ###

# Asks for user name & I will clear up any error inputs

# https://twitter.com/JoshuaLilley18
url = input("URL: " ).strip()

print(url)


# Get username from format method:
if match := re.search(r'^(.+://.+.+/)(.+)$', url):
        Username =  match.group(2)

print(f'Hello, {Username}')  

# Get username from replace method:
# very fragile!!
Username = url.replace("https://twitter.com/","")

print(f'Username: {Username}')


# Get username from removeprefix method:
# slightly more specific incase other endings included.
Username = url.removeprefix("https://twitter.com/")

print(f'Username: {Username}')


# Get username from re.sub method:
# re.sub(pattern we want to look for, replace with, string that you want to perform it on)
# use the r".." script
User = re.sub(r"^(https?:(www\.)?//)?twitter\.com/$","",url)

print(f'Username: {User}')

# Get username from format method improved:
# starts with https or http: (might start with www. [?: dont count as group]) //twitter '.' com/(Username = group 1) ends with
if match := re.search(r"^https?:(?:www\.)?//twitter\.com/([a-z0-9_]+)$", url,re.IGNORECASE):
        Username =  match.group(1)

print(f'Hello, {Username}')  


from gitGo import git_go

git_go()