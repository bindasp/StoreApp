from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        screen = Screen()
        # username = MDTextField(text="Enter username",
        #                         pos_hint={'center_x' :0.5, 'center_y' : 0.5}, 
        #                         size_hint_x=None, width=300)
        self.username = Builder.load_string(username_helper)

        btn_flat = MDRectangleFlatButton(text='Show', pos_hint= {'center_x': 0.5, 'center_y': 0.4}, on_release=self.show_data)

        #icon_btn = MDFloatingActionButton(icon='facebook', pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        screen.add_widget(self.username)
        screen.add_widget(btn_flat)

        return screen
    def show_data(self,obj):
        print(self.username.text)

DemoApp().run()