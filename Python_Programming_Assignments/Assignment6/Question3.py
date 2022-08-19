#BMI in python

h=float(input('Enter height in meters '))
w=float(input('Enter weight in kgs '))

BMI=round(w/(h**2),3)

print('Your BMI is ',BMI)