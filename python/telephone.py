def get_letters(num):
    match num:
        case '2': return "abc"
        case '3': return "def"
        case '4': return "ghi"
        case '5': return "jkl"
        case '6': return "mno"
        case '7': return "pqrs"
        case '8': return "tuv"
        case '9': return "wxyz"
        case _: return None
# Thank you python 3.10 for match statments *heart eyes*

def pretty_print(digits, words):
    print(digits, end="")
    print(":", end=" ")
    for i in range(len(words)):
        print("%s" % words[i], end=" ")
    print()

import re
import nltk
try:
    print("\n\nWelcome! This program will find all of the words associated with your phone number")
    print("according to the keypad letters (Think about way back when texting was with only\nthe digits).\n")
    num = input("Please enter your phone number as xxx-xxx-xxxx: ")

    if not re.search(r"^[0-9]+[0-9]+[0-9]+", num):
        print("Follow the instructions.")
        exit()
    strs = []
    strs.append(num[:3])
    strs.append(num[4:7])
    strs.append(num[8:12])

    wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

    print("your number is (%s) %s-%s" % (strs[0], strs[1], strs[2]))
    for i in range(3):
        curstr = strs[i]
        searchstring = ""
        for i in range(len(curstr)):
            s = get_letters(curstr[i])
            try:
                searchstring += "[" + s + "]"
            except TypeError:
                continue

        sstring = "^" + searchstring + "$"
        case = [w for w in wordlist if re.search(sstring, w)]
        pretty_print(curstr, case)

except KeyboardInterrupt:
    print("\n\nThanks for playing.\n")