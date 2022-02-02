# generating a quantity of dictionaries from 2 to 10 as well as number of elements (keys and values)
# in future generated dictionaries
import random
from random import randint
dicts_number = randint(2,10)
elements_number = randint(1,10)

# print('dicts number =', dicts_number, 'elements number =', elements_number)

# creating a list of empty dictionaries
list_of_dicts = []

# importing a String module for further using of the alphabet (string.ascii_lowercase) to get the necessary
# letters for keys
import string

# using the Dictionaries generator method of Python, filling a dictionary with pairs key:value, where
# letters are taken from the string above, their quantity might be in a range of 'elements_number', while keys
# are in a range form 0 to 100
for i in range(dicts_number):
    dictionary = {a: b for a in [random.choice(string.ascii_lowercase) for p in range(elements_number)]
                  for b in {randint(0,100)}}
    list_of_dicts.append(dictionary)
print('list of dictionaries:', list_of_dicts)

# now we are creating a list of all keys - firstly as a list
list_of_keys = []
for letter in range(dicts_number):
    list_of_keys.append(list(list_of_dicts[letter].keys()))

# transforming a list of all keys (including duplicates) into a string
all_keys = ''
for i in list_of_keys:
    all_keys += '' + ''.join(i)

# the type 'string' will allow us to count how many times each and every key is met in all the dictionaries;
# we are import Counter module to count the quantity of each element
from collections import Counter
key_quantity = Counter(all_keys)
print('keys quantity is:', dict(key_quantity))
