#Sum of natural numbers:

num=int(input('Enter number of term '))

while num==1:
    num = int(input('Enter number greater than 1 '))

nsum=num*(num+1)/2


print('Sum of natural numbers is ',nsum)