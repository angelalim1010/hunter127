#miguel helped me
s = "aabbbccccdde"
def rle(s):
    encoded = []
    while len(s)>1:
        runlen = 1
        runchar = s[0]
        while runlen < len(s) and s[runlen] == runchar:
            runlen = runlen + 1
            #run len will end at the next letter
        if runlen>1:
            encoded.append(runlen)
            # only adds number but next line will return character
        encoded.append(runchar)
        s=s[runlen:]
    return encoded

enc = rle(s)
print(enc)

def rle_decode(l):
    s = ""
    counter = 0
    for i in range(len(l)):
        if (i%2 == 0):
            counter = l[i]
        if (i%2 != 0):
            s += l[i] * counter
    return s

print(rle_decode(enc))
    
    