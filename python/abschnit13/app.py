import json
import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches


def getDiscription(text):

    text = text.lower()

    with open('data.json') as file:

        data = json.load(file)
        matches = get_close_matches(text, data.keys(), n=3, cutoff=0.6)

        if matches == []:
            print('No matches found')
        else:
            if text in data:
                print(data[text])
            else:
                print('Did you mean: ')
                for count, item in enumerate(matches):
                    print(count, item)
                number = int(input("coose one number: "))

                print(data[matches[number]])


end = True

userInput = input("Enter a word: ")

getDiscription(userInput)
