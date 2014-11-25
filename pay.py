#Ashley Nkomo
#13/11/2014
#Pay calculation

basic_hours = int(input("Please enter the basic hours you worked: "))
overtime_hours = int(input("Please enter any overtime hours that you worked: "))
overtime_payrate = int(input("Please enter the overtime pay rate: "))
pay_rate = float(input("Please enter you normal pay rate: "))

basic_pay = basic_hours * pay_rate
overtime_pay = overtime_payrate * overtime_hours
total_pay = basic_pay + overtime_pay

print("The total pay you have made is £{0}".format(total_pay))
