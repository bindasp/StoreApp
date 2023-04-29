from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

# Pobranie hasła z pliku .env
password = os.environ.get("MONGODB_PWD")

# Link do bazy danych
connection_string = f"mongodb+srv://bindaspatryk:{password}@bindasp.39na5lh.mongodb.net/?retryWrites=true&w=majority"
# Połączenie z bazą danych

client = MongoClient(connection_string)

# Pobranie listy baz danych
dbs = client.list_database_names()

# Stworzenie bazy danych
test_db = client.Baza
# Pobranie listy kolekcji

collections = test_db.list_collection_names()

# Dodawanie dokumentu
def insert_test_doc():
    collection = test_db.users
    users = {
        "name":" Patryk",
        "type": "Test"
    }
    inserted_id = collection.insert_one(users).inserted_id
    print(inserted_id)

# Nowa baza danych
production = client.production
#Nowa kolekcja
person_collection = production.person_collection

# Tworzenie dokumentów
def create_documents():
    first_names = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "Allen"]
    last_names = ["Ruscica", "Smith", "Bart", "Cater", "Pit", "Geral"]
    ages = [21, 40, 23, 19, 34, 67]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age }
        docs.append(doc)
    person_collection.insert_many(docs)

################ Kwerendy #################

printer = pprint.PrettyPrinter()

def find_all_people():
    people = person_collection.find()

    for person in people:
        printer.pprint(person)

def find_tim():
    tim = person_collection.find_one({"first_name": "Tim"})
    printer.pprint(tim)

def count_all_people():
    count = person_collection.count_documents(filter = {})
    print ("Number of people: ", count)

def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    printer.pprint(person)

def get_age_range(min_age, max_age):
    query = {"$and": [
            {"age": {"$gte": min_age} },
            {"age": {"$lte": max_age} }
            ]}
    people = person_collection.find(query).sort("age")
    for person in people: 
        printer.pprint(person)

def update_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    all_updates = {
        "$set": {"new_field": True},
        "$inc": {"age": 1},
        "$rename": {"first_name": "first", "last_name": "last"}

    }
    person_collection.update_one({"_id": _id}, all_updates)

update_person_by_id("64495b6d1644b479e6914f20")