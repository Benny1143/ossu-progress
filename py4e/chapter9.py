# Chapter 9 Exercise
# Exercise 1
fhand = open('words.txt')
dic = dict()
for word in fhand.read().split():
    dic[word] = " "
print("are" in dic)

# Exercise 2
fhand = open("mbox-short.txt")
dic = dict()
for line in fhand:
    if line.startswith("From "):
        day = line.split()[2]
        dic[day] = dic.get(day, 0) + 1
print(dic)

# Exercise 3
fhand = open("mbox-short.txt")
dic = dict()
for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        dic[email] = dic.get(email, 0) + 1
print(dic)

# Exercise 4
fhand = open("mbox-short.txt")
dic = dict()
most = None
e = ""
for email in dic:
    if most is None or most < dic[email]:
        most = dic[email]
        e = email
print(e, most)

# Exercise 5
fhand = open("mbox-short.txt")
domain = dict()
for line in fhand:
    if line.startswith("From "):
        d = line.split()[1].split("@")[1]
        domain[d] = domain.get(d, 0) + 1
print(domain)
