#leap year

year=int(input('Enter the year '))

if year%400==0 and year%100==0:
    print('Given year is leap year ')
elif year%100!=0 and year%4==0:
    print('Given year is leap year')
else:
    print('Given year is not leap year')


