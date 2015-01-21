#as computing/python/functions/functions2 starter
#31-10-12

def GetHoursAndRate():
    Hours = -1
    Rate = -1
    while Hours < 0 or Hours <= 60:
        Hours = int(input('Please enter the number of hours worked (max. 60 hours): '))
    while Rate < 0:
        Rate = float(input('Please enter your hourly rate of pay: '))
    return Hours, Rate

def CalculateBasicPay(Hours, Rate):
    BasicPay = 0
    if Hours >= 40:
        Hours = 40
        BasicPay = Hours * Rate
    return BasicPay

def CalculateOvertimePay(Hours, Rate):
    OvertimePay = 0
    if Hours > 40:
        Hours = Hours % 40
        OvertimePay = Hours * Rate * 1.5
    return OvertimePay

def calculate_total_pay(Hours, Rate):
    if Hours <= 40:
        total = CalculateBasicPay(Hours, Rate)
    else:
        total = CalculateOvertimePay(Hours, Rate)
    return total

def calculatepay():
    Hours,Rate = GetHoursAndRate()
    totalPay = calculate_total_pay(Hours, Rate)
    #DisplayTotalPay(TotalPay)

def DisplayTotalPay(TotalPay):
    TotalPay = round(TotalPay,2)
    print('Your pay this week is: £{0}'.format(TotalPay))    

# main program
BasicPay = 0
OvertimePay = 0
calculatepay()
