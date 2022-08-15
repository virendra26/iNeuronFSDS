#HCF of two numbers

a=int(input('Input first number '))
b=int(input('Enter second number '))

if a>b:
    num=b
else:
    num=a

for i in range(1,num+1):

    if a%i==0 and b%i==0:
        hcf=i


print('HCF of given numbers is ',hcf)