from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineListItem, MDList, ThreeLineIconListItem, IconLeftWidget, ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView

list_helper = """




"""

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            image = ImageLeftWidget(source="zdj.jpg")
            items = ThreeLineAvatarListItem(text= 'Item ' + str(i), secondary_text='Hello world', tertiary_text = 'Third text')
            
            items.add_widget(image)
            list_view.add_widget(items)
            
        
        screen.add_widget(scroll)

        # username = MDTextField(text="Enter username",
        #                         pos_hint={'center_x' :0.5, 'center_y' : 0.5}, 
        #                         size_hint_x=None, width=300)
        self.username = Builder.load_string(username_helper)

        btn_flat = MDRectangleFlatButton(text='Show', pos_hint= {'center_x': 0.5, 'center_y': 0.4}, on_release=self.show_data)

        #icon_btn = MDFloatingActionButton(icon='facebook', pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        #screen.add_widget(self.username)
        #screen.add_widget(btn_flat)
        

        return screen
    def show_data(self,obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + ' does not exist'
        close_button = MDFlatButton(text='Close', on_release = self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Username Check' ,text=check_string,
                        size_hint=(0.7, 1),
                        buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

DemoApp().run()