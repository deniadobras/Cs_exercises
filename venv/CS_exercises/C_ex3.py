import csv
import json

users = []
ids = []

with open('/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/passwrd2.csv') as password_file:
    password_csv = csv.DictReader(password_file, delimiter=':')
    for row in password_csv:
        users.append(row['username'])
        ids.append(row['id'])
dictionary = dict(zip(users, ids))

result = '\n'.join("{!s}\t{!s}".format(k,v) for (k,v) in dictionary.items())

print("This is the result: " ,result)
with open('/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/CS_exercises/helloworld.txt', 'w') as f:
    f.write(result)
