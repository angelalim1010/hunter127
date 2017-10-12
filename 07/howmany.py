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
    f =[]
    for i in l:
        f.append(freq(i, l))  
    mode = f[i]
    for i in f:
        if mode < f[i]:
            mode = l[i]
    return mode

numbers = [3,2,2,1,3,4,5,4,3,4,3]

print (str(freq(2,numbers)))
print (str(min(numbers)))
print(str(mode(numbers)))