#Ashley Nkomo
#Functions Spot check
#09/12/14

def input_password():
    password = input("Please Enter your Password : ")
    return password

def password_size(password):
    password_length = len(password)
    return  password_length

def password_checker(password_length):
    if "8" <= password_length <= "16":
        print("Password Accepted")
    

def running():
    password = input_password
    password_size(password)
    password_checker(password_length)

#main program

running()
