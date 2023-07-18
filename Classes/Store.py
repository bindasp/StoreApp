
from kivy.uix.screenmanager import Screen
from Classes.database import Database
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable

class StoreScreen(Screen):
    def __init__(self, **kwargs):
        super(StoreScreen, self).__init__(**kwargs)
        self.dialog = None

        self.baza = Database()

        self.create_datatable()
        self.reload_data_table()
        
    def insert_data(self):
        description = self.ids['item_name'].text
        price = self.ids['price_field'].text
        date = self.ids['date_field'].text
        category = self.ids['item_category_label'].text
        track = 0 if self.ids['id_check'].active else 1

        self.baza.create_entry(description, price, date , category, track)
        self.reload_data_table()

        self.clear_text()

    def create_datatable(self):
        self.data_table= MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            check=True, 
            column_data=[
                ("Id", dp(20)), 
                ("Description", dp(30)), 
                ("Price", dp(25)), 
                ("Date", dp(25)), 
                ("Category", dp(25)),
                ("Track", dp(25)),
            ],
            row_data = [],

        )

        self.ids['table'].add_widget(self.data_table)

    def reload_data_table(self):
        self.remove_datatable()
        data = self.baza.get_product()
        if data is not None:
            self.create_datatable()
            self.data_table.row_data = data
        else:
            # Handle the case when data is None, e.g., display an error message or set an empty row_data
            self.create_datatable()
            self.data_table.row_data = []



    def remove_datatable(self):
        self.ids["table"].remove_widget(self.data_table)

    def clear_text(self):
        self.ids["item_name"].text = ''
        self.ids["price_field"].text = ''
        self.ids["date_field"].text = ''
        self.ids["item_category_label"].text = 'Brak kategorii'
