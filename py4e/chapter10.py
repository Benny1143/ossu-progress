# Chapter 10 Exercise
# Exercise 1
import string
fhand = open("mbox-short.txt")
dic = dict()
for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        dic[email] = dic.get(email, 0) + 1
i = []
for email, value in list(dic.items()):
    i.append((value, email))
i.sort(reverse=True)
value, email = i[0]
print(email, value)

# Exercise 2
fhand = open("mbox-short.txt")
dic = dict()
for line in fhand:
    if line.startswith("From "):
        hour = line.split()[5].split(":")[0]
        dic[hour] = dic.get(hour, 0) + 1
i = list(dic.items())
i.sort()
for hour, count in i:
    print(hour, count)

# Exercise 3
fhand = open("mbox-short.txt")
s = fhand.read()
dic = dict()
for c in s:
    if c.isalpha():
        ch = c.lower()
        dic[ch] = dic.get(ch, 0) + 1
li = list(dic.items())
li.sort()
print(li)
