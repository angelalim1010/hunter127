

def rotate_char(c,r):

    v = ord(c)
    v = v - 97 # shifts down so that 'a' is 0
    v = (v + r)%26
    v = v + 97 #shifts back up so that 'a' is 97
    result = chr(v)
    return result



def encode_string(s,r):
   
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter = rotate_char(letter,r)
        result = result + letter
    return result


import math

def distance(l1,l2):
   
    length = len(l1)
    if len(l1) > len(l2):
        length = len(l2)
    sum=0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d

def build_frequency_vector(s):
        # count the letterse in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)
    return v
        # count each letter to see how many times it appears
def print_vector_table(v):
    s = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i], " : ", v[i])

def decode(s):
        #build a list of 26 rotations and their frequencies
    rotations = []
    frequencies = []
    distances = []
    for i in range(26):
        rstring = encode_string(s,i)
        freq = build_frequency_vector(rstring)
        rotations.append(rstring)
        frequencies.append(freq)
        d = distance(freq, real_stats)
        distances.append(d)
        #find the smallest value and its index = idiom in coding
    min_index = 0
    min_value = distances[0]
    for i in range(1,len(distances)):
         if distances[i] < min_value:
            min_value = distances[i]
            min_index = i
    return (encode_string(s,min_index))
s= "this is my string"
print ("original:", s)
print('encoded: ', encode_string(s, 13))


f = open('11-0.txt')
r = f.read()
r = r.lower()
real_stats = build_frequency_vector(r)
f.close()

print('decoder(alice): ',decode(s))

f = open('sherlock_holmes.txt')
r = f.read()
r = r.lower()
real_stats = build_frequency_vector(r)
f.close()
print('decoder (sherlock): ', decode(s))