from datetime import date, datetime, timedelta
from simple_colors import *

class Publication:
    def __init__(self):
        self.text = input("Please, enter your publication text: \n").capitalize()
        self.date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.line = ''

    def filling_document(self):
        f = open('5_Classes.OOP.txt', 'a')
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

def publication():
    publication_type = input('''Please, chose a Publication type:\n1 - for a news\n2 - for an ads\n3 - for a healthy breakfast: \n''')
    if publication_type == '1':
        News().filling_document()
    elif publication_type == '2':
        Ads().filling_document()
    elif publication_type == '3':
        Healthy_breakfast().filling_document()
    else:
        print("Sorry! We don't have this type of Publication. Try again: ")
        publication()

publication()