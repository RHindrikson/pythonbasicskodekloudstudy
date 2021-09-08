##
##  While brings a condition that will be executed while is not true (loop)
#

secret_number = 3
guess = int(input('Guess a number: '))

while guess != secret_number:   # condition is TRUE
    guess = int(input('Guess a number: '))
else:                           # condition is FALSE
    print('Congratulations, you got it !!!!')

i = 1
x = 3
sum = 0
while ( i <= x ):
 sum += i
 i += 1
print(sum)

i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2

i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1

x = 0
while (x < 50):
  x+=2

print(x)

x = 1
while ( x <= 5 ):
  x += 1
print(x)

i = 1
while True:
    if i % 0o7 == 0:
        break
    print(i)
    i += 1

    x = 1
while ( x < 20 ):
 x = x * 2
print(x)

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1