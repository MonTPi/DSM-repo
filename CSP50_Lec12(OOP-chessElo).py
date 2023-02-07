### Object Oriented Programing ###

# We had algorithmic programs
# We had functional prgrams
# We can do object oriented


def main():
    player = get_chesser()
    if player['name'] == 'Josh' :
        player['elo'] = '1300'
    print(f'{player["name"]} has {player["elo"]} ELO')


## return x,y  = tuple
def get_chesser() :
    name =  input('Name: ' ).strip()
    elo =  input('Elo: ' ).strip()
    return {'name' : name, 'elo' : elo}

if __name__ == '__main__':
    main()


