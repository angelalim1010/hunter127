def encode_letter(c,r):
    if 'a' <= c <= 'z':
        new_ord = ord(c) + r
        if new_ord > ord('z'):
            new_ord = new_ord - 26
    else:
        new_ord = ord(c)
    return chr(new_ord)
            
print (encode_letter('y',3))

    



    
    