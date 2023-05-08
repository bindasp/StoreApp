from kivy.properties import ObjectProperty
from Classes.database import mycursor, db
from kivy.uix.screenmanager import Screen, ScreenManager

class RegisterScreen(Screen):
    forename = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email= ObjectProperty(None)
    password= ObjectProperty(None)
    phone_number= ObjectProperty(None)
    address = ObjectProperty(None)
    birth = ObjectProperty(None)
    gender = ObjectProperty(None)

    def validate(self):

        forename = self.forename.text
        lastname = self.lastname.text
        email = self.email.text
        password = self.password.text
        phone_number = self.phone_number.text 
        address = self.address.text
        birth = self.birth.text
        gender = self.gender.text

        mycursor.execute("SELECT * FROM uzytkownicy WHERE email = %s", (email,))
        user = mycursor.fetchone()
        if user:
            print("Użytkownik o podanym adresie email już istnieje.")
            return False
        else:
            mycursor.execute("INSERT INTO uzytkownicy (Imie, Nazwisko, Email, Haslo, NumerTelefonu, Adres, DataUrodzenia, Plec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (forename, lastname, email, password, phone_number, address, birth, gender))
            db.commit()
            self.manager.current = 'mainapp'
        
    