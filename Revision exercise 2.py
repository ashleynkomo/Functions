#Ashley Nkomo
#04-12-14
#Inverted Pyramid


def check_digit():
    number = 2
    while number % 2 == 0:
        number = int(input("Please enter an odd number: ")) 
    return number

def inverted_pyramid(number):
    n = number
    while number >=1:
        number_sign = "*" * number
        print("{0:^{1}}".format(number_sign, n))
        number = number - 2
    return number

def coolrunnings():
    number = check_digit()
    inverted_pyramid(number)


#main program
coolrunnings()
