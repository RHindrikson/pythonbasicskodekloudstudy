##
##  if/else statements allow us to conditionally run code

age = int(input('How old are you?'))

#if age >= 18:   # TRUE
#    print('You are an adult!!!')
#else:           # FALSE
#    print('You are not an adult!!!')

if age >= 18:   # TRUE
    if age == 18:   
        print('You are exactly 18 years old !!!')
    else:           # FALSE
        print('You older than 18 years old !!!')

if 4 + 5 == 10:
    print("TRUE")
else:
    print("FALSE")
print("TRUE")

x = 3
if ( x == 0 ):
  print("Am I here?")
elif ( x == 3 ):
  print("Or here?")
print("Or over here?")

a = 5
b = 10
if b < a:
  print("a is greater than b")
elif a == b:
  b = 5
  print("a and b are equal")
else:
  print("b is greater than a")

x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")

if(5,10): 
    print('hello')

x = 0
a = 6
b = 6
if a > 0:
    if b < 0: 
        x = x + 6 
    elif a > 6:
        x = x + 5
    else:
        x = x + 4
else:
    x = x + 3

print(x)

a = 5
b = 10
if b > a:
    print("b is greater than a")

#if age >= 18:   # TRUE    (firt condition)
#    print('You are an adult!!!')
#elif age >12 and < 18:    # (second condition)
#     print('You are a teen!!!')
#else:          # FALSE
#    print('You are a kid!!!')
