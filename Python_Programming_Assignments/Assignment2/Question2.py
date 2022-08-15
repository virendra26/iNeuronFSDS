#Celcius to Fahrenheit

def celtofaren(temp):

    faren= 1.8*temp+32

    return faren


temp=int(input('Enter temperature in celsius '))

print('Temperature in fahrenheit is ',celtofaren(temp))