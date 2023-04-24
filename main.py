from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import navigation_helper, screen_helper
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (300,500)

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

sm.add_widget(ProfileScreen(name='profile'))

sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'

        return Builder.load_string(screen_helper)

    def navigation_draw(self):
        print("Navigation")

DemoApp().run()