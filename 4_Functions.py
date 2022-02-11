import re, random, string
from collections import Counter
from random import randint, choice

#################################
### 2_COLLECTIONS ###
#################################

# generating a quantity of dictionaries from 2 to 10 as well as number of elements (keys and values)
def list_of_dictionaries():
    global dicts_number, elements_number, list_of_dicts # marking those variables as global as we will need them later
    dicts_number = randint(2, 10)
    elements_number = randint(1, 10)
    list_of_dicts = []
    for i in range(dicts_number):
        dictionary = {choice(string.ascii_lowercase): randint(0, 100) for i in range(elements_number)}
        list_of_dicts.append(dictionary)
    return list_of_dicts


def new_dictionary(list_of_dictionaries = list_of_dictionaries()):
    # creating a list of duplicate keys
    list_of_keys = []
    for number in range(dicts_number):
        list_of_keys.append(list(list_of_dicts[number].keys()))
    all_keys = ''
    for i in list_of_keys:
        all_keys += '' + ''.join(i)
    key_quantity = Counter(all_keys)
    duplicate_keys = []
    for key in key_quantity.keys():
        if key_quantity[key] > 1:
            duplicate_keys.append(key)
    print(duplicate_keys)
# choosing necessary keys (from MAX value point of view)
    final_dictionary = {}
    for d in list_of_dicts:
        for key in d.keys():
            if key not in duplicate_keys:
                final_dictionary[key] = d[key]
            else:
                if key not in final_dictionary.keys():
                    final_dictionary[key] = d[key]
                else:
                    if final_dictionary[key] < d[key]:
                        final_dictionary[key] = d[key]
# adding indexes were necessary
    for index, d in enumerate(list_of_dicts):
        for key in d.keys():
            if key in duplicate_keys:
                if key in final_dictionary.keys():
                    if final_dictionary[key] == d[key]:
                        del final_dictionary[key]
                        final_dictionary[key + '_' + str(index + 1)] = d[key]
    return final_dictionary

# print(list_of_dictionaries())
# print(new_dictionary())

#################################
### 3_STRING_OBJECT ###
#################################

# normalizing the original text from the case point of view
def normal_text(text):
    split_text = re.split(r'(\.\s*|\t\n)', text)
    normalized_text = ''
    for i in split_text:
        normalized_text = normalized_text + i.capitalize()
    return normalized_text

# creating a new sentence from the last words of each sentence and adding it to the determined paragraph
def additional_sentence(text, hardcode_text = 'add it to the end of this paragraph'):
    normalized_text = normal_text(text)
    last_words = re.findall(r'\w+(?=[.])', normalized_text)
    sentence_normal = ' '.join(last_words).capitalize()
    text = re.split(r'([.])', normalized_text)
    for index, i in enumerate(text):
        if hardcode_text in i:
            text[index] = i + '. ' + sentence_normal
    full_text = ''.join(text)
    return full_text

# replacing unnecessary 'iz'
def full_text_corrected(text):
    full_text = additional_sentence(text)
    new_full_text = full_text.replace(' iz ', ' is ').replace(' Iz ', ' is ') # capitalized Iz (as the first word in
    return new_full_text                                            # a possible sentence) is taken into account

# counting whitespaces, using a regular expression
def white_spaces(text):
    ready_for_count = full_text_corrected(text)
    white_spaces_number = len(re.findall(r'\s', ready_for_count))
    return white_spaces_number

original_text = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# print(normal_text(original_text))
# print(additional_sentence(original_text))
# print(full_text_corrected(original_text))
# print(white_spaces(original_text))