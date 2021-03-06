# generating a quantity of dictionaries from 2 to 10 as well as number of elements (keys and values)
# in future generated dictionaries
import random
import string
from collections import Counter
from random import randint, choice
dicts_number = randint(2,10)
elements_number = randint(1,10)

# print('dicts number =', dicts_number, 'elements number =', elements_number)

# creating a list of empty dictionaries
list_of_dicts = []

# using the Dictionaries generator method of Python, filling a dictionary with pairs key:value, where
# letters are taken from the string above, their quantity might be in a range of 'elements_number', while keys
# are in a range form 0 to 100
for i in range(dicts_number):
    dictionary = {choice(string.ascii_lowercase): randint(0, 100) for i in range(elements_number)}
    list_of_dicts.append(dictionary)
print('list of dictionaries:', list_of_dicts)

# now we are creating a list of all keys (including duplicates) - firstly as a list
list_of_keys = []
for number in range(dicts_number):
    list_of_keys.append(list(list_of_dicts[number].keys()))

# transforming a list of all keys into a string
all_keys = ''
for i in list_of_keys:
    all_keys += '' + ''.join(i)

# the type 'string' will allow us to count how many times each and every key is met in all the dictionaries;
key_quantity = Counter(all_keys)
# print('key_quantity', dict(key_quantity))

# Now we are creating a list of duplicate keys:
duplicate_keys = []
for key in key_quantity.keys():
    if key_quantity[key] > 1:
        duplicate_keys.append(key)
# print(duplicate_keys)

# now we are creating a final dictionary (empty for this moment)
final_dictionary = {}

# we are creating a list of distinct keys with maximum value for each of them:
for index, d in enumerate(list_of_dicts):  # in all dictionaries from our big list
    for key in d.keys():  # for all keys in a list of distinct keys (with their quantity counted)
        if key not in duplicate_keys: # if a key is NOT in duplicate list, we are inserting it
            final_dictionary[key] = d[key]  # to our final dictionary as it is in our big list
        else:
            if key not in final_dictionary.keys():  # on this stage we are checking duplicate key: if a key is not
                final_dictionary[key] = d[key]  # already in a final list - we insert it with its value.
            else:
                if final_dictionary[key] < d[key]:   # If it's already in the final list, we compare its old and
                    final_dictionary[key] = d[key]  # new values and leave the biggest
                    if final_dictionary[key] == d[key]: # if keys match -
                        del final_dictionary[key] # we delete old key
                        final_dictionary[key + '_' + str(index + 1)] = d[key] # and combine a necessary key-name

print('final dictionary:', final_dictionary)