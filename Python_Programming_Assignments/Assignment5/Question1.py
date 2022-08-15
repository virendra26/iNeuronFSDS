#LCM of two numbers

a=int(input('Input first number '))
b=int(input('Enter second number '))

if a>b:
    num=a
else:
    num=b

while(True):
    if num%a==0 and num%b==0:
        lcm=num
        break
    num=num+1

print('LCM of given numbers is ',lcm)
        