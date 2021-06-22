# Chapter 8 Exercise
# Exercise 1
def chop(t):
    del t[0]
    del t[len(t)-1]


def middle(t):
    return t[1:len(t)-1]


items = ["a", "b", "c", "d", "e", "f"]
chop(items)
print(items)
print(middle(items))

# Exercise 2 & 3
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    print(words[2])

# Exercise 4
fhand = open("romeo.txt")
unique = []
for line in fhand:
    words = line.split()
    for word in words:
        if word not in unique:
            unique.append(word)

unique.sort()
print(unique)

# Exercise 5
fhand = open(input("Enter a file name: "))
count = 0
for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        print(email)
        count += 1
print("There were %d lines in the file with From as the first word" % count)

# Exercise 6
numbers = []
while True:
    i = input("Enter a number: ")
    if i == "done":
        break
    numbers.append(float(i))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
