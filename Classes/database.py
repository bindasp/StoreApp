import mysql.connector 

class Database:
    def __init__(self):
        #Połączenie z bazą danych
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user = "root",
            database = "projekt"
            )    
        #Utworzenie kursora
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produkty (ID int PRIMARY KEY AUTO_INCREMENT, nazwa varchar(50), cena FLOAT, data DATE ,kategoria varchar(50))")

    #Tworzenie tabeli produkty
    def create_products_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produkty (ID int PRIMARY KEY AUTO_INCREMENT, nazwa varchar(50), cena FLOAT, data DATE ,kategoria varchar(50))")
        self.db.commit()

    #Dodawanie produktów do tabeli
    def create_entry(self, description, price, date , category):
        self.cursor.execute("INSERT INTO produkty (nazwa, cena, data, kategoria) VALUES (%s,%s,%s,%s)", (description, price,date, category))
        self.db.commit()
    def get_product(self):
    #Zapytanie zwracające produkty
        self.cursor.execute ("SELECT id, nazwa, cena, data, kategoria FROM produkty")
        all_products = self.cursor.fetchall()
        return all_products
    #Zapytanie modyfikujące produkty
    def update_product(self, id,  description, price, date , category ):
        self.cursor.execute("UPDATE produkty SET nazwa=%s, cena=%s, data=%s, kategoria=%s WHERE id =%s", (description, price, date, category,  id))
        self.db.commit()

    #Usuwanie produktów
    def delete_product(self, id):
        self.cursor.execute("DELETE FROM produkty WHERE id=%s", (id,))
        self.db.commit()

    #Wyszukiwanie produktów po ID
    def search_by_id(self, id):
        self.cursor.execute("SELECT id, nazwa, cena, data, kategoria FROM produkty WHERE id=%s", (id,))
        item = self.cursor.fetchone()
        return [item]
    #Wyszukiwanie produktów po nazwie
    def search_by_name(self, description):
        self.cursor.execute("SELECT id, nazwa, cena, data, kategoria FROM produkty WHERE nazwa LIKE %s", ('%'+description+'%',))
        items = self.cursor.fetchall()
        return items

class Users:
    def __init__(self):
        #Połączenie z bazą danych
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user = "root",
            database = "projekt"
            ) 
        #Utwworzenie kursora
        self.cursor=self.db.cursor()
        self.create_users_table()
    #Utworzenie tabeli użytkownicy
    def create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uzytkownicy (Imie varchar(50), Nazwisko varchar(50), Email varchar(50), Haslo varchar(50), NumerTelefonu INTEGER, Adres varchar(50), DataUrodzenia DATE, Plec varchar(50))")
        self.db.commit()
    #Dodawanie użytkowników
    def add_user(self, forename, lastname, email, password, phone_number, address, birth, gender):
        try:
            self.cursor.execute("INSERT INTO uzytkownicy (Imie, Nazwisko, Email, Haslo, NumerTelefonu, Adres, DataUrodzenia, Plec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                (forename, lastname, email, password, phone_number, address, birth, gender))
            self.db.commit()
            print("User added successfully.")
        except Exception as e:
            print("Error occurred while adding user:", e)
