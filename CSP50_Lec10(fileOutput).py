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

    ##READ extract text as var & then print names in var 'lines'
    with open("friends.txt",'r') as file:
        lines = file.readlines()
    
    for line in lines:
        print(f'hello {line.strip()}, U R A QT')

    #Simplify?? in read 'r' mode open file, read lines & print content
    with open("friends.txt",'r') as file:
        for line in file:
            print(f'hello, {line.strip()}')

    #'r' (read is implicit)
    #we are going to open & read a file, for reach line in the file we add it to friends
    #here we sort the list of friends extracted by the text file
    with open('friends.txt') as file:
        for line in file:
            friends.append(line.rstrip())

    for name in sorted(friends):
        print(f'hello, {name}')
        
    
   #Simplify?
    with open('friends.txt') as file:
        for line in sorted(file):
            print(f'hello, {line.strip().upper()}')

    #CSV files
    with open('friends.csv') as file:
        for line in sorted(file):
            row = line.strip().split(",")
            print(f'{row[0]} is {row[1]}')
    
    pals = []
    # open csv, for each row split the input by ','. create a dictionary called palz, append palz to a list for sorting.
    with open('friends.csv') as file:
        for line in (file):
            name,attribute = line.strip().split(",")
            palz = {}
            palz['name'] = name
            palz['attribute'] = attribute
            pals.append(palz)

    #for dictionary in list, print(...)  
    for palz in pals:
        print(f"{palz['name']} is {palz['attribute']}")

    # Simplify?
    with open('friends.csv') as file:
        for line in (file):
            name,attribute = line.strip().split(",")
            palz = {'name':name, 'attribute':attribute}
            pals.append(palz)

    # In order to get the name of a dictionary we need to call a function, then use this function as the key
    def get_name(pal):
        return palz['name']

    #Cannot sort dictionary, can sort list. for dictionary in list sorted by name() function.
    for palz in sorted(pals, key = get_name, reverse = False):
        print(f"{palz['name']} is {palz['attribute']}")


    #This is kinda pointless to use a function once..
    #Use lambda function
    for palz in sorted(pals, key= lambda palz:palz['name']):
        print(f"{palz['name']} is {palz['attribute']}")
    
    import csv

    #Of course there is a better way than manual CSV edit.
    with open('friends.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            pals.append({'name':row[0], 'attribute' : row[1]})
    
    pals = []

    #Simplify?
    with open('friends.csv') as file:
        reader = csv.reader(file)
        for name, attribute in reader:
            pals.append({'name': name, 'attribute' : attribute})


    pals = []


    #reading csv's - what if we dont know the collumns? Need to name first row (Collumn, names)
    with open('friends++.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pals.append({'name': row['name'], 'attribute' : row['attribute']})

    print(pals)
    pals = []

    #interacting with csv's 
    name = input('what is your name?')
    attribute = input('what is your strength?')

    with open('friends++.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name,attribute])
    
    #simplify as dictionary?
    name = input('what is your name?')
    attribute = input('what is your strength?')
    
    with open('friends++.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['name','attribute'])
        writer.writerow({'name': name, 'attribute': attribute})

#Image files using Pillow

    import pil

   
friends = []

if __name__ == '__main__':
    main()


