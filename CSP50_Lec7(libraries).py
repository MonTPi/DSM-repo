#Code pre written that can be used in your project. Moduels do a single process.
##can you module rather than copy & paste

#random mods are basic functionality. - doc.python/3/library/python.html

#brings all of the content in random, must use random.***
from ast import Index
import random
#by loading a specific function from the random import we can just use choice()
from random import choice


#both types of function call
def main():
 coin = random.choice(seq)
 print(coin)
 coin1 = choice(seq)
 print(coin1)

seq = ["heads","tails"]

main()

number = random.randint(1,20)
print(number)

cards = ['mel','bazukus', 'josh']

random.shuffle(cards)
for card in cards:
    print(card)



import statistics

score = statistics.mean([100,90,77])
print(score)


#command line arguments
import sys

#argument vector, is a list of all elements typed in the human prompt
sys.argv

#if I call the file in the terminal & include an augment the augument will be in argv[1]
#... +/VisualStudio/DSM-repo/CSP50_Lec7(libraries).py" Josh
try:
    print('hello, my name is not', sys.argv[1])
except IndexError:
    print("needs an augument")

##Can we remove all the error checks from the main code we are interested in.
#error checks
if len(sys.argv) == 3 :
    sys.exit('hello,', sys.argv[1], sys.argv[2])
elif len(sys.argv) < 2 :
    sys.exit("too few")

#code interested in #see argv[1: ] starts at 1 not 0 , :-1 would remove somone from the end
for arg in sys.argv[1: ]:
    print('Hello, ' , arg)

##Lets install packages other than the pre made sets
#3rd party functions can be called by importing packages
#pyPI = pypi.org is home to many

import cowsay

import sys

if len(sys.argv) == 2:
    cowsay.trex("hello" + sys.argv[1])

#python -m pip install
##Shift^ + command + P 
## python select interpretor

###API's
##pulling a txt file from a website api, search the documentation for the api
#often this will be a url 
#Json files are text formatted in a specific way

#for api
import requests
# for command line intrerface
import sys
#helps to format json files
import json


##exits program if incorrectly formatted
if len(sys.argv) != 2:
    sys.exit()
##attempts to make a request for data on a song, stores as var
response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2))

o = response.json()

for result in o['results'] :
    print(result['trackName'])
    print(result['trackPrice'])

from gitGo import git_go 

git_go()