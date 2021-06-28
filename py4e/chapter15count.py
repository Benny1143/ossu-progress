# Autograder: Counting Email in a Database
import sqlite3

conn = sqlite3.connect('count.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

# fname = input('Enter file name: ')
fname = ""
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)
orgs = dict()
for line in fh:
    if not line.startswith('From: '):
        continue
    org = line.split()[1].split("@")[1]
    orgs[org] = orgs.get(org, 0) + 1
for i in list(orgs. items()):
    cur.execute('''INSERT INTO Counts (org, count) VALUES (?, ?)''', i)
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts WHERE count = (SELECT MAX(count) FROM Counts)'
for row in cur.execute(sqlstr):
     print(str(row[0]), row[1])

cur.close()
