from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import screen_helper
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from database import mycursor, db

Window.size = (800,800)

class MenuScreen(Screen):
    pass

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
                self.manager.current = 'mainapp'
            else:
                print("Błędne hasło")
        else:
            print("Użytkownik o podanym adresie email nie istnieje")
        

class RegisterScreen(Screen):
    forename = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email= ObjectProperty(None)
    password= ObjectProperty(None)

    def validate(self):

        forename = self.forename.text
        lastname = self.lastname.text
        email = self.email.text
        password = self.password.text

        mycursor.execute("SELECT * FROM uzytkownicy WHERE email = %s", (email,))
        user = mycursor.fetchone()
        if user:
            print("Użytkownik o podanym adresie email już istnieje.")
            return False
        else:
            mycursor.execute("INSERT INTO uzytkownicy (Imie, Nazwisko, Email, Haslo) VALUES (%s, %s, %s, %s)",  (forename, lastname, email, password))
            db.commit()
            self.manager.current = 'mainapp'
        



class AppScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

sm.add_widget(LoginScreen(name='profile'))

sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(RegisterScreen(name='mainapp'))

class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        return Builder.load_string(screen_helper)


MyApp().run()