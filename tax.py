import time
def final_tax_liability():
    print('Welcome! I am here to calculate your 2022 final tax liability in US Dollars.')
    time.sleep(2)
    while True:
        try:
            q3 = int(input('First off, please enter your pre-tax income in dollars without any commas.'))
        except ValueError:
            print('Please enter a valid amount.')
            continue
        else:
            break
    q1 = input('Next, we would like to know if you are married or single? Type "y" for yes, or "n" for no.\n ' )
    while q1 != "y" and q1 != "n":
        q1 = input('please enter "y" for yes, and "n" for no.\n')
    if q1 == "y":
        print('Great! Your standard deduction this year will be $25,900.\n')
    elif q1 == "n":
        print('Sounds good. Your standard deduction this year will be $12,950.\n')
    q2 = input('Did you make any IRA contributions this year? . y or n.\n')
    while q2 != "y" and q2 != "n":
        q2 = input('please enter "y" for yes, and "n" for no.\n') 
    while True:
        try:
            if q2 == "y":
                ira = int(input('Please enter the amount in dollars without any commas.\n'))
        except ValueError:
            continue
        else:
            break
    if q2 == "n":
        print('Ok, now we can move onto your taxable income.')
        time.sleep(2)
    if q2 == "y" and q1 == "y":
        deductions = ira + 25900
        print('Your total deductions this year will be: ')
        print(deductions)
    elif q2 == "y" and q1 == "n":
        deductions = ira + 12950
        print('Your total deductions this year will be: ')
        print(deductions)
    elif q2 == "n" and q1 == "n":
        deductions = 12950
        print('Your total deductions remain unchanged.') 
        print(deductions)
    elif q2 == "n" and q1 == "y":
        deductions = 25900
        print('Your total deductions this year will be: ')
        print(deductions)
    time.sleep(2)
    if  q3 - deductions <= 10275:
        final = abs(q3 - deductions)
        print('Your total refund for this year is: $', final)
    elif q3 - deductions > 10275 and q3 - deductions <= 41775:
        final = float(1027.50 + (.12*((q3-deductions)-10275)))
        print('Your total tax liability for this year is: $', final)
    elif q3 - deductions > 41775 and q3 - deductions <= 89075:
        final = float(4807.50 + (.22*((q3-deductions)-41775)))
        print('Your total tax liability is: $', final)
    else:
        print('You make too much money!')


   


    

final_tax_liability()