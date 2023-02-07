### Object Oriented Programing ###

# We had algorithmic programs
# We had functional prgrams
# We can do object oriented


# Self is needed to store the values name etc...
# Validate user input? elo > 0 or name missing? We can use if not &  if to create value errors.
# we can catch these errors with try & exceptions.

class Player:
    def __init__(self,name,elo,open, piece) :
        if not name:
            raise ValueError("Your name is missing")
        self.name = name
        self.elo = elo
        self.open = open
        # A function inside of a class is a function
        self.piece = piece


    # This defines the string response to call class
    def __str__(self) :
        return f"Their name is {self.name} he has a {self.elo} rank. They opens with {self.open}."

    def charm(self):
        match self.piece:
            case "CASTLE":
                return '||'
            case "KNIGHT":
                return '<^^'




def main():
    player = get_chesser()
    print(f'{player.name} has an elo of {player.elo}. Opens with: {player.open}')
    # Alternative method to print a result, you can print the class but needs to define string
    print(player)
    print(player.charm())


## new function sets player = to class
def get_chesser() :
    name = input('Name: ')
    elo = int(input('elo: ')) 
    open = input('opening: ')
    piece = input('Prefer castle or knight?')
    try:
        return Player(name, elo, open,piece)
    except ValueError:
        name = input('Name: ')
        return Player(name, elo, open,piece)



if __name__ == '__main__':
    main()


