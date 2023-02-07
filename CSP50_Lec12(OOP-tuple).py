### Object Oriented Programing ###

# We had algorithmic programs
# We had functional prgrams
# We can do object oriented

# name, elo, Opening functions designed as a tuple
# cannot over write a tupple

def main():
    Chess = get_chesser()
    print(f'{Chess[0]} has {Chess[1]} ELO')


## return x,y  = tuple
def get_chesser() :
    name =  input('Name: ' )
    elo =  input('Elo: ' )
    return (name, elo)

if __name__ == '__main__':
    main()
#Can  return a list instead of a tupple []
# then: 
# Chess = get_chesser()
#    if Chess[0] == 'Josh':
#        Chess[1] = '1300'
#    print(f'{Chess[0]} has {Chess[1]} ELO')

# Would work.

