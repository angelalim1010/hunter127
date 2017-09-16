def piglatin(word):
    vowel = ('a', 'e', 'i', 'o', 'u')
    first_letter = word[0]
    if first_letter in vowel:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'
print (piglatin("apple"))
print (piglatin("banana"))

