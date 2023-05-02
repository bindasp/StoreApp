KV = '''
ScreenManager:
    MenuScreen:
    LoginScreen:
    RegisterScreen:
    AppScreen:
    StoreScreen:


<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Zaloguj się'
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        on_press: root.manager.current = 'store'
        size_hint_x: 0.4

    MDRectangleFlatButton:
        text: 'Zarejestruj się'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        on_press: root.manager.current = 'register'
        size_hint_x: 0.4

<LoginScreen>:
    email: email
    password: password
    name: 'login'

    MDTextField:
        id: email
        hint_text: "Podaj email"
        pos_hint: {'center_x' :0.5, 'center_y' : 0.7}
        size_hint_x: 0.5
        max_text_length: 32

    MDTextField:
        id: password
        hint_text: "Podaj hasło"
        max_text_length: 16
        helper_text_mode: "on_focus"
        pos_hint: {'center_x' :0.5, 'center_y' : 0.5}
        size_hint_x: 0.5
        password:True

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_x": 0.75, "center_y": 0.5}
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            password.password = False if password.password is True else True

    MDRectangleFlatButton:
        text:'Zaloguj się'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.login()

    MDFlatButton:
        text: 'Wróć do menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}   
        on_release: root.manager.current = 'menu'



<RegisterScreen>:
    forename: forename
    lastname: lastname
    email: email
    password: password
    name: 'register'

    MDTextField:
        id: forename
        hint_text: "Podaj imię"
        pos_hint: {'center_x' :0.5, 'center_y' : 0.8}
        size_hint_x: 0.5
        max_text_length: 16

    MDTextField:
        id: lastname
        hint_text: "Podaj nazwisko"
        pos_hint: {'center_x' :0.5, 'center_y' : 0.7}
        size_hint_x: 0.5
        max_text_length: 16
        
    MDTextField:
        id: email
        hint_text: "Podaj email"
        pos_hint: {'center_x' :0.5, 'center_y' : 0.6}
        size_hint_x: 0.5
        max_text_length: 32

    MDTextField:
        id: password
        hint_text: "Podaj hasło"
        max_text_length: 16
        helper_text_mode: "on_focus"
        pos_hint: {'center_x' :0.5, 'center_y' : 0.5}
        size_hint_x: 0.5
        password:True

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_x": 0.75, "center_y": 0.5}
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            password.password = False if password.password is True else True

    MDRectangleFlatButton:
        text:'Zarejestruj się'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.validate()


    MDFlatButton:
        text: 'Wróć do menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}   
        on_release: root.manager.current = 'menu'


<AppScreen>:
    name: 'mainapp'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "Pasek nawigacji"
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
                    id: user_name
                    text: 'test'
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
                            text: 'Profil'
                            
                            IconLeftWidget:
                                icon: 'face-man-profile'
                        OneLineIconListItem:
                            text: 'Magazyn'
                            on_release: root.manager.current = 'store'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Wyloguj się'
                            IconLeftWidget:
                                icon: 'logout'


<StoreScreen>:
    name:'store'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 5
        MDTopAppBar:
            title: 'Magazyn'
            size_hint: 1.0, 0.2
        
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_x: 1

            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 0.4, None
                spacing: 10 

                MDTextField:
                    id: item_name
                    hint_text: 'Podaj nazwę produktu'
                    mode: 'rectangle'
                    size_hint: .9, None
                    pos_hint: {'center_x': .5}

                MDTextField:
                    id: price_field
                    hint_text: 'Podaj cenę'
                    mode: 'rectangle'
                    size_hint: .9, None
                    pos_hint: {'center_x': .5}

                MDTextField:
                    id: date_field
                    hint_text: 'Data'
                    mode: 'rectangle'
                    size_hint: .9, None
                    pos_hint: {'center_x': .5}
                    on_focus: app.show_date_picker()
                    
                #Kategorie produktów
                MDBoxLayout:
                    size_hint: 0.9, None
                    height: 40
                    pos_hint: {'center_x': 0.5}
                    MDLabel:
                        id: item_category_label
                        text: "Brak kategorii"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDRaisedButton:
                        id: item_category_button
                        text: 'Wybierz kategorię'
                        size_hint: 0.7, None
                        on_release: app.show_caregory_dialog()
            # Zdjęcie
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 0.4, 1
                spacing: 10
                pos_hint: {'center_y': 0.8}

                FitImage:
                    id: product_photo
                    size_hint: 0.5, None
                    paddding: 5.5
                    height: '130dp'
                    pos_hint: {'center_x': 0.5, 'center_y': 1}
                    source: 'images/image.jpg'

                    

        Widget: 

'''
