annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = .25
current_savings = 0
r = 0.04

down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12 * portion_saved
num_of_months = 0

while current_savings < down_payment:
    current_savings += current_savings*r/12 + monthly_salary
    num_of_months += 1

print(f"Number of months: {num_of_months}")