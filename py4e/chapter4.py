# Chapter 4 Exercise
# Exercise 6
def computepay(hours, rate):
    return (hours if hours <= 40 else (hours - 40)*1.5 + 40)*rate


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print(f"Pay: {computepay(hours, rate)}")

# Exercise 7
def computegrade(score):
    if score < 0 or score > 1:
        raise
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter score: "))
    print(computegrade(score))
except:
    print("Bad score")
