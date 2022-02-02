# Firstly, we import the Random module of Python to be able to generate random numbers
import random

# Then we generate 100 random numbers from 0 to 1000
random_list = random.sample(range(0, 1000), 100)

# We create empty sorted_list to add there numbers from random_list in a distinct order
sorted_list = []

# We are searching for a minimum number in the random_list (using min() function),
# appending it to the sorted_list ('append' function) and deleting from the random_list
# ('remove' function) at the same time. 'While' loop will allow to carry out this
# operation multiple times
while random_list:
    sorted_list.append(min(random_list))
    random_list.remove(min(random_list))

# Finally we are transforming our sorted_list in 2 lists: a list with even numbers
# (summ_even) and a list with odd numbers (summ_odd) using a condition when a number
# could be (or not) be divided by 2. Additionally we add a condition when a
# denominator equals 0: in this case we add 'pass' not to break the process and
# pass to the next operation.
summ_even = [even for even in sorted_list if even % 2 == 0]
if len(summ_even) == 0:
    print("As the quantity of even numbers in a list is 0, to calculate its average is impossible. Sorry!)")
    pass
else:
    print("Average for even numbers is", round(sum(summ_even) / len(summ_even),1))

summ_odd = [odd for odd in sorted_list if odd % 2 != 0]
if len(summ_odd) == 0:
    print("As the quantity of odd numbers in a list is 0, to calculate its average is impossible. Sorry!)")
    pass
else:
    print("Average for odd numbers is", round(sum(summ_odd) / len(summ_odd),1))