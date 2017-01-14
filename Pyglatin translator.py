#Last word to add
pyg = 'ay'

#Asks the question
original = raw_input('Enter a word:')

#Makes the first letter lowercase
word = original.lower()

#It takes the first letter of word
first = word[0]

#It slices the letters from 1 to x 
new_word = new_word[1:]

#Concatenation of strings
new_word = word + first + pyg

#Condition to print the word, it must be a word, no numbers and more than 0 characters
if len(original) > 0 and original.isalpha():
    print new_word
else:
    print 0
