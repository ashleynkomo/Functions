#Ashley Nkomo
#Task 1 - Part 2
#02-12-14

def reg_information():
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    housenumber = input("Please enter your house number or house name: ")
    streetname = input("Please enter your street name: ")
    town = input("Please enter the town you live in: ")
    postcode = input("Please enter your postcode: ")
    gender = input("Please enter your gender: ")
    return firstname, lastname, gender

def getTitle(gender):
    if gender == "Male" or "male" or "m":
        title = "Mr"
    elif gender == "Female" or "female" or "f":
        title = "Ms"
    return title

def custommessage(title, firstname, lastname):
    print("Hello {0} {1} {2}, thank you for registering to the National Bank of Uganda.".format(title, firstname, lastname))

def coolrunnings():
    firstname, lastname, gender = reg_information()
    title = getTitle(gender)
    custommessage(title, firstname, lastname)
        
    
#main program

coolrunnings()
