username = []
id = []

with open('/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/passwd',"r") as password_file:
    for x in password_file.readlines():
        username.append(x.split(':')[0])
        id.append(x.split(':')[2])

dictionary = dict(zip(username, id))

for i in sorted(dictionary):
    print ((i, dictionary[i]))