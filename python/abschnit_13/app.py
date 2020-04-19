import json
import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches


def getDiscription(text):

    text = text.lower()
    textTitle = text.title()
    textUpper = text.upper()

    with open('data.json') as file:

        data = json.load(file)
        matches = get_close_matches(text, data.keys(), n=3, cutoff=0.6)

        if matches == []:
            print('No matches found')
        else:
            if text in data:
                return "".join(data[text])
                #print(t)
            elif textTitle in data:
                t = "".join(data[textTitle])
                print(t)
            elif textUpper in data:
                t = "".join(data[textUpper])
                print(t)
            else:
                print('Did you mean: ')
                for count, item in enumerate(matches):
                    print(count, "-", item, end="\n")
                number = int(input("choose one number: "))

                print("".join(data[matches[number]]))


end = True

userInput = input("Enter a word: ")

getDiscription(userInput)
