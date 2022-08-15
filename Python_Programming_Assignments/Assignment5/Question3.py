#Decimal to binary octal and hexadecimal

num=int(input('Enter decimal number '))

bin=num
l1=[]

while(bin):
    rem=bin%2
    l1.append(rem)
    bin=bin//2

l1.reverse()
print('Binary conversion of {}'.format(num),'is ')
for item in l1:
    print(item,end='')

oct=num
l2=[]
while(oct):
    rem=oct%8
    l2.append(rem)
    oct=oct//8

l2.reverse()
print('\n','Octal conversion of {}'.format(num),'is ')
for item in l2:
    print(item,end='')


conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

hexadecimal = ''
hex=num
while (hex > 0):
    rem = hex % 16
    hexadecimal = conversion_table[rem] + hexadecimal
    hex = hex // 16

print('\n',"Hexadecimal conversion of {} ".format(num),'is ', hexadecimal)


