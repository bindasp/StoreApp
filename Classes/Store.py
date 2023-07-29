
from kivy.uix.screenmanager import Screen
from Classes.database import Database
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable

class StoreScreen(Screen):
    def __init__(self, **kwargs):
        super(StoreScreen, self).__init__(**kwargs)
        self.dialog = None

        self.db = Database()

        self.create_datatable()
        self.reload_data_table()
    

    #Dodawanie danych
    def insert_data(self):
        description = self.ids['item_name'].text
        price = self.ids['price_field'].text
        date = self.ids['date_field'].text
        category = self.ids['item_category_label'].text

        self.db.create_entry(description, price , date , category)
        self.reload_data_table()

        self.clear_text()


    #Utworzenie tabeli
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

    #Odświeżenie tabeli
    def reload_data_table(self):
        self.remove_datatable()
        data = self.db.get_product()
        if data is not None:
            self.create_datatable()
            self.data_table.row_data = data
        else:

            self.create_datatable()
            self.data_table.row_data = []


    #Usunięcie tabeli
    def remove_datatable(self):
        self.ids["table"].remove_widget(self.data_table)
    
    #Czyszczenie pól tekstowych
    def clear_text(self):
        self.ids["item_name"].text = ''
        self.ids["price_field"].text = ''
        self.ids["date_field"].text = ''
        self.ids["item_category_label"].text = 'Brak kategorii'
        self.ids["search"].text = ''

    #Aktualizacja przedmiotu
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

        self.db.update_product(id, description, price, date, category)
        self.reload_data_table()
        self.clear_text()

    #Usunięcie przedmiotu
    def delete(self):
        rows = [i[0] for i in self.data_table.get_row_checks()]
        if rows != []:
            for id in rows:
                self.db.delete_product(id)
            self.reload_data_table()
            self.clear_text()
        else:
            print("Nie wybrano produktu")

    #Zaznaczenie wiersza
    def on_check_press(self, instance_table, current_row):
        self.ids["item_name"].text = current_row[1]
        self.ids["price_field"].text = current_row[2]
        self.ids["date_field"].text = current_row[3]
        self.ids["item_category_label"].text = current_row[4]
        print(current_row[0])


    def cancel(self):
        self.reload_data_table()
        self.clear_text()
        
    #Wyszukiwanie produktów
    def search(self):
        id_check = self.ids['id_check']
        item_check = self.ids['item_check']

        if id_check.active and not item_check.active:
            try:
                self.data_table.row_data = self.db.search_by_id(int(self.ids['search'].text))
            except:
                pass
        elif not id_check.active and item_check.active:
            self.data_table.row_data = self.db.search_by_name(str(self.ids['search'].text))
        else:
            print("wybierz jedno pole")

