##
##  With the 'and" keyword we have the following return values:
#
#   True    and     True     >>>    True
#   True    and     False    >>>    False
#   False   and     True     >>>    False
#   False   and     False    >>>    False
# 
##  With the 'or" keyword we have the following return values:
#
#   True    and     True     >>>    True
#   True    and     False    >>>    True
#   False   and     True     >>>    True
#   False   and     False    >>>    False
# 
##  With the 'not" keyword we have the following return values: (one value)
#
#   not True    >>>    False
#   not False   >>>    True
# 

age1 = 27
age2 = 26
if(age1 >= 18 and age2 >= 18):
    print('You are both adults')
elif(age1 >= 18 or age2 >= 18):
    print('One of you is an adult')
else:
    print('You are both children')

is_hungry = False
if(not is_hungry):
    print('You are not hungry!')

is_hungry = True
if(not is_hungry):
    print('You are not hungry!')

##      More samples
#

x = 6
print(x > 4 and x < 12)

is_hungry = False
if(not is_hungry):
  print("You are not hungry")
else:
  print("You are hungry")

x = 6
print(x > 7 or x < 12)

is_hungry = True
if(not is_hungry):
  print("You are not hungry")
else:
  print("You are hungry")

x = 6
y = 7
print(x == y)


