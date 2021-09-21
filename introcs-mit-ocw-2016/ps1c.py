annual_salary = int(input("Enter your annual salary: "))
total_cost = 1000000
within = 100
semi_annual_raise = .07
months = 36

portion_down_payment = .25
r = 0.04

down_payment = total_cost * portion_down_payment
num_of_months = 0

low = 0
high = 10000
steps = 0

while True:
    steps += 1
    current_savings = 0
    portion_saved = (high + low)/2/10000
    
    monthly_salary = annual_salary / 12 * portion_saved

    for month in range(months):
        if month != 0 and month % 6 == 0:
            monthly_salary *= 1 + semi_annual_raise
        current_savings += current_savings*r/12 + monthly_salary
    
    diff = int((high - low)/2)
    if current_savings <= down_payment - within:
        if portion_saved == 0.5:
            print("It is not possible to pay the down payment in three years.")
            break
        low += diff
    elif current_savings >= down_payment + within:
        high -= diff
    else:
        print("Best savings rate:", portion_saved)
        print("Steps in bisection search:", steps)
        break