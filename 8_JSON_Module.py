import json
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
            self.which_document = input('If you want to use your document, please, enter 1. \nIf you want to use a default file, please, enter 2. \n')
            if self.which_document == '1':
                self.document_name = input("Please, enter your document name (including '.txt' or '.json'- \n(example: document.txt or document.json)): \n")
                try:
                    file = open(self.document_name)
                    if self.document_name.endswith('.json'):
                        try:
                            json.load(file)
                        except json.decoder.JSONDecodeError:
                            print('Wrong file completion! A JSON file must include type, name, text, etc. enclosed in double quotes')
                            quit()
                    file.close()
                except (FileNotFoundError):
                    print("Wrong file name!")
                    quit()
            elif self.which_document == '2':
                self.document_name = 'lyuba.txt'
            else:
                print('Wrong choice! Try again.')
        else:
            print('Wrong choice! Try again.')

    def source_document(self):
        if self.document_name.endswith('.txt'):
            self.source_file_open = open(self.document_name, 'r').read()
            self.text = re.split('\\n\\n', self.source_file_open)
            return self.text
        elif self.document_name.endswith('.json'):
            self.source_file_open = open(self.document_name)
            self.text = json.load(self.source_file_open)
            return self.text

    def final_document(self):
        self.publications_number = int(input('Please, define how many publications you want to use: \n'))
        with open('Final.txt', 'w') as f:
            if self.document_name.endswith('.txt'):
                try:
                    if self.publications_number < len(self.text) and self.publications_number > 0:
                            for i in self.text:
                                if self.text.index(i) < self.publications_number:
                                    f.write(i + '\n\n')
                    elif self.publications_number >= len(self.text):
                        for i in self.text:
                            f.write(i + '\n\n')
                        os.remove(self.document_name)
                except ValueError:
                    print('Wrong symbol! Not a digit!')
            elif self.document_name.endswith('.json'):
                try:
                    if self.publications_number < len(self.text):
                        if self.publications_number > 0:
                            for i in self.text:
                                if self.text.index(i) < self.publications_number:
                                    for ind, dict_ in enumerate(self.text):
                                        if 'type' in dict_ and dict_['type'] == 'news':
                                            f.write(f"""News -----------------\n{str(dict_["name"]).capitalize()}\n{str(dict_["text"]).capitalize()}\n{str(dict_["city"]).capitalize()}\n{datetime.now()}\n\n""")
                                        elif 'type' in dict_ and dict_['type'] == 'ads':
                                            f.write(f"""Ads ----------------- \n{str(dict_["name"]).capitalize()}\n{str(dict_['text']).capitalize()}\nExpiration date is: {str(date.today() + timedelta(days=30))}\n\n""")
                                        elif 'type' in dict_ and dict_['type'] == 'Healthy breakfast':
                                            f.write(f"""Healthy breakfast ---------------- \n{str(dict_["name"]).capitalize()}\n{str(dict_['ingredients']).capitalize()}\n{str(dict_['text']).capitalize()}\n{datetime.now()}\n\n""")
                    elif self.publications_number >= len(self.text):
                        for i in self.text:
                            for ind, dict_ in enumerate(self.text):
                                if 'type' in dict_ and dict_['type'] == 'news':
                                    f.write(f"News -----------------\n{str(dict_['name']).capitalize()}\n{str(dict_['text']).capitalize()}\n{str(dict_['city']).capitalize()}\n{datetime.now()}\n\n")
                                elif 'type' in dict_ and dict_['type'] == 'ads':
                                    f.write(f"Ads ----------------- \n{str(dict_['name']).capitalize()}\n{str(dict_['text']).capitalize()}\nExpiration date is: {str(date.today() + timedelta(days=30))}\n\n")
                                elif 'type' in dict_ and dict_['type'] == 'Healthy breakfast':
                                    f.write(f"Healthy breakfast ---------------- \n{str(dict_['name']).capitalize()}\n{str(dict_['ingredients']).capitalize()}\n{str(dict_['text']).capitalize()}\n{datetime.now()}\n\n")

                        #os.remove(self.document_name)
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

    letters_frequency = {}
    file = open('Final.txt', 'r')
    data_upper = file.read().replace(' ', '')
    data = data_upper.lower()
    for i in data:
        if i.isalpha():
            count = letters_frequency.get(i, 0)
            letters_frequency[i] = count + 1

    frequency_list = letters_frequency.keys()

    upper_frequency = {}
    for l in data_upper:
        if l.isupper():
            count_upper = upper_frequency.get(l, 0)
            upper_frequency[l] = count_upper + 1

    up = []
    upper_list = upper_frequency.keys()
    for i in upper_list:
        up.append(i.lower())

    total_letters = len([i for i in data if i.isalpha()])

    headerList = ['letter', 'total', 'upper', 'percentage']

    with open('percent.csv', 'w') as csvfile_2:
        dw = csv.DictWriter(csvfile_2, delimiter=' ', fieldnames=headerList)
        dw.writeheader()

        for s in frequency_list:
            if s not in up:
                csvfile_2.write(s + '   ' + str(letters_frequency[s]) + '   ' + 'none' + '   ' + str(
                    round(letters_frequency[s] * 100 / total_letters, 2)) + '\n')
            else:
                for t in upper_list:
                    if s == t.lower():
                        csvfile_2.write(
                            s + '   ' + str(letters_frequency[s]) + '   ' + str(upper_frequency[t]) + '      ' + str(
                                round(letters_frequency[s] * 100 / total_letters, 2)) + '\n')

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
        if source_type.which_document == '1':
            if source_type.document_name.endswith('.txt'):
                source_type.source_document()
                source_type.final_document()
            elif source_type.document_name.endswith('.json'):
                source_type.source_document()
                source_type.final_document()
           #     source_type.final_document_json()
            else:
                'Wrong document type!'
        elif self.which_document == '2':
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
csv_write()