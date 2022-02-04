import nltk

words = [w for w in nltk.corpus.words.words('en') if len(w) == 5 and w.islower()]
words = set(words)

done = False
goal = [-1, -1, -1, -1, -1]
ans = [' ', ' ', ' ', ' ', ' ']
atleastone = False
confirmed = []
confirmed_not = []

def printWord(lst):
    for i in range(len(lst)):
        if(lst[i]) != ' ':
            print(lst[i], end=" ")
        else:
            print("_", end=" ")
    print("\n")

def cleanup_recs(dic):
    for el in dic:
        for i in range(len(goal)):
            if goal[i] == 2:
                if el[i] != ans[i]:
                    dic[el] = 0
    for el in dic:
        if dic[el] < len(confirmed):
            dic[el] = 0
    return dic

def getRecommendations(letters):
    recs = {}
    for w in words:
        for i in range(len(letters)):
            if letters[i] in w:
                try: 
                    recs[w] += 1
                except KeyError: 
                    recs[w] = 1
    return cleanup_recs(recs)

def printRecs(recs):
    message = False
    for el in recs:
        if recs[el] > 0:
            if message == False:
                print("For your next guess, I recommend:")
                message = True
            print("%s" % (el), end=" ")
    if not message:
        i = 0
        for x in words:
            print("%s" % (x), end=" ")
            i += 1
            if (i == 10):
                break
    print('\n')

def checkDone(word):
    for c in word:
        if c == ' ':
            return False
    return True

def cleanup_wordlist(anti):
    non = []
    for el in words:
        for i in range(len(anti)):
            if anti[i] in el:
                non.append(el)
    for i in range(len(non)):
        try:
            words.remove(non[i])
        except:
            continue
        
def printKnown(lst):
    if not lst:
        print("No confirmed letters right now :(")
        return
    print("We know that the word also has:")
    for el in lst:
        print("%s" % (el), end = " ")



while not done:
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
            atleastone = True
            ans[i] = guess[i]
            confirmed.append(ans[i])
        if goal[i] == 1:
            if (guess[i] not in confirmed):
                confirmed.append(guess[i])
                print(confirmed)
        if goal[i] == 0:
            if ((guess[i] not in confirmed_not) and (guess[i] not in confirmed)):
                confirmed_not.append(guess[i])
                print(confirmed_not)
    if checkDone(ans):
        print("Congrats! You're all done")
        break
    cleanup_wordlist(confirmed_not)
    print("Alright, here's where we're at:")
    printWord(ans)
    for c in confirmed:
        if c not in ans:
            print(c, end = " ")
    print("\n")
    printRecs(getRecommendations(confirmed))

    