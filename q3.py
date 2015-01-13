def values():
    distance = float(input("Please enter the length of the journey: "))
    mpg = float(input("Please enter the miles per gallon of your vehicle: "))
    fuel_price = float(input("Please enter the current price for fuel: "))
    return distance, mpg, fuel_price

def Calculations(distance, mpg, fuel_price):
    fuel_needed = mpg * distance
    actual_price = fuel_price * fuel_needed
    return actual_price

def display(actual_price):
    print("The fuel cost of this journey is £{0}".format(actual_price))

def engine():
    user_input = values()
    answers = Calculations(distance, mpg, fuel_price)
    display(actual_price)

#main program

engine()
