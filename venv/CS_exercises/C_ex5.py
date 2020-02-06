filepath = "/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/scores/scores/lorem.txt"

with open(filepath,"r+") as file:
    wordcount = {}
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
print(wordcount)

occurrences = [(value, key) for key, value in wordcount.items()]
print("Word with most occurences is: ", max(occurrences)[1], "with" , wordcount['pariatur'], "occurrences")