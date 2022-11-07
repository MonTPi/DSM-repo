


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

#Dictionary
edgeRunner = {'dave':"super suit",'jack': "Hacker", 'josh': 'mega penis'}
#prints dave's dictionary term
print(edgeRunner["dave"]) 
#for i (conditional var) in dictionary, print i & print dictionary item, seperate with 'x'
def main():
 for Runner in edgeRunner:
  print(Runner , edgeRunner[Runner], sep=(' has power: '))

#Var assigned to dictionary
edgeRunner = {'dave':'super suit','jack': 'Hacker', 'josh': 'mega penis'}

main()

## Multi point dictionary, seperate lines for readabillity using \, None = no value, this is a list of dictionaries.
ER = [\
    {"name":"Dave", "power":"super suit", "role":"main character"},\
    {"name":"jack", "power":"hacker", "role":"side character"},\
    {"name":"Josh", "power":"mega penis", "role": None}
]
#calling dicrtionary definiation in list 
for R in ER:
    print(R["name"], R["power"], R["role"], sep=", ")


## super mario blocks
#Lets call the level design
def main():
  column(int(input('how high? ')))
  row(int(input('how long? ')))
  block(int(input('how big? ')))

# using a for loop based on input. each loop concatanates the code.
def column(hight):
    for _ in range(hight):
     print('#')

#using a python string * var set up to produce a single row string.
def row(length):
    print('|?|' * length )

#using both to create a x by x block.
def block(size):
    #sets hight
    for _ in range(size):
    #sets length
     print("# " * size)

main()

