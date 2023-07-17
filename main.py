from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from Classes.Login import LoginScreen
from Classes.Register import RegisterScreen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.button import MDFlatButton
from Classes.ItemPopup import ItemCategoryPopup
from Classes.Store import StoreScreen

from Classes.database import Database

Window.size = (1000,800)

class MenuScreen(Screen):
    pass

class AppScreen(Screen):
    pass


Builder.load_file('Layout/menu.kv')
Builder.load_file('Layout/login.kv')
Builder.load_file('Layout/register.kv')
Builder.load_file('Layout/app.kv')
Builder.load_file('Layout/store.kv')


class MyApp(MDApp):
    dialog = None

    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(LoginScreen(name = 'login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(AppScreen(name = 'app'))
        sm.add_widget(StoreScreen(name = 'store'))

        self.theme_cls.primary_palette="Blue"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Light"
        
        return sm


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
                            text_color=self.theme_cls.primary_color,
                            on_release = self.get_category
                            )

                        ])
            
        self.dialog.open()

    def get_category(self, inst):
        screen = self.root.get_screen('store')
        for item in self.dialog.items:
            if item.ids.check.active == True:
                screen.ids.item_category_label.text = item.text

        self.dialog.dismiss()
        self.dialog = None
        

    def cancel_dialog(self, instance):
        self.dialog.dismiss()

    def show_date_picker(self):
        screen = self.root.get_screen('store')
        date_field = screen.ids.date_field
        date_field.focus = False
        date_dialog = MDDatePicker(min_year = 2000, max_year = 2023)
        date_dialog.bind(on_save=self.on_save_date, on_cancel= self.on_cancel)
        date_dialog.open()

    def on_save_date(self, instance, value, date_range):
        screen = self.root.get_screen('store')
        date_field = screen.ids.date_field
        date_field.text = str(value)

    def on_cancel(self, instance, value):
        pass



MyApp().run()