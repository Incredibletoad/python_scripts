'''
Adam Altice
SDEV 300
Week 2 - Lab 2
Functions
'''
#modules
import string
import random
from datetime import date

def passwordGenerator():
    while True:
        passwordLength = int(input('Welcome to the Python PAssword Generator!\n'
                'please input the length of the password you desire, 4-20 characters\t'))
        if passwordLength > 20:
            print('Try Again')
            continue
        elif passwordLength < 4:
            print('Try Again')
            continue
        else:
            pass
        complex = input('Would you like to use a complex password? These will contain '
                'uppercase letters and special symbols, in addition to '
                'numbers and lowercase letters. Y or N?\t').upper()
        if complex == "Y":
        #use string module for each component of complex password
            Upper = string.ascii_uppercase
            Lower = string.ascii_lowercase
            Numbers = string.digits
            Symbols = string.punctuation

            charPool = Upper+Lower+Numbers+Symbols

            randomPassword = random.sample(charPool, passwordLength)
            randomPassword = ''.join(randomPassword)

            print(f" Your randomly generated complex password is : {randomPassword}")
            break

        else:
            Lower = string.ascii_lowercase
            Numbers = string.digits

            charPool = Lower + Numbers

            randomPassword = random.sample(charPool, passwordLength)
            randomPassword = ''.join(randomPassword)

            print(f" Your randomly generated simple password is : {randomPassword}")
            break

def percentageGenerator(numerator,denominator):
    percent_of = float(numerator/denominator) * 100
    #Round off for final
    percent_rounded = str(round(percent_of,2))
    print(f'{numerator} is {percent_rounded}% of {denominator}')

def get_values():
    while True:
        try:
            numerator = int(input('Provide the first number'))
            denominator = int(input('provide the second number'))
        except:
            print('Enter valid number')
        else:
            break
    percentageGenerator(numerator,denominator)

def dayCalculator(year, month, day):
    #create timedelta object (days , time)
    baseline_day = date(year,month,day)
    target_day = date(2025, 7,4)
    #calulate days
    final_day = target_day - baseline_day
    #final_day.days returns the timedelta object 'days' value
    print(f'There are {final_day.days} days between the day provided and July 4th, 2025')

def get_day():
    while True:
        try:
            user_year = int(input('Provide the year'))
            user_month = int(input('provide the month, example: 06 for June'))
            user_day = int(input('provide the date'))
        except:
            print('Enter valid number')
        else:
            break
    print(dayCalculator(user_year,user_month,user_day))


menu_input = 1
if menu_input == 1:
    get_values()