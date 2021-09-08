##
##  we can execute code for each item in sequence with a for ... in loop
#

for i in range(5):
    print('i is: ', i)

for i in range(2,5):        # starting the range on 2
    print('i is: ', i) 

for i in range(5):          # breaking the loop based in a certain condition
    if(i==2):
        break
    print('i is: ', i) 

for i in range(5):          # skip the loop to the next cycle based in a condition
    if(i==2):
        continue
    print('i is: ', i) 