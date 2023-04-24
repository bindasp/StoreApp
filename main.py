from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, MDList, ThreeLineIconListItem, IconLeftWidget, ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
                



"""

class DemoApp(MDApp):

    def build(self):

        screen = Builder.load_string(list_helper)

        return screen
    
    def on_start(self):
        for i in range(20):
            items = OneLineListItem(text = 'Item ' +  str(i))
            self.root.ids.container.add_widget(items)

DemoApp().run()