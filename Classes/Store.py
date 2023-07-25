
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
        formatted_price = float(price)
        date = self.ids['date_field'].text
        category = self.ids['item_category_label'].text

        self.baza.create_entry(description, formatted_price , date , category)
        self.reload_data_table()

        self.clear_text()

    def create_datatable(self):
        self.data_table= MDDataTable(
            size_hint=(1, 1),
            elevation= 2,
            use_pagination=True,
            check=True, 
            column_data=[
                ("Id", dp(20)), 
                ("Nazwa produktu", dp(45)), 
                ("Cena (zł)", dp(25)), 
                ("Data dostawy", dp(25)), 
                ("Rodzaj produktu", dp(50)),
            ],
            row_data = [],

        )
        self.data_table.bind(on_check_press=self.on_check_press)
        self.ids['table'].add_widget(self.data_table)

    def reload_data_table(self):
        self.remove_datatable()
        data = self.baza.get_product()
        if data is not None:
            self.create_datatable()
            self.data_table.row_data = data
        else:

            self.create_datatable()
            self.data_table.row_data = []



    def remove_datatable(self):
        self.ids["table"].remove_widget(self.data_table)

    def clear_text(self):
        self.ids["item_name"].text = ''
        self.ids["price_field"].text = ''
        self.ids["date_field"].text = ''
        self.ids["item_category_label"].text = 'Brak kategorii'

    def update(self):
        checked_rows = self.data_table.get_row_checks()
        if not checked_rows:
            print("Nie wybrałeś żadnego produktu.")
            return
        id = checked_rows[0][0]
        
        description = self.ids['item_name'].text
        price = self.ids['price_field'].text
        date = self.ids['date_field'].text
        category = self.ids['item_category_label'].text

        self.baza.update_product(id, description, price, date, category)
        self.reload_data_table()
        self.clear_text()


    def delete(self):
        rows = [i[0] for i in self.data_table.get_row_checks()]
        if rows != []:
            for id in rows:
                self.baza.delete_product(id)
            self.reload_data_table()
            self.clear_text()
        else:
            print("Nie wybrano produktu")

    def on_check_press(self, instance_table, current_row):
        self.ids["item_name"].text = current_row[1]
        self.ids["price_field"].text = current_row[2]
        self.ids["date_field"].text = current_row[3]
        self.ids["item_category_label"].text = current_row[4]
        print(current_row[0])

    def cancel(self):
        self.reload_data_table()
        self.clear_text()

    def refresh_update(self):
        rows = self.data_table.get_row_checks()
        if rows != []:
            if len(rows) == 1:
                self.ids['update_button'].disabled = False
                self.ids['delete_button'].disabled = False
            elif len(rows) > 1:
                self.ids['update_button'].disabled = True
                self.ids['delete_button'].disabled = False
            else:
                self.ids['update_button'].disabled = True
                self.ids['delete_button'].disabled = True
        else:
            self.ids['update_button'].disabled = True
            self.ids['delete_button'].disabled = True
            self.clear_text()

    def refresh_insert(self):
        if self.data_table.get_row_checks() != []:
            self.ids['insert_button'].disabled = True
        else:
            self.ids['insert_button'].disabled = False