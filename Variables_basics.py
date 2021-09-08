## pythn variables (like buckets to store values)
##   variables names are case sensitive and must begin with a letter or "_" ;
##   can not have the same name of a pre-define python name, unless you change the casing 
##
amount_of_apples = 2
cost_of_apple = 5
print(amount_of_apples*cost_of_apple)

mount_of_apples = 5
cost_of_apple = cost_of_apple + 2  ## all other operators can be used out of Add
print(amount_of_apples*cost_of_apple)

mount_of_apples = 5
cost_of_apple += 2   ## another way to incremet a variable value
print(amount_of_apples*cost_of_apple)

## More samples
#
age = 22
AGE = 44
age /= 2
print(age + AGE)

amount = 4
cost = 2
cost += 2
print(amount * cost)

y = 5
y = "Jack"
print(y)