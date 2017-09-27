def encode_letter(c,r):
    if 'a' <= c <= 'z':
        new_ord = ord(c) + r
        if new_ord > ord('z'):
            new_ord = new_ord - 26
    else:
        new_ord = ord(c)
    return chr(new_ord)

def encode_string(s,r):
    n = ''
    for i in s:
        if ord(i) >= 97 or ord(i) <= 122 or ord(i) >= 65 or ord(i) <= 90:
            n += encode_letter(i,r)
        else:
            n += i
    return n

print(encode_string("asy",3))
      

