
filename = input("Please provide the path to your file: ")
"""This is the path to a test file: /Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/text.txt"""


with open(filename, "r") as file:
    data = file.read()
print("Number of characters in the text file: ", len(data))

with open(filename,"r") as file:
     data = file.read()
     words = data.split()
print("Number of words in the text file: ", len(words))

with open(filename,'r') as lines_doc:
  data = lines_doc.readlines()

print("Number of lines in the text file: ", len(data))

with open(filename,'r') as unique_words:
    wordcount = {}
    for word in unique_words.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    print("Number of unique words in the text file: ", len(word))

