#how to output data outside of data
def main():

    name = input('what is your name?')
    friends.append(name)

    for name in sorted(friends):
        print(f'hello {name}')
    
    ##WRITE
    #We don't have to 'close' if  we use 'with' instead:
    #file = open("friends.txt", "a")
    with open("friends.txt","a") as file:
        file.write(f'{name}\n')
    #This can be skipped if we use 'with' instead
    ##file.close()

    ##READ
    with open("friends.txt",'r') as file:
        lines = file.readlines()
    
    for line in lines:
        print(f'hello {line.strip()}, U R A QT')

    #Simplify??
    with open("friends.txt",'r') as file:
        for line in file:
            print(f'hello, {line.strip()}')

    #'r' (read is implicit)
    ##we are going to open & read a file, for reach line in the file we add it to friends
    with open('friends.txt') as file:
        for line in file:
            friends.append(line.rstrip())

    for name in sorted(friends):
        print(f'hello, {name}')






friends = []

if __name__ == '__main__':
    main()
