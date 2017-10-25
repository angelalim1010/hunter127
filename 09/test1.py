def divide(A,B,u):
    piece = 0
    if u >= 1:
        piece += (A/B)
    return int(u // piece)
    
print (divide(5,10,1))

print (divide(6,12,2))

print (divide(4, 8, 3))

def encode(s):
    count = 1
    prev = s[0]
    list = []
    for letter in s[1:]:
        if letter == prev:
            count += 1
        else:
            if count != 1:
                list.append(count)
            list.append(prev)
            prev = letter
            count = 1
    if count != 1:
        list.append(count)
    list.append(prev)
    return list
 
print (encode('aaabbc'))
print (encode('aaaaaa'))
    

points = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
          'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
          'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

def scrabble(s):
    score = 0
    for letter in s:
        score = score + points[letter] 
    return score 

print (scrabble('hello'))
print (scrabble('zebra'))
    