text = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

import re

# dividing a string to several parts in order to keep initial whitespaces (by dots, exclamations and question marks
# with whitespaces, tabs and new lines)
split_text = re.split(r'([.!?]\s*|\t\n)', text)
# print(split_text)

# creating a normalized text (from the case point of view)
normalized_text = ''
for i in split_text:
    normalized_text = normalized_text + i.capitalize()
print('''This is the text, normalized from the case point of view:
''', normalized_text)

# creating a list of last words of all the sentences taking a word before dot
last_words = re.findall(r'\w+(?=[.])', normalized_text)
# print(last_words)

# creating a sentence made of the last words
sentence_normal = ' '.join(last_words).capitalize()
# print(sentence_normal)

# defining a location for the new sentence
new_sentence_location = 'add it to the end of this paragraph'

# splitting normalized text to the parts to be able to find indexes later
text = re.split(r'([.])', normalized_text)
# print(text)

# adding the new sentence after the place defined (using index)
for index, i in enumerate(text):
    if new_sentence_location in i:
        text[index] = i + '. ' + sentence_normal
full_text = ''.join(text)
print('''This is the text with the new sentence added:
''', full_text)

# replacing unnecessary 'iz'
full_tex_corrected = (full_text.replace(' iz ', ' is '))
print('''This is the text without unnecessary "iz":
''', full_tex_corrected)

# counting whitespaces, using a regular expression
white_spaces = len(re.findall(r'\s', full_tex_corrected))
print('Whitespaces are:', white_spaces)