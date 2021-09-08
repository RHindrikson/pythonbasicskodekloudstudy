## ##  Python has 7 types of Arithmetic Operators
##
##      Add             +
##      Subtract        -
##      Multiply        *
##      Divide          /
##      Floor Divide    //
##      Modulo          %
##      Exponential >   **
##
##      For Exponential and Multiply:
##          if all values are integers, the result will be an integer
##          when at least one of the values is a float number, the reulst will be a flot number
print (2**3)
print( 2.**3.)
print( 2.**3)
print( 2**3.)
##      For Divide: indepentend of the types (integer or float) the result is alwasys a float
##          if all values are inte
print (10/2)
print (10./2.)
print (10./2)
print (10/2.)
##      For Floor Divivion
##          if all values are integers, the result will be an integer
##          when at least one of the values is a float number, the reulst will be a flot number
print (10//2)
print (10.//2.)
print (10.//2)
print (10//2.)
##          Note that the float rounds the result towards to the less integer value
#
print (6/4)
print (6.//4)
print (6./-4)
print (6.//-4)
##  Module
##
print(4%2)
print(5%2)
##
##  Operators Priority
#       **
#       *  then / then // then %
#       + and - (binary)
# 
print(10-6**2/9*10+1)  
##
##  From above:  
#       1st:    6 ** 2 = 36  then we have:  36/9*10
#       2nd:    36 / 9 = 4   then we have    4*10
#       (10 - 40 + 1)  = -29]
##
## more print samples
#
print(2 ** 3.)
print(10 / 2)
print(13 / 4 + 13 % 4)
print(2*(2+3))
print(2 ** 3)
print(6. // 4)
x = 10 / 4
y = 5 / 2.0
print (x + y)
print(9 % 4)
print(10 - 6 ** 2 / 9 * 10 + 1)
print(2 * 3 ** 3 * 4)
print(100/50)