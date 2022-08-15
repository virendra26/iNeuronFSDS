#Even odd
num=int(input('input any number '))

if num<=0:
    print('Please enter a positive number')
    num=int(input('Enter new number '))

if num%2==0:
    print('Given number is even')
else:
    print('Given number is odd')