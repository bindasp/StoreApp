from kivy.properties import ObjectProperty
from Classes.database import Database
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):

    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        email = self.email.text
        password = self.password.text

        Database.mycursor.execute("SELECT * FROM uzytkownicy WHERE email = %s", (email,))
        user = Database.mycursor.fetchone()
        if user:
            Database.mycursor.execute("SELECT Haslo FROM uzytkownicy WHERE email = %s", (email,))
            passwd = Database.mycursor.fetchone()
            if password == passwd[0]:
                self.manager.current = 'app'
            else:
                print("Błędne hasło")
        else:
            print("Użytkownik o podanym adresie email nie istnieje")

