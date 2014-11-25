#Ashley Nkomo
#Calculate Pay
#18/11/14

def hours_and_pay(hours,pay):
    work_hours = int(input("Please enter your hours worked: "))
    work_pay = float(input("Please enter your Pay Rate: "))
    return total

def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total

def calculate_overtime_pay(hours,pay):
    total = ((hours - 40) * (pay * 1.5) + (pay * 40))
    return total

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def display_result(total):
    print("Your total pay {0}".format(calculate_total_pay))



#main program





