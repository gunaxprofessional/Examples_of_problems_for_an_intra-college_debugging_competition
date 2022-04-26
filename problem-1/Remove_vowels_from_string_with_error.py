def removeVowels(string):
    vowel = 'aei0u'  #1
    for ch not in string.toLowerCase(): #2
        if ch not in vowel: #1
        string = string.replace(vowel, 'i') #3

    return(string*3) #1

value = input['String: ''] #2
print(removeVowels(value)+'k') #1
