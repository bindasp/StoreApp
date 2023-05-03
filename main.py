from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import KV
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from database import mycursor, db
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture


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
        
    
class AppScreen(Screen):
    pass

class StoreScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

sm.add_widget(LoginScreen(name='profile'))

sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(AppScreen(name='mainapp'))


class ItemCategoryPopup(OneLineAvatarIconListItem):
    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active= False



class MyApp(MDApp):
    dialog = None

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
    
    def show_date_picker_register(self):
        screen = self.root.get_screen('register')
        date_field = screen.ids.birth
        date_field.focus = False
        date_dialog = MDDatePicker(min_year = 2000, max_year = 2023)
        date_dialog.bind(on_save=self.on_save_date_register, on_cancel= self.on_cancel)
        date_dialog.open()

    def on_cancel(self, instance, value):
        pass
    def on_save_date(self, instance, value, date_range):
        screen = self.root.get_screen('store')
        date_field = screen.ids.date_field
        date_field.text = str(value)
        
    def on_save_date_register(self, instance, value, date_range):
        screen = self.root.get_screen('register')
        date_field = screen.ids.birth
        date_field.text = str(value)

    #wyskakujące okienko
    def show_caregory_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = 'Wybierz kategorię',
                type='confirmation',
                items = [ItemCategoryPopup(text='Bluzy'),
                        ItemCategoryPopup(text='Koszulki'),
                        ItemCategoryPopup(text='Spodnie'),
                        ItemCategoryPopup(text='Kurtki')],
                        buttons= [
                            MDFlatButton(
                            text='COFNIJ',
                            theme_text_color= 'Custom',
                            text_color=self.theme_cls.primary_color, 
                            on_release=self.cancel_dialog
                                        ),
                            MDFlatButton(
                            text='OK',
                            theme_text_color= 'Custom',
                            text_color=self.theme_cls.primary_color, )



                        ])
            
        self.dialog.open()

    def show_gender_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = 'Wybierz płeć',
                type='confirmation',
                items = [ItemCategoryPopup(text='Mężczyzna'),
                        ItemCategoryPopup(text='Kobieta'),
                        ItemCategoryPopup(text='Inne'),
                        ],
                        buttons= [
                            MDFlatButton(
                            text='COFNIJ',
                            theme_text_color= 'Custom',
                            text_color=self.theme_cls.primary_color, 
                            on_release=self.cancel_dialog
                                        ),
                            MDFlatButton(
                            text='OK',
                            theme_text_color= 'Custom',
                            text_color=self.theme_cls.primary_color,
                            on_release= self.set_gender )



                        ])
            
        self.dialog.open()

    def cancel_dialog(self, instance):
        self.dialog.dismiss()

    def set_gender(self, gender):
        screen = self.root.get_screen('register')
        date_field = screen.ids.gender
        date_field.text = 'Kobieta'


MyApp().run()