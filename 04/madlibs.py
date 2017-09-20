#Shariar Kabir and Angela Lim

import random

s = "NAME VERB my cat. NAME VERB towards the NOUN. NAME VERB towards the NOUN."

nouns = ["chicken", "pizza", "fries"]
verbs = ["run", "jump" , "punch"]
names = ["Juan", "Tom", "Bob"]

def madlib(s):
    s = s.split(" ")
    i = 0
    name =""
    punc = ['.',',','!','?']
    for words in s:
        punc_hold = ''
        if (words[-1] in punc):
            punc_hold = punc[punc.index(words[-1])]
            words = words[0:-1]
        if (words == "NOUN"):
            s[i] = random.choice(nouns) + punc_hold
        elif (words == "VERB"):
            s[i] = random.choice(verbs) + punc_hold
        elif (words == "NAME"):
            if name != "":
                s[i] = name
            else:
                name = random.choice(names)
                s[i] = name
        i+=1
    ret_string=""
    for words in s:
        ret_string += words + ' '
    return ret_string

print(madlib(s))