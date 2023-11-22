import csv
import json
import os

from my_functions.classes import *

def is_json_file(file_name):
   file_extention = os.path.splitext(file_name)[1].lower()
   if file_extention == '.json':
       return True
   return False

def read_file(file_name):
    if is_json_file(file_name):
       return read_json_file(file_name)
    else:
        return read_csv_file(file_name)

def write_file(file_name, my_wardrobe):
    if is_json_file(file_name):
        write_json_file(file_name, my_wardrobe)
    else:
        write_csv_file(file_name, my_wardrobe)

def file_existing(file_name):
   if not os.path.exists(file_name):
       file = open(file_name, "w")
       file.write("")
       file.close()

def read_csv_file(file_name):
    file_existing(file_name)
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        list_items = [Item(**row) for row in reader]

        my_wardrobe = Wardrobe(list_items)
        print(my_wardrobe)
        return my_wardrobe

def read_json_file(file_name):
    file = open(file_name, "r")
    file_contents = file.read()
    list_items = []
    if len(file_contents) == 0:
        return Wardrobe(list_items)
    raw_json_data = json.loads(file_contents)
    for id in raw_json_data:
        article = Item(**raw_json_data[id])
        list_items.append(article)
    my_wardrobe = Wardrobe(list_items)
    print(my_wardrobe)
    return my_wardrobe

def write_csv_file(file_name, my_wardrobe):
    with open(file_name, 'w') as csvfile:
        list_items = my_wardrobe.list_items()
        writer = csv.DictWriter(csvfile, fieldnames=list_items[0].__dict__.keys(), delimiter=';', lineterminator='\n')
        # writer = csv.DictWriter(csvfile, fieldnames=list_items[0].item_dictionary().keys(), delimiter=';', lineterminator='\n')
        writer.writeheader()
        writer.writerows([item.__dict__ for item in list_items])
        # writer.writerows([item.item_dictionary() for item in list_items])
        print(f'file {file_name} is updated')

def write_json_file(file_name, my_wardrobe):
    file = open(file_name,"w")
    list_items = my_wardrobe.list_items()
    if len(list_items) == 0:
        file.write("")
        return
    list_articles = {}
    for article in list_items:
        list_articles[article.name()] = article.__dict__
        # list_articles[article.name()] = article.item_dictionary()
    file.write(json.dumps(list_articles))
    file.close()
