#miguel helped me 
import csv
f = open("sample-texts.csv")

csv_reader = csv.reader(f)
l = []
for line in csv_reader:
    l.append(line)
f.close()
print(l)
'''
if: [one,two,three,four]
you: [one,two,three,four]
prick: [one]
do: [one,two, three]
tickle: [two]
poison: [three]
'''
def ii(l):
    d = {}
    for i in l:
        for j in range(len(i)/2):
            for k in i[1].split():
                d[k] = []
    for i in l:
        for j in range(len(i)/2):
            for k in i[1].split():
                d[k].append(i[0]) 
    return(d)

print(ii(l))
            