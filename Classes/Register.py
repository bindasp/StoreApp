from kivy.properties import ObjectProperty
from Classes.database import Users
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.dialog import MDDialog
from Classes.ItemPopup import ItemCategoryPopup
from kivymd.uix.button import MDFlatButton

class RegisterScreen(Screen):
    forename = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email= ObjectProperty(None)
    password= ObjectProperty(None)
    phone_number= ObjectProperty(None)
    address = ObjectProperty(None)
    birth = ObjectProperty(None)
    gender = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.dialog = None

        self.uzytkownicy = Users()
    def validate(self):

        forename = self.forename.text
        lastname = self.lastname.text
        email = self.email.text
        password = self.password.text
        phone_number = self.phone_number.text 
        address = self.address.text
        birth = self.birth.text
        gender = self.gender.text

        self.uzytkownicy.cursor.execute("SELECT * FROM uzytkownicy WHERE email = %s", (email,))
        user = self.uzytkownicy.cursor.fetchone()
        if user:
            print("Użytkownik o podanym adresie email już istnieje.")
            return False
        else:
            self.uzytkownicy.add_user(forename, lastname, email, password, phone_number, address, birth, gender)
            self.manager.current = 'app'
        
    def show_date_picker_register(self):
        date_field = self.ids.birth
        date_field.focus = False
        date_dialog = MDDatePicker(min_year = 2000, max_year = 2023)
        date_dialog.bind(on_save=self.on_save_date_register, on_cancel= self.on_cancel)
        date_dialog.open()


    def on_cancel(self, instance, value):
        pass

    def on_save_date_register(self, instance, value, date_range):
        date_field = self.ids.birth
        date_field.text = str(value)
        self.on_cancel


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
                            on_release=self.cancel_dialog
                                        ),
                            MDFlatButton(
                            text='OK',
                            on_release= self.set_gender )



                        ])
            
        self.dialog.open()

    def cancel_dialog(self, instance):
        self.dialog.dismiss()

    def set_gender(self, gender):
        screen = self.ids.gender
        for item in self.dialog.items:
            if item.ids.check.active == True:
                screen.text = item.text

        self.dialog.dismiss()
        self.dialog = None