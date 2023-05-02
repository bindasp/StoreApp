from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import KV
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from database import mycursor, db
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker

Window.size = (1000,770)

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

class StoreScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

sm.add_widget(LoginScreen(name='profile'))

sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(AppScreen(name='mainapp'))

class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        
        return Builder.load_string(KV)

    def show_date_picker(self):
        screen = self.root.get_screen('store')
        date_field = screen.ids.date_field
        date_field.focus = False
        date_dialog = MDDatePicker(min_year = 2000, max_year = 2023)
        date_dialog.bind(on_save=self.on_save_date, on_cancel= self.on_cancel)
        date_dialog.open()
    def on_cancel(self, instance, value):
        pass
    def on_save_date(self, instance, value, date_range):
        screen = self.root.get_screen('store')
        date_field = screen.ids.date_field
        date_field.text = str(value)
        

MyApp().run()