def encode_letter(c,r):
    if 'a' <= c <= 'z':
        no = ord(c) + r
        if no > ord('z'):
            no = no - 26
    else:
        no = ord(c)
    return chr(no)

def encode_string(s,r):
    n = ''
    for i in s:
        if ord(i) >= 97 or ord(i) <= 122 or ord(i) >= 65 or ord(i) <= 90:
            n += encode_letter(i,r)
        else:
            n += i
    return n

def full_encode(s):
    n = ''
    for i in s:
        if ord(i) >= 97 or ord(i) <= 122 or ord(i) >= 65 or ord(i) <= 90:
            for r in range(1,27):
                n = n + encode_string(s,r) + "\n"
    return n

print(full_encode("abcd"))
