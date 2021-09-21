# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
# then your program should print:

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print:

# Longest substring in alphabetical order is: abc

# Given
s = 'azcbobobegghakl'

word = ''
index = 0
while index < len(s):
    ix = index + 1
    tempword = s[index]

    while ix < len(s) and s[ix] >= s[ix-1]:
        tempword += s[ix]
        ix += 1
    
    index += len(tempword)
    
    if len(tempword) > len(word):
        word = tempword

print('Longest substring in alphabetical order is:', word)