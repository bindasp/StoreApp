from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import screen_helper
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel

Window.size = (300,500)

class MenuScreen(Screen):
    pass

class LoginScreen(Screen):
    data = ObjectProperty(None)
    text_field = ObjectProperty(None)

    def login(self):
        username = self.data.text 
        password = self.text_field.text

        print(username)
        print(password)

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

sm.add_widget(LoginScreen(name='profile'))

sm.add_widget(UploadScreen(name='upload'))

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        return Builder.load_string(screen_helper)


DemoApp().run()