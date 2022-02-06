text = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

import re

# transforming a string to a list, getting rid of unnecessary whitespaces
# and splitting elements by dot with any number of whitespaces after it
ss = re.sub(r'\s+', ' ', text)
rez = re.split(r'\.\s+',ss)

# creating a list of capitalized sentences (without dot)
n = []
for i in rez:
    i = i.capitalize()
    n.append(i.capitalize())

# transforming a list of lines to a list of lists
y = [x.split() for x in n]

# creating a list of last words of all sentences
sentence = []
for i in y:
    sentence.append(i[-1])

# the sentence made of the last words
sentence_normal = ' '.join(sentence).capitalize()

# collecting final text and replacing unnecessary 'iz'
m = '. '.join(n)
s = (m + ' ' + str(sentence_normal)).replace('. ', '.\n').replace(' iz ', ' is ')

print(s)
#
# # counting whitespaces, tabs and new lines in the old text and in the new sentence
white_spaces = text.count(' ') + text.count('\n') + text.count('\t') + sentence_normal.count(' ')
print('Whitespaces are:', white_spaces)