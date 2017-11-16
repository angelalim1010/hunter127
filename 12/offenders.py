import csv

def csv_d(file):
    f = open(file)
    csv_dict_reader = csv.DictReader(f)
    l = []
    
    count = 0
    for line in csv_dict_reader:
        l.append(line)
        count += 1

    f.close()
    return l

def iindex(dict, l):
    d = {}
    for wordlist in dict:
        for word in l:
            if word in wordlist['Last Statement']:
                d.setdefault(word, [])
                d[word].append(wordlist['TDCJ Number'])
    return d

        
sad_word = ['sorry', 'apologize', 'forgiveness', 'god', 'love']
angry_word = ['hate', 'hell', 'damn'] 

wordlist = csv_d('offenders.csv')

for k, v in iindex(wordlist, sad_word).items():
    print(k + ' : ' + str(v))


