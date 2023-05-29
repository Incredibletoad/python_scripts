'''
Adam Altice
SDEV 300
Week 1 - Lab 1
Voter Registration Prompt
'''
import string
import sys

print('Welcome to the 2023  U.S voter registration system..\n\n'
      'Sucessful completion of the follow form means you are eligible'
       'to vote in the upcoming election\n\n')
#Age check while block
while True:
    try:
        age = int(input('Please enter your age:\t'))
    #Unless there is an exception
    except ValueError:
        print("Incorrect value input, please try again")
    else:
        if age < 18:
            print('Unfortunately, you aren\'t old enough to vote in the election.'
                  'See you next time!')
            sys.exit()
        if age >= 18 and age < 120:
            print(f"Thank you for providing your age of {age}... You are old enough to continue.")
            break
citizenCheck = input('Are you a U.S citizen with an issued Social Security Number'
                     '... please type \"Y\" for yes and \"N\" for no')
citizenCheck = citizenCheck.upper()
#If a Citizen, go into a block with detail questions
if citizenCheck == 'Y':
    print(f" Excellent. As a U.S citizen of age {age}, we can proceed..\n\n")
    #Input for user State. .upper so match states list
    citizen_state = input("What is your state of residence?"
                          "Please provide the abbreviation letters. "
                          "For example, Virginia = VA ").upper()
    states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    #If they enter an allowable state of residence
    if citizen_state in states:
        while True:
            citizen_info = {
            "First Name": string,
            "Last Name": string,
            "Addres": string, 
            "Zipcode": int 
        }
            #Prompt for information
            citizen_firstn = input("What is your first name?\n").capitalize()
            citizen_lastn = input("What is your last name?\n").capitalize()
            citizen_address = input("Please provide your street address\n")
            citizen_zip = int(input("What is your zipcode\n"))
            citizen_confirmation = input(f"Please confirm the following information"
                                         " is correct with \'Y\',"
                                          f"Full Name: {citizen_firstn} {citizen_lastn} Age: {age} "
                                          f"State of Residence: {citizen_state} "
                                           f"Address: {citizen_address} Zip: {citizen_zip}").upper()
            #if user enters Y, update KVPs in dictionary citizen info
            if citizen_confirmation == 'Y':
                citizen_info["Addres"] = citizen_address
                citizen_info['First Name'] = citizen_firstn
                citizen_info['Last Name'] = citizen_lastn
                citizen_info['citizen_zip'] = citizen_zip
                #Aggregate data and post to user
                print(f"Thank you for registering to vote. Your voter registration "
                      "card will arrive in the mail with the follow information\n "
                      f"First Name: {citizen_firstn} Last Name: {citizen_lastn}  Age: {age} "
                      f"State of Residence: {citizen_state} Address: {citizen_address} "
                      f"Zip: {citizen_zip}")
                break
            else:
                #If confirmed is no, will continue to top of loop and ask for information
                continue
    else:
        print("Sorry you must be a resident of the 50 states or D.C to vote in this election.")
        sys.exit()
#If not a citizen, they can't vote.
else: print("Sorry, only U.S citizens may vote in this election.")
