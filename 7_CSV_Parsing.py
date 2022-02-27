import re
import os, sys
import string
import csv
from datetime import date, datetime, timedelta
from Functions import normal_text

class First_choice:
    def __init__(self): # we are getting the information about the source of a future publication: a file or manual input
        self.choice = input("If you want to insert a news manually - please, type 1.\nIf you want to insert a news from the document - please, type 2.\nMake your choice: \n")
        if self.choice == '1':
            self.publication_type = input('''Please, choose a Publication type:\n1 - for a news\n2 - for an ads\n3 - for a healthy breakfast: \n''')
        elif self.choice == '2':
            self.document_path = sys.path[1] # the folder where our Python project is stored
            # self.which_document = input('If you want to use your document, please, enter 1. \nIf you want to use a default file, please, enter 2. \n')
            self.document_name = input('Please, provide your document name: \n')
            # if self.which_document == 1:
            #     self.document_name = input('Please, enter your document name: \n')
            # elif self.which_document == 2:
            #     self.document_name = 'final.txt'
            try:
                file = open(self.document_name)
                file.close()
            except FileNotFoundError:
                print("Wrong file name!")
                quit()
        else:
            print('Wrong choice! Try again.')

    def source_document(self): # we are creating a full path to the document in a default folder and splitting it by double newlines
        self.source_file = os.path.join(self.document_path, self.document_name)
        self.source_file_open = open(self.source_file, 'r').read()
        self.text = re.split('\\n\\n', self.source_file_open)
        return self.text

    def final_document(self, doc_name = 'Final.txt'): # we are inserting information from the file provided to our new file
        try:
            self.publications_number = int(input('Please, define how many publications you want to use: \n'))
            f = open('Final.txt', 'a')
            if self.publications_number > 0:
                for i in self.text:
                    if self.text.index(i) < self.publications_number:
                        f.write(i + '\n\n')
            f.close()
         #   os.remove(self.source_file)
        except ValueError:
            print('Wrong symbol! Not a digit!')

class Publication:
    def __init__(self): # here we are using our normalization from the HW#4
        self.text = normal_text(input(f"Please, enter your publication text: \n"))
        self.date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.line = ''

    def filling_document(self, doc_name = 'Final.txt'):
        f = open(doc_name, 'a')
        f.write(self.line)
        f.close()

class News(Publication):
    def __init__(self):
        super().__init__()
        self.name = input("Please, enter your news Title: \n").upper()
        self.place = input("Please, enter your news Place: \n").capitalize()
        self.line = f"""News -----------------\n{self.name}\n{self.text}\n{self.place}\n{str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))}\n\n"""

class Ads(Publication):
    def __init__(self):
        super().__init__()
        self.name = input("Please, enter your ads Title: \n").upper()
        self.date = f"Expiration date is: {str(date.today() + timedelta(days=30))}\n"
        self.line = f"""Ads -----------------\n{self.name}\n{self.text}\n{self.date}\n\n"""

class Healthy_breakfast(Publication):
    def __init__(self):
        super().__init__()
        self.name = input("Please, enter your breakfast name: \n").upper()
        self.ingredients = f"""Healthy ingredients: {input("Please, enter all necessary ingredients (only healthy ones!): ").capitalize()}"""
        cooking_recommendations = f"Cooking recommendations: {self.text}\n"
        self.line = f"""Healthy breakfast -----------------\n{self.name}\n{self.ingredients}\n{cooking_recommendations}{self.date}\n\n"""

def csv_write():
    with open('Final.txt', 'r') as file:
        data_upper = file.read()
        data = data_upper.lower()
    frequency = {}
    pattern = re.findall(r'\b[a-z]{2,15}\b', data)

    for i in pattern:
        count = frequency.get(i, 0)
        frequency[i] = count + 1

    frequency_list = frequency.keys()

    with open('frequency.csv', 'w') as csvfile:
        for t in frequency_list:
            csvfile.write(t + ': ' + str(frequency[t]) + '\n')

    with open('percent.csv', 'w') as csvfile_2:
        csvfile_2.write('Total letters amount is: ' + str(len([i for i in data if i.isalpha()])) + '\n')
        csvfile_2.write('Total upper letters amount is: ' + str(len([i for i in data_upper if i.isupper()])) + '\n')
        csvfile_2.write('The % of upper letters in the quantity of all symbols is: ' + str(round(
            len([i for i in data_upper if i.isupper()]) * 100 / (len(data_upper) - data_upper.count(' ')))) + '\n')

def publication():
    source_type = First_choice()
    if source_type.choice == '1':
        if source_type.publication_type == '1':
            News().filling_document()
        elif source_type.publication_type == '2':
            Ads().filling_document()
        elif source_type.publication_type == '3':
            Healthy_breakfast().filling_document()
        else:
            print("Sorry! We don't have this type of Publication. Try again: ")
            publication()
    elif source_type.choice == '2':
        source_type.source_document()
        source_type.final_document()
    else:
        print("Sorry. We have no other publication input type")
        publication()
    last_choice = input("If you want to end the program, enter 1.\nIf you want to continue, enter 2.\n")
    if last_choice == '1':
        csv_write()
    elif last_choice == '2':
        publication()

publication()