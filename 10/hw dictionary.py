def remove_non_alpha(w):
    result= [l for l in w if l.isalpha()]
    return ''.join(result)


def bwd(wordlist):
    d={}
    word = wordlist[0]
    for w in wordlist:
        if word in d:
            d[word].append(w)
            word = w
        d.setdefault(w,[])
    return d

def bwf(f):
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = bwd(l)
    return d

d = bwf("hamlet.txt")