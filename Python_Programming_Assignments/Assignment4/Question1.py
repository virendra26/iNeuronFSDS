#Factorial of a number

num=int(input('Enter any positive number '))

mult=1

for i in range(1,num+1):
    mult=mult*i


print('Factorial of {}'.format(num),'is ',mult)