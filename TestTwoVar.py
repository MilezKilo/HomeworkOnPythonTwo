from math import *

#Exercise 1
def areaCalculation():
    print('Enter length and width:')
    length, width = int(input()), int(input())
    temporary = length * width
    SQFT_PER_ACRE = temporary / 43560
    print("Result =", SQFT_PER_ACRE, "acres")

#Exercise 2
def freeFall(accseleration=9.8):
    distance = int(input('Enter distance: '))
    Vf = sqrt(2 * (accseleration * distance))
    print('The velocity of an object in contact with the ground: ', Vf)

#Exercise 3
def howManyDays():
    month = input('Enter a month: ')
    if month.capitalize() == 'February':
        print('There is 28, or 29 days in', month)
    elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
        print('There is 30 days in', month)
    else:
        print('There is 31 days in', month)


areaCalculation()
print('---------------------')
freeFall()
print('---------------------')
howManyDays()