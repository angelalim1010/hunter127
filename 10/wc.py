def remove_non_alpha(w):
    '''
input: w - string representing a "word"
output: the stirng with non alpha chars removed
'''
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def bwcd(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d

def bwcff(f):
    '''
input: f - string representing a filename
returns: a dictitonary with keys for words and values
of the number of times each word occurs 
    '''
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = bwcd(l)
    return d


d = bwcff("hamlet.txt")

v= d.values()
v= list(d.values())
v.sort ()
for k in d:
    if d[k] > 10:
        print (k, ":", d[k])
        
d2 = bwcff("sonnets.txt")
v2 = list(d2.values())
v2.sort
for l in d2:
    if d2[l] > 150:
        print (l, ":", d2[l])
#stemming turns words into the same word. ex: plural or possessive
# ex making -> make, makes -> make
'''
l = []
for a in b:
    if _:
        l.append(_)
#or
l = []
for k in d:
    if _:
        l.append(_)
        '''
l = [x for x in range(10)]

[k for k in d2 if d2[k] >200]
# gives d if it appears more than 100x
