# Chapter 5 Exercise
# Exercise 1
total = 0
count = 0

while True:
    try:
        i = input("Enter a number: ")
        if i == "done":
            break
        total += int(i)
        count += 1
    except:
        print("Invalid input")
print(total, count, total/count)

# Exercise 2
maximum = None
minimum = None

while True:
    try:
        i = input("Enter a number: ")
        if i == "done":
            break
        number = int(i)
        if maximum is None or number > maximum:
            maximum = number
        if minimum is None or number < minimum:
            minimum = number
    except:
        print("Invalid input")
print("Maximum:", maximum)
print("Minimum:", minimum)
