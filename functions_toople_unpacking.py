#make a list of tuples

stock_prices = [('appl', 200)]

#basic tuple unpacking
for ticker, price in stock_prices:
    print(ticker)
    print(price)
    
#functions can return tuples to unpack

work_hours_completed = [('bob', 50), ('jan', 60)]

#check who has the most hours
def employee_check(work_hours):

    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    return (employee_of_the_month,current_max)
    #returning a tuple
    
item = employee_check(work_hours_completed)

print(item)
