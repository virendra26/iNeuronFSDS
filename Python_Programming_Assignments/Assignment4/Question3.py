#Fibbonaci Sequence

a=0
b=1

num=int(input('Enter number of terms in fibonacci sequence '))

for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c