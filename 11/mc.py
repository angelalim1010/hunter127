import random
def remove_non_alpha(w):
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result


def build_word_chain(wordlist):
    d={}
    for i in range(len(wordlist)):
        w1 = wordlist[i-2]
        w2=wordlist[i-1]
        d.setdefault((w1,w2),[])
        d[(w1,w2)].append(wordlist[i])
    return d

def bwcff(f):
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    
    return build_word_chain(l)

def generate_text(d,start_word,length=50):
    wordlist2 = []
    next = start_word
    for i in range(length):
        if next not in d:
            break
        wordlist2.append(next)
        next = random.choice(d[next])
    return "".join(wordlist2)

hamlet = bwcff("hamlet.txt")
psalms = bwcff("psalms.txt")
sonnets = bwcff("sonnets.txt")


    
for i in range(len(hamlet) -1):
    print(str(list(hamlet.keys())[i]) + ': ' + str(list(hamlet.values())[i]))

