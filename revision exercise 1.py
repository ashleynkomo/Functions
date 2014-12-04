#Ashley Nkomo
#revision exercise 1
#04-12-14


def input_character():
    character = input("Please enter a character: ")
    return character


def input_number():
    number = int(input("Please enter the number of times to dublicate a character: "))
    return number
                      

def output_symbols(number,character):
    print( number * character)

def coolrunnings():
    character = input_character()
    number = input_number()
    output_symbols(number,character)


#main program

coolrunnings()
