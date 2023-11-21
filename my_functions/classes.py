import my_functions.data_storage
from my_functions.classificators import *
from my_functions.interface import delete_data_question
from typing import Optional
from pydantic import BaseModel

# class Item(BaseModel):
#     __item_name: str
#     item_class: str
#     item_type: str
#     size: str
#     season: str
#     color: str
#     brand: str
#     price: float
#     description: Optional[str]

class Item:
    def __init__(self, item_name: str, item_class: str, item_type: str, size: str, season: str,
                 color: str, brand: str, price: float = 0.0, description: str = ''):

        self.__item_name = item_name
        self.item_class = item_class
        self.item_type = item_type
        self.size = size
        self.season = season
        self.color = color
        self.brand = brand
        self.price = float(price)
        self.description = description

    def __str__(self):
        return self.__item_name

    def fullstr(self, delimiter="; "):
        return str(self.__item_name) + delimiter + str(self.item_class) + delimiter + str(self.item_type) + delimiter \
            + str(self.size) + delimiter + str(self.season) + delimiter + str(self.color) + delimiter + \
            str(self.brand) + delimiter + str(self.price) + delimiter + str(self.description)

    def name(self):
         return self.__item_name

    def item_dictionary(self):
        article_dict = {}
        for key in self.__dict__:
            if key == "_Item__item_name":
                article_dict['item_name'] = self.__dict__[key]
            else:
                article_dict[key] = self.__dict__[key]
        return article_dict

    @classmethod
    def input_name(cls):
        while True:
            name = input('Name = ').strip()
            if name == '':
                print('Name cannot be empty')
            else:
                return name

    @classmethod
    def input_new_item(cls, name):
        item_class = input_from_classificator(item_classes, 'item_class')
        item_type = input_from_classificator(item_types.get(item_class), 'item type')
        size = cls.input_size(item_class, 'size')
        season = input_from_classificator(seasons, 'season')
        color = input_from_classificator(colors, "color")
        brand = cls.input_brand(item_class, "brand")
        price = cls.input_price("price")
        description = input('description = ').strip()

        new_item = Item(name, item_class, item_type, size, season, color, brand, price, description)
        return new_item

    def change_article(self, my_wardrobe):
        print(f'article = {self.fullstr()}')
        # attributes = list(self.__dict__.keys())
        attributes = list(self.item_dictionary().keys())
        attribute = input_from_classificator(attributes, 'attribute')
        # print(f'old {attribute} = {self.__getattribute__(attribute)}')
        print(f'old {attribute} = {self.item_dictionary()[attribute]}')
        if attribute == "name":
            name = Item.input_name()
            article = my_wardrobe.find_item(name, True)
            if article is None:
                self.__item_name = name
        elif attribute == "item_class":
            item_class = input_from_classificator(item_classes, 'new item_class')
            if item_class != self.item_class:
                self.item_class = item_class
                self.item_type = input_from_classificator(item_types.get(item_class), 'new item type')
                self.size = self.input_size(item_class, 'new size')
                self.brand = self.input_brand(item_class, 'new brand')
        elif attribute == "item_type":
            self.item_type = input_from_classificator(item_types.get(self.item_class), 'new item type')
        elif attribute == "size":
            self.size = self.input_size(self.item_class, 'new size')
        elif attribute == "season":
            self.season = input_from_classificator(seasons, 'new season')
        elif attribute == "color":
            self.color = input_from_classificator(colors, "new color")
        elif attribute == "brand":
            self.brand = self.input_brand(self.item_class, "new brand")
        elif attribute == "price":
            self.price = self.input_price("new price")
        else:
            new_value = input(f'new {attribute} = ').strip()
            self.__setattr__(attribute, new_value)

        action = input("Change other attribute? Yes - 1, No - any other key: ")
        if action == '1':
            self.change_article(my_wardrobe)

    @classmethod
    def input_size(cls, item_class, attribute_name: str):
        if item_class in ["closes", "shoes"]:
            return input_from_classificator(sizes.get(item_class), attribute_name)
        else:
            size = input(f'{attribute_name} = ').strip()
            # if size == "":
            #     size = None
            return size

    @classmethod
    def input_brand(cls, item_class, attribute_name: str):
        if item_class in ["closes", "shoes"]:
            brand = input_from_classificator(brands.get(item_class), attribute_name)
            if not brand == "input other":
                return brand
        brand = input(f'{attribute_name} = ').strip()
        return brand

    @classmethod
    def input_price(cls, attribute_name: str):
        while True:
            price = input(f'{attribute_name} = ').strip()
            try:
                price = float(price)
                return price
            except ValueError:
                print("Incorrect price! Value must be float.")


class Wardrobe:
    def __init__(self, list_items: [Item]):
        self.__list_items = list_items

    def __str__(self):
        wardrobe_string = "My wardrobe:"
        index = 0
        for element in self.__list_items:
            index += 1
            wardrobe_string += "\n" + str(index) + ' ' + element.fullstr()
        return wardrobe_string

    def list_items(self):
        return self.__list_items

    def add_new_item(self):
        name = Item.input_name()
        new_article = self.find_item(name, True)
        if new_article is None:
            new_article = Item.input_new_item(name)
            # if save_data_question():  # interface
            self.__list_items.append(new_article)
            my_functions.data_storage.write_data(self)
        print(self)

    def find_item(self, name, new_item=False):
        for article in self.__list_items:
            if article.name() == name:
                if new_item:
                    print(f'Article with name "{name}" already exist.')
                return article
        if not new_item:
            print(f'Article with name "{name}" not found')
        return None

    def choose_item(self):
        print("Choose action!")
        action = input('1 - Find article by name, 2 - Choose article from list: ')
        if action == "1":
            name = Item.input_name()
            return self.find_item(name)
        elif action == '2':
            return input_from_classificator(self.__list_items, 'article')
        else:
            print("Incorrect input")
            return None

    def change_item(self):
        element = self.choose_item()
        if element is not None:
            element.change_article(self)
            my_functions.data_storage.write_data(self)

    def delete_item(self):
        element = self.choose_item()
        if element is not None:
            print(element.fullstr())
            # answer = input("Do you really want to delete element? Yes - 1, No - any other key: ")
            # if answer == "1":
            # if save_data_question():  # interface
            if delete_data_question():
                self.__list_items.remove(element)
                my_functions.data_storage.write_data(self)
            print(self)
