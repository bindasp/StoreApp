from kivy.properties import ObjectProperty
from Classes.database import mycursor
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):

    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        email = self.email.text
        password = self.password.text

        mycursor.execute("SELECT * FROM uzytkownicy WHERE email = %s", (email,))
        user = mycursor.fetchone()
        if user:
            mycursor.execute("SELECT Haslo FROM uzytkownicy WHERE email = %s", (email,))
            passwd = mycursor.fetchone()
            if password == passwd[0]:
                self.manager.current = 'app'
            else:
                print("Błędne hasło")
        else:
            print("Użytkownik o podanym adresie email nie istnieje")
        
