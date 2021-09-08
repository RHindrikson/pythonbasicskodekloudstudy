##
##  we have 6 comparison operators in python (all returns TRUE or FALSE)
#       1)  ==     EQUAL
#       2)  !=     NOT EQUAL
#       3)  >      GREATER THAN
#       4)  >=     GREATER THAN OR EQUAL TO
#       5)  <      SMALLER THAN   (both value egual, will return True)
#       6)  <=      SMALLER THAN OR EQUAL TO  (both value egual, will return True)


a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)

min_score = 13
score = 13

print(score > min_score)
print(score <= min_score)

x = 6
y = 7
print(x != y)

print(2 < 4)

#y = 20
#x = y += 3
#print(x)