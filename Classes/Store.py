
from kivy.uix.screenmanager import Screen
from Classes.database import Database
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable

class StoreScreen(Screen):
    def __init__(self, **kwargs):
        super(StoreScreen, self).__init__(**kwargs)
        self.dialog = None

        self.create_datatable()
        self.reload_data_table()
        
    def insert_data(self):
        description = self.ids['item_name'].text
        price = self.ids['price_field'].text
        date = self.ids['date_field'].text
        category = self.ids['item_category_label'].text
        track = 0 if self.ids['id_check'].active else 1

        Database.mycursor.execute("INSERT INTO produkty (opis, cena, kategoria, track) VALUES (%s,%s,%s,%s)", (description, price, category, track))
        Database.db.commit()
        self.reload_data_table()

    def create_datatable(self):
        self.data_table= MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            check=True, 
            column_data=[
                ("Id", dp(20)), 
                ("Description", dp(30)), 
                ("Price", dp(25)), 
                ("Category", dp(25)),
                ("Track", dp(25)),
            ],
            row_data = [],

        )

        self.ids['table'].add_widget(self.data_table)

    def reload_data_table(self):
        self.remove_datatable()
        self.create_datatable()
        
        # Wykonaj zapytanie SQL
        Database.mycursor.execute("SELECT id, opis, cena, kategoria, track FROM produkty")
        
        # Pobierz wszystkie wiersze
        result = Database.mycursor.fetchall()
        
        # Przetwórz wynik i przypisz do row_data
        self.data_table.row_data = [list(row) for row in result]
        Database.db.commit()
    def remove_datatable(self):
        self.ids["table"].remove_widget(self.data_table)