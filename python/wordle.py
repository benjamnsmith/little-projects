from importlib.abc import ResourceLoader
import nltk

words = [w for w in nltk.corpus.words.words('en') if len(w) == 5 and w.islower()]
words = set(words)

done = False
goal = [-1, -1, -1, -1, -1]
ans = [' ', ' ', ' ', ' ', ' ']
confirmed = {}
confirmed_not = []
recs = {}

# FIRST PASS
# Remove words that don't have confirmed letters
# ie. If we know the word has an 'h', remove all words without an 'h'
def pass_one(confirmed):
    global recs
    global num_recs

    for rec in recs:
        for conf in confirmed:
            if conf not in rec:
                recs[rec] = -1

# SECOND PASS
# Remove words that don't have for-certain letters in the right location
# ie. if we know the word has an 'e' in position 2, remove words that don't have an 'e' as the second letter
def pass_two():
    global recs
    global goal
    global num_recs

    for rec in recs:
        for i in range(len(goal)):
            if goal[i] == 2: # IF A LETTER IN THIS SPOT IS CONFIRMED TO BE CORECT LOCATION
                if rec[i] != ans[i]: # if the confirmed location letter is not in the same place in the recommendation
                    recs[rec] = -1
    

# THIRD PASS
# Remove words that have confirmed letters in the wrong location
# ie. if we know there is not an 'h' in position 4, remove all words that have an 'h' there
def pass_three(confirmed):
    global recs

    for rec in recs:
        for letter in confirmed:
            places = len(confirmed[letter])
            for i in range(places):
                curlist = confirmed[letter]
                if rec[curlist[i]] == letter:
                    recs[rec] = -1

# ZERO PASS
# Remove words that have letters we know are not in the word
# ie. if we know the word does not contain a 't', remove all words with 't'
def pass_zero(anti):
    for rec in recs:
        for letter in anti:
            if letter in rec:
                recs[rec] = -1

def getRecommendations(letters):
    global recs
    global confirmed_not

    pass_zero(confirmed_not)
    

    pass_one(letters)


    pass_two()


    pass_three(letters)


def countRecs():
    global recs
    total = 0

    for el in recs:
        if recs[el] == 1:
            total += 1
    return total

def initRecs():
    global recs
    for w in words:
        recs[w] = 1

def printWord(lst):
    for i in range(len(lst)):
        if(lst[i]) != ' ':
            print(lst[i], end=" ")
        else:
            print("_", end=" ")
    print("\n")

def checkDone(word):
    for c in word:
        if c == ' ':
            return False
    return True

        
def printKnown(lst):
    if not lst:
        print("No confirmed letters right now :(")
        return
    print("We know that the word also has:")
    for el in lst:
        print("%s" % (el), end = " ")

def filterRecs():
    global recs

    tmp = recs

    least_common = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm']

    for rec in tmp:
        for letter in least_common:
            if letter in rec:
                tmp[rec] = -1
    return tmp


def printRecs():
    if countRecs() > 20:
        here = filterRecs()
    else:
        global recs
        here = recs
    message = False
    iter = 0
    for r in here:
        if recs[r] > 0:
            if not message:
                print("Here are my recommendations:")
                message = True
            print(r, end = " ")
            iter += 1
            if iter % 9 == 0:
                print()
                iter = 0
    print()

print("\n========= GET LIVE WORDLE RECOMMENDATIONS =========\n")
print("  We will give you live wordle recommendations")
print("  all you have to do is come up with a starting")
print("  word!")

initRecs()
try:
    while not done:
        print("---------------------------------------------------")
        guess = input("Please input your guess: ")
        print("Please tell us how your word performed:")
        print("0 - not present\n1 - present, wrong location\n2 - present, right location\n")
        for i in range(5):
            if (ans[i] == ' '):
                goal[i] = int(input("%c - " % (guess[i])))
            else:
                print("%c - CONFIRMED" % ans[i])
                continue
            if goal[i] == 2:
                ans[i] = guess[i]
            if goal[i] == 1:
                if (guess[i] not in confirmed):
                    confirmed[guess[i]] = [i]
                else:
                    confirmed[guess[i]].append(i)
                print(confirmed)
            if goal[i] == 0:
                if ((guess[i] not in confirmed_not) and (guess[i] not in confirmed)):
                    confirmed_not.append(guess[i])
        if checkDone(ans):
            print("Congrats! You're all done")
            break
        print("---------------------------------------------------")
        print("Alright, here's where we're at:")
        printWord(ans)
        print("Here's the other letters we know are in the word somewhere:")
        for c in confirmed:
            if c not in ans:
                print(c, end = " ")
        print("\n---------------------------------------------------")
        getRecommendations(confirmed)
        printRecs()
except KeyboardInterrupt:
    print("\n\nThanks for playing! Now shutting down...\n")
finally:
    exit(0)