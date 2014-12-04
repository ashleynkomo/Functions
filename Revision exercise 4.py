#04-12-2014
#Ashley Nkomo
#Revision Exercise 4

def celcius_temperature():
    c_temp = int(input("Please enter your temperaturein Fahrenheit: "))
    return c_temp

def conversion(c_temp):
    f_temp = (c_temp - 32) * (5/9)
    return f_temp

def coolrunnings():
    c_temp = celcius_temperature()
    conversion(c_temp)
