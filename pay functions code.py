#Ashley Nkomo
#Calculate Pay
#18/11/14

def input_hours_and_pay():
    work_hours = int(input("Please enter your hours worked: "))
    work_pay = float(input("Please enter your Pay Rate: "))
    return work_hours, work_pay

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

def calculatepay():
    hours,pay = input_hours_and_pay()
    totalPay = calculate_total_pay(hours,pay)
    display_total_pay(totalPay)

    
def display_total_pay(total):
    print("Your total pay £{0}".format(total))



#main program
calculatepay()
