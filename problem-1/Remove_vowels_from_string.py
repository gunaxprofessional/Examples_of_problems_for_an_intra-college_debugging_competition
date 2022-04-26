def removeVowels(string):
    vowel = 'aeiou'
    for ch in string.lower():
        if ch in vowel:
            string = string.replace(ch, '')

    return (string)

value = input('String: ')
print(removeVowels(value))
