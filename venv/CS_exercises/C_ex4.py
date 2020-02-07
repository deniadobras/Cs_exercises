import json

filename = "/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/scores/9a.json"

with open(filename) as scores_json:
    scores_json = json.load(scores_json)

average_math = sum(d['math'] for d in scores_json) / len(scores_json)
average_lit = sum(d['literature'] for d in scores_json) / len(scores_json)
average_sci = sum(d['science'] for d in scores_json) / len(scores_json)

max_math = max(d['math'] for d in scores_json)
min_math = min(d['math'] for d in scores_json)


max_lit = max(d['literature'] for d in scores_json)
min_lit = min(d['literature'] for d in scores_json)

max_sci = max(d['science'] for d in scores_json)
min_sci = min(d['science'] for d in scores_json)

math_dict = {"math": (min_math, max_math, average_math)}
sci_dict = {"science": (min_sci, max_sci, average_sci)}
lit_dict = {"literature": (min_lit, max_lit, average_lit)}

string = "Math: " + "min " + str(math_dict["math"][0]) + ", max " + str(math_dict["math"][1]) + ", average " + str(math_dict["math"][2]) + "\n" + \
         "Science: " + "min " + str(sci_dict["science"][0]) + ", max " + str(sci_dict["science"][1]) + ", average " + str(sci_dict["science"][2]) + "\n" +\
         "Literature: " + "min " + str(lit_dict["literature"][0]) + ", max " + str(lit_dict["literature"][1]) + ", average "  + str(lit_dict["literature"][2])
print(string)

if filename is "/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/scores/9a.json":
    with open("/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/scores/9a_average.json", "w") as f:
        f.write(string)
elif filename is "/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/scores/9b.json":
    with open("/Users/denia.dobras/PycharmProjects/Cs_exercises/venv/etc/scores/9b_average.json", "w") as f:
        f.write(string)
else:
    print("This is a different file!")