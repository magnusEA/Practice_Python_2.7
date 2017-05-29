#Pig latin program in python
#User inputs a word and it returns the pig latin version
#i.e. the first letter of the word is moved to the end and 'ay' is concatenated to that

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'