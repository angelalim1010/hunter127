def freq(n,l):
    count = 0
    for i in l:
        if i == n:
            count += 1
    return count

def min(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

def mode(l):
    v =[]
    for i in l:
        v.append(freq(i, l))  
    mode = v[i]
    for i in v:
        if mode < v[i]:
            mode = l[i]
    return mode

numbers = [3,2,2,1,3,4,5,4,3,4,3]

print (str(freq(2,numbers)))
print (str(min(numbers)))
print(str(mode(numbers)))