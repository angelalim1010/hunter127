import sys #given in problem
def ladybug(n, bug):
    bugs = [i for i in bug if i ==n]
    return (len(bugs))
def move(bug):
    happy = True
    list = []
    for i in range(0, len(bug)):
        if bug[i] not in list:
            list.append(bug[i])
        else:
            list.remove(bug[i])
    if (len(list) == 0 and ladybug(bug[i], bug) != len(bug)):
        return False
    for d in list:
        if d != '_' and ladybug(d, bug) == 1:
            happy = False
    return happy

#given in problem
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    if move(b):
        print ("YES")
    else:
        print ("NO")
