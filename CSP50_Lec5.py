
##Syntax error:
from ast import Try
from re import X
import string
from symbol import try_stmt


print('hello, world)
#FIX - check error & fix

###Value (input) error:
x = int(input('what is number?'))
print(f"x is {x}")
#input = T

#FIX
try: 
    x = int(input('what is number?'))
    #print will not fail.. do not include in try:
    print(f"x is {x}")
    except ValueError:
    print("X must be number not text")

##IMPROVE
try: 
#single evaluation try:
    x = int(input('what is number?'))
except ValueError:
    print("X must be number not text")
#if x != int, immidiatly -> except & doesnt assign
else:
    print(f"x is {x}")

##IMPROVE  2.0
#incurs loop until correct value given.
while True:
  try: 
    x = int(input('what is number?'))
  except ValueError:
     print("X must be number not text")
  else:
    break
print(f"x is {x}")


###Function
def main()
 x = get_int()
 print(f"x is {x}")

def get_int():
    while True:
    try: 
        x = int(input('what is number?'))
    except ValueError:
        print("X must be number not text")
    else:
        return x

main()

###Function 2.0
def main():
     x = get_int()
     print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input('what is number? '))
        except ValueError:
            print("X must be number not text")    
main()

###Function 3.0
def main():
     x = get_int('what is your number? ')
     print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
#Soft nudge rather than error message: pass (begins the next loop)
            pass  
main()

