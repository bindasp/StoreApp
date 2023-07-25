import mysql.connector 

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user = "root",
            database = "projekt"
            )    
        self.cursor = self.db.cursor()
        self.create_products_table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produkty (ID int PRIMARY KEY AUTO_INCREMENT, opis varchar(50), cena FLOAT, data DATE ,kategoria varchar(50))")
    def create_products_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produkty (ID int PRIMARY KEY AUTO_INCREMENT, opis varchar(50), cena FLOAT, data DATE ,kategoria varchar(50))")
        self.db.commit()

    def create_entry(self, description, price, date , category):
        self.cursor.execute("INSERT INTO produkty (opis, cena, data, kategoria) VALUES (%s,%s,%s,%s)", (description, price,date, category))
        self.db.commit()
    def get_product(self):
        self.cursor.execute ("SELECT id, opis, cena, data, kategoria FROM produkty")
        all_products = self.cursor.fetchall()
        return all_products
    
    def update_product(self, id,  description, price, date , category ):
        self.cursor.execute("UPDATE produkty SET opis=%s, cena=%s, data=%s, kategoria=%s WHERE id =%s", (description, price, date, category,  id))
        self.db.commit()

    def delete_product(self, id):
        self.cursor.execute("DELETE FROM produkty WHERE id=%s", (id,))
        self.db.commit()
class Users:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user = "root",
            database = "projekt"
            ) 
        self.cursor=self.db.cursor()
        self.create_users_table()
    def create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uzytkownicy (Imie varchar(50), Nazwisko varchar(50), Email varchar(50), Haslo varchar(50), NumerTelefonu INTEGER, Adres varchar(50), DataUrodzenia DATE, Plec varchar(50))")
        self.db.commit()
        
    def add_user(self, forename, lastname, email, password, phone_number, address, birth, gender):
        try:
            self.cursor.execute("INSERT INTO uzytkownicy (Imie, Nazwisko, Email, Haslo, NumerTelefonu, Adres, DataUrodzenia, Plec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                (forename, lastname, email, password, phone_number, address, birth, gender))
            self.db.commit()
            print("User added successfully.")
        except Exception as e:
            print("Error occurred while adding user:", e)
