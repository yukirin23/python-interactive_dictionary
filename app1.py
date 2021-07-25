import json
# import library for checking match text
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if No: " %
                   get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. please double check it"


word = input("Enter Word : ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
