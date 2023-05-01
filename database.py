import mysql.connector 

db = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    database = "projekt"
    )

mycursor= db.cursor()

### Stworzenie bazy danych
#mycursor.execute("CREATE TABLE uzytkownicy (ID_Osoby int PRIMARY KEY AUTO_INCREMENT, Imie VARCHAR(50), Nazwisko VARCHAR(50),Email VARCHAR(50),Haslo VARCHAR(50) )")

### Usunięcie bazy danych
#mycursor.execute("DROP TABLE uzytkownicy")

mycursor.execute("SELECT * FROM uzytkownicy")