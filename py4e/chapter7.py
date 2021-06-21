# Chapter 7 Exercise
# Exercise 1
fname = input("Enter a file name: ")
# fname = "mbox-short.txt"
fhand = open(fname)
# print(fhand)

# Exercise 2
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        total += float(line[line.find(":")+1:])
print("Average spam confidence:", total/count)

# Exercise 3
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
