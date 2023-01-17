
def main():
    X = int(input('What is X? '))
    N = int(input('To the power of? '))
    print(f'Your answer : {X} ^ {N} =', ToThePower(X,N))
    whatname('ben')

def ToThePower(X,N):
    return  X**N



## For test scripts you need to return a value not just print 

def whatname(name):
    name = input('what is your name?')
    print(hello(name))
    

def hello(name='ben'):
    return f'hello, {name}'


if __name__ == '__main__':
    main()