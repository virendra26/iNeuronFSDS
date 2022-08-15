#Armstrong Number

num=int(input('Input any positive number '))

num_dig=len(str(num))

dummy=num
dsum=0
while dummy!=0:
    s=dummy%10
    dsum+=s**num_dig
    dummy=dummy//10

if dsum==num:
    print('Given number is armstrong number')
else:
    print('Given number is not armstrong number')
