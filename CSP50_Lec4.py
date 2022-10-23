


#____ meow loops meow while X < 5
def loopmeow():
    # x starts @ 0 by convention
    x = 0
    while x < 5:
     print('meow')
    # x += 1 == x = x+1
     x += 1


loopmeow()
     

#____ 4Meow loop recreates the above loop using a list
for _ in range(3):
    print("meow")

print('meow\n' * 3, end="")

#____ looped 'get n' error message + Meow function

def getnumber():
    while True:
      n = int(input('How many meows?'))
      if n > 0:
        break
    return n

def main():
    meow(getnumber())

def meow(n):
    for _ in range(n):
     print('meow')

main()

# ____ list - cyber punk

edgeRunners = ['dave','jack', 'josh']

print(edgeRunners[2])

# ____ list - cyber punk

edgeRunners = ['dave','jack', 'josh']

for edgeRunners in edgeRunners :
    print(edgeRunners)

#for variable i in.. = i = 0, then i = 1, then i = 2. 
#range = how many am I going to name? len prodivdes and int value required for range
for i in range(len(edgeRunners)):
    print(i+1,edgeRunners[i])

#dictionary - associate a list with something else. AKA words with deffinitions.
#second list to link.
mods = ['super suit', 'hacker', 'mega penis']

edgeRunner = {'dave':"super suit",'jack': "Hacker", 'josh': 'mega penis'}

print(edgeRunner["dave"])
