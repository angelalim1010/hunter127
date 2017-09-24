spam = ["apples", "bananas", "tofu", "cats"]

def commacode(l):
    s1 = l[:-1]
    s2 = l[-1]
    s3 = " , " .join(s1) + ', and ' + s2
    return s3

print (commacode(spam))

        