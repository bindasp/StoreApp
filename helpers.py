screen_helper = '''
ScreenManager:
    MenuScreen:
    LoginScreen:
    RegisterScreen:
    AppScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Zaloguj się'
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        on_press: root.manager.current = 'login'
        size_hint_x: 0.4

    MDRectangleFlatButton:
        text: 'Zarejestruj się'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        on_press: root.manager.current = 'register'
        size_hint_x: 0.4

<LoginScreen>:
    data: data
    text_field: text_field
    name: 'login'

    MDTextField:
        id: data
        hint_text: "Enter email"
        pos_hint: {'center_x' :0.5, 'center_y' : 0.7}
        size_hint_x: 0.5
        max_text_length: 16

    MDTextField:
        id: text_field
        hint_text: "Enter password"
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
            text_field.password = False if text_field.password is True else True

    MDRectangleFlatButton:
        text:'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.login()

    MDFlatButton:
        text: 'Go back to menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}   
        on_release: root.manager.current = 'menu'



<RegisterScreen>:
    forname: forname
    lastname: lastname
    email: email
    password: password
    name: 'register'

    MDTextField:
        id: forname
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
        text:'Rejestracja'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.register()
        on_press: root.manager.current = 'mainapp'

    MDFlatButton:
        text: 'Wróć do menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}   
        on_release: root.manager.current = 'menu'


<AppScreen>:
    name: 'mainapp'
    MDLabel:
        halign: 'center'
        text: "Aplikacja"

'''
