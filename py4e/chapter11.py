# Chapter 11 Exercise
# Exercise 1
import re
fname = "mbox-short.txt"
fhand = open(fname)
i = input("Enter a regular expression:")
count = 0
for line in fhand:
    if re.search(i, line):
        count += 1

print(f"{fname} had {count} lines that matched {i}")

# Exercise 2
fname = "mbox-short.txt"
fhand = open(fname)
total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    num = re.findall("^New Revision: ([0-9]+)", line)
    if len(num) > 0:
        total += int(num[0])
        count += 1
print(int(total/count))

# Autograder
fhand = open("regex_sum_1281870.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    num = re.findall("([0-9]+)", line)
    if len(num) > 0:
        for i in num:
            count += int(i)
print(count)

# Optional: Just for Fun
print(sum([int(i) for i in re.findall(
    "([0-9]+)", open("regex_sum_1281870.txt").read())]))
