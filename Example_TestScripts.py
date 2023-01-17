
#call in the script you want to test
from CSP50_Lec9_UnitTest import ToThePower



#simple def main var set up (Not necassary if using pytest)
def main():
    Test_ToThePower()
    Test_ToThePower_2()
    testbasic()


#version 1 using basic
def Test_ToThePower():
    if ToThePower(2,2) != 4:
        print('error - (simple to the power error)')
    if ToThePower(10,10) != 10000000000:
       print('error - (simple to the power error)')

#version 2 using new 'assert' syntax
def Test_ToThePower_2():
    try:
      assert ToThePower(2,2) == 4
    except AssertionError:
      print('2^2 does not = 4')
    try:  
      assert ToThePower(10,10) == 10000000000
    except AssertionError:
        print('10^10 does not = error')
    try:  
      assert ToThePower(-2,2) == 4
    except AssertionError:
        print('10^10 does not = error')
    try:  
      assert ToThePower(0,0) == 0
    except AssertionError:
        print('0^0 does not = error')

#How to improve?

def testbasic():
 assert ToThePower(2,2) == 4
 assert ToThePower(10,10) == 10000000000

def testedge(): 
 assert ToThePower(-2,2) == 4
 assert ToThePower(0,0) == 0


 #test strings

 def strtest():
    for name in ['ben', 'sam', 'joe']:
        assert hello(name) == f'hello {name}'


if __name__ == '__main__':
    main()


     