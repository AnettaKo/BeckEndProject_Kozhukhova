from pymongo import MongoClient
from classes import Item

client = MongoClient("mongodb+srv://ankozhukhova:mongo4anna.@cluster0.yt7xy1p.mongodb.net/?retryWrites=true&w=majority")

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)

class Wardrobe_database:

    client = client
    database = client.my_wardrobe
    collection = database.wardrobe

    def insert_article(self, article: Item):
        return self.collection.insert_one(**article.item_dictionary())

    def get_article_by_name(self, name: str):
        article = self.collection.find_one({"item-name": name})
        return Item(**article)

    def get_all_articles(self):
        articles = self.collection.find({})
        list_articles = []
        for article in articles:
            list_articles.append(Item(**article))
        return list_articles

    def delete_article_by_name(self, name: str):
        return self.collection.delete_one({"item-name": name})

    def update_article_by_name(self, name: str, article: Item):
        return self.collection.replace_one({"item-name": name}, article.item_dictionary())
