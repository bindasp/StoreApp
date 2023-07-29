from kivy.properties import ObjectProperty
from Classes.database import Users
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):

    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.dialog = None
        self.uzytkownicy = Users()

    def login(self):
        email = self.email.text
        password = self.password.text

        self.uzytkownicy.cursor.execute("SELECT * FROM uzytkownicy WHERE email = %s", (email,))
        user = self.uzytkownicy.cursor.fetchone()
        #Sprawdzenie, czy użytkownik istnieje
        if user:
            #Walidacja danych
            self.uzytkownicy.cursor.execute("SELECT Haslo FROM uzytkownicy WHERE email = %s", (email,))
            passwd = self.uzytkownicy.cursor.fetchone()
            if password == passwd[0]:
                self.manager.current = 'app'
            else:
                print("Błędne hasło")
        else:
            print("Użytkownik o podanym adresie email nie istnieje")

