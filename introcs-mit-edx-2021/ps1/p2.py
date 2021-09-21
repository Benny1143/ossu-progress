# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

# Give
s = 'azcbobobegghakl'

bob = 0
index = 0
for letter in s:
    if letter == 'b':
        if s[index:index+3] == 'bob':
            bob += 1
    index += 1
print('Number of times bob occurs is:', bob)