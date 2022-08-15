#Prime number:

num=int(input('Enter a positive number '))
indication=False

if num>1:
    for i in range(2,num):
        if num%i==0:
            indication=True
            break
else:
    num = int(input('Enter a positive number greater than 1 '))

if indication:
    print(num, 'is not a prime number')
else:
    print(num, 'is a prime number')