# Chapter 12 Exercise
import urllib.error
import urllib.parse
import re
import ssl
from bs4 import BeautifulSoup
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Exercise 3
fhand = urllib.request.urlopen(
    'http://py4e-data.dr-chuck.net/regex_sum_1281870.txt')
count = 0
total = 0
for line in fhand:
    p = line.decode().strip()
    total += len(p)
    if count == 3000:
        continue
    count += len(p)
    if count > 3000:
        print(p[0:count-3000])
        print("...")
        count = 3000
        continue
    print(p)
print(f"Length: {total}")

# Autograder
url = "http://py4e-data.dr-chuck.net/comments_1281872.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print(sum([int(span.contents[0]) for span in soup('span')]))


# Autograder 2
url = "http://py4e-data.dr-chuck.net/known_by_Waqaas.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


def get_name(a):
    return re.findall("known_by_(.*).html", a)


names = get_name(url)
count = input("Enter count:")
position = input("Enter position:")

for a in range(int(count)):
    url = soup('a')[int(position)-1].get('href', None)
    names += get_name(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

print(" ".join(names))
print(f"Last Name: {get_name(url)[0]}")
