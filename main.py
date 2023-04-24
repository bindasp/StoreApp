from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300,500)

screen_helper = '''
Screen:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Demo"
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 3
        MDLabel:
            text: "Hello World"
            halign: "center"
        MDBottomAppBar:
            MDTopAppBar:
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode:'end'
                type: 'bottom'
                icon: "language-python"
                elevation: 0
                on_action_button: app.navigation_draw()
'''

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'

        return Builder.load_string(screen_helper)

    def navigation_draw(self):
        print("Navigation")

DemoApp().run()