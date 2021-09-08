##
##  Bitwise Operators:  (helps you manipulate single bits of data)
#       &   >>>  Conjunction
#       |   >>>  Disjunction
#       ~   >>>  Negation
#       ^   >>>  Exclusive
#
#       two 1:
#             1  &  1   (returns 1 if both are 1s)
#      
#       At least one 1:
#               1   |   1
#               0   |   1
#               1   |   0
#
#       Exactly 1:      (XOR)
#               0   ^   1
#               1   ^   0
#####
#
#       15 & 22
#
print(bin(15))
print(bin(22))
#
#   Visualizing the bits of the numbers we have: (with & returns 1 if both are 1s)

#  For the 15:  0   0   0   0   1   1   1   1  
# 
#  For the 22:  0   0   0   1   0   1   1   0  
#
# Returns:(&)   0   0   0   0   0   1   1   0  (which correspondes to the integer "6")

print(15 & 22)

#   Visualizing the bits of the numbers we have:  (with | returns 1 if at least one is 1)

#  For the 15:  0   0   0   0   1   1   1   1  
# 
#  For the 22:  0   0   0   1   0   1   1   0  
#
# Returns:(|)   0   0   0   1   1   1   1   1  (which correspondes to the integer "31")

print(15 | 22)

#   Visualizing the bits of the numbers we have:  (with & returns 1 if only one is 1)

#  For the 15:  0   0   0   0   1   1   1   1  
# 
#  For the 22:  0   0   0   1   0   1   1   0  
#
# Returns:(|)   0   0   0   1   1   0   0   1  (which correspondes to the integer "25")

print(15 ^ 22)

#   Visualizing the bits of the numbers we have:  (returns 0 for every 1 and 1 for every 0)
#
#  For the 22:  0   0   0   1   0   1   1   0  
#
# Returns:(|)   1   1   1   0   1   0   0   1  (which correspondes to the integer "-23")

print(~22)

#  More samples

bit1 = 15
bit1 = bit1 & 22            
print(bit1)
bit1 = bit1 | 22
print(bit1)
bit1 = bit1 ^ 22
print(bit1)

bit1 = 15
bit1 &= 22
print(bit1)
bit1 |= 22
print(bit1)
bit1 ^= 22
print(bit1)

##  With bitshifting we move bits to the right or to the left
#       ">>"   >>> bit shift right
#       "<<"   >>> bit shift left
#
#   22  :  0  0   0   1   0   1   1   0
#   >> 1:  0  0   0   0   1   0   1   1     (which represents the integer "11")
#

print(22 >> 1)

#   22  :  0  0   0   1   0   1   1   0
#   >> 2: 0  0   0   0   0   1   0   1    (which represents the integer "5")
#
print(22 >> 2)

#   22  :  0  0   0   1   0   1   1   0
#   >> 1:  0  0   1   0   1   1   0   0     (which represents the integer "44")
#

print(22 << 1)


##  performing 1 bit right shifts is the same of an integer division by 2
##             2 bits right shifts is the same of an integer division by 4
#
print('='*10,'right bit shifting')
print(22 // 2)
print(22 >> 1)
print(22 // 4)
print(22 >> 2)

##  performing 1 bit left shifts is the same of an integer multiply by 2
##             2 bits left shifts is the same of an integer multiply by 4
#
print('='*10,'left bit shifting')
print(22 * 2)
print(22 << 1)
print(22 * 4)
print(22 << 2)

#
#  More samples

print('============= More Samples')

print('5^11: ', 5^11)

a = 20
b = 5
print("a & b =", a & b)

print(~200)

x=2
print('x << 4: ', x << 4)

x=2
print(x << 2)


a = 20
b = 5
print("a | b =", a | b)

print(int(1001))