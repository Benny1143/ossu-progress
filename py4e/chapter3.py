# Chapter 3 Exercise
# Exercise 1
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
    hours = (hours - 40)*1.5 + 40
print(f"Pay: {str(hours*rate)}")

# Exercise 2
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours > 40:
        hours = (hours - 40)*1.5 + 40
    print(f"Pay: {str(hours*rate)}")
except:
    print('Error, please enter numeric input')

# Exercise 3
try:
    score = float(input("Enter score: "))
    if score < 0 or score > 1:
        raise
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except:
    print("Bad score")
