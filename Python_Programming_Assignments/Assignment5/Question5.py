#Baisc Calculator

a=int(input('Enter first number '))
b=int(input('enter second number '))

while b==0:
    b = int(input('enter second number again'))


choice=int(input('Enter 1 for addition, 2 for substraction, 3 for multiplication, 4 for division '))

sum=a+b
sub=a-b
mult=a*b
div=a/b

if choice==1:
    print('We are doing addition ')
    print('Addtion of given numbers is ', sum)
elif choice==2:
    print('We are doing substraction ')
    print('Subtraction of given numbers is ',sub)
elif choice==3:
    print('We are doing multiplication')
    print('Multiplication of given numbers is ',mult)
else:
    print('We are doing division')
    print('Division of given numbers is ',div)