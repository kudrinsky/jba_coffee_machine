alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
string = input()

for char in string:
    if char not in alphabet:
        break
    print('vowel' if char in vowels else 'consonant')