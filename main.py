from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window



Window.size = (300,500)

navigation_helper="""
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "Demo"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
                        elevation: 3
                    
                    Widget:
                        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                spacing: '8dp'
                padding: '8dp'
                orientation: 'vertical'

                MDLabel:
                    text:'Patryk'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text:'bindas.patryk@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-man-profile'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'

"""

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

        return Builder.load_string(navigation_helper)

    def navigation_draw(self):
        print("Navigation")

DemoApp().run()