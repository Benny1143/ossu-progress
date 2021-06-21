# Chapter 6 Exercise
# Exercise 1
fruit = "banana"
index = len(fruit)
while index > 0:
    print(fruit[index-1])
    index -= 1

# Exercise 2
print(fruit[:])

# Exercise 3
def letter_counter(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count = count + 1
    return count


print(letter_counter(fruit, 'a'))

# Exercise 4
print(fruit.count("a"))

# Exercise 5
str = 'X-DSPAM-Confidence:0.8475'
print(float(str[str.find(":")+1:]))

# Exercise 6
print(fruit.replace("b", " ").strip())
