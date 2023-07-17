import mysql.connector 

class Database:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user = "root",
        database = "projekt"
        )    
    mycursor = db.cursor()
    def create_products_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produkty (ID int PRIMARY KEY AUTO_INCREMENT, opis varchar(50), cena FLOAT, kategoria varchar(50), track BOOLEAN NOT NULL CHECK (track IN(0,1) ) )")
        self.cursor.commit()

    def create_entry(self, description, price, category, track):
        self.cursor.execute("INSERT INTO produkty (description, price, category, track) VALUES (?,?,?,?)", (description, float(price), category, track))
        self.cursor.commit()
    def get_product(self):
        all_products = self.cursor.execute ("SELECT id, description, price, category, track FROM produkty")
        return all_products
### Stworzenie bazy danych
#mycursor.execute("CREATE TABLE uzytkownicy (ID_Osoby int PRIMARY KEY AUTO_INCREMENT, Imie VARCHAR(50), Nazwisko VARCHAR(50),Email VARCHAR(50),Haslo VARCHAR(50) )")

### Usunięcie bazy danych
#mycursor.execute("DROP TABLE uzytkownicy")

