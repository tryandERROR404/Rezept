from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import kivy
import sqlite3
import os

from recipe import Recipe
from zutat import Category, Availability, Zutat
from rezeptsammlung import RecipeCollection
from mealplanner import MealPlanner

#kivy.require('1.0.7')


# class MyApp(App):
#     def build(self):
#         # Erstellen eines BoxLayouts, das die Widgets enthält
#         layout = BoxLayout(orientation='vertical')

#         # Erstellen eines Labels
#         self.label = Label()
        
#         # Erstellen eines Buttons
#         button = Button(text="Klick mich!")

#         # Füge den Button und das Label zum Layout hinzu
#         layout.add_widget(self.label)
#         layout.add_widget(button)

#         # Definiere, was beim Klick auf den Button passieren soll
#         button.bind(on_press=self.on_button_click)

#         return layout

#     def on_button_click(self, instance):
#         # Ändere den Text des Labels
#         self.label.text = "Button wurde geklickt!"

# if __name__ == "__main__":
#     MyApp().run()

#testing

def create_db():
    connection = sqlite3.connect("rezepte.db")
    cursor = connection.cursor()

    # Tabelle rezepte erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            collection TEXT
        );
    """)

    # Tabelle zutaten erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rezept_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            menge REAL NOT NULL,
            einheit TEXT NOT NULL,
            kategorie TEXT,
            FOREIGN KEY (rezept_id) REFERENCES rezepte (id) ON DELETE CASCADE
        );
    """)

    # Tabelle wochenplan erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wochenplan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag TEXT NOT NULL,
            rezept_id INTEGER NOT NULL,
            FOREIGN KEY (rezept_id) REFERENCES rezepte (id) ON DELETE CASCADE
        );
    """)

    # Tabelle einkaufsliste erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS einkaufsliste (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            menge REAL NOT NULL,
            einheit TEXT NOT NULL,
            verfügbarkeit TEXT DEFAULT "kaufen",
            kategorie TEXT
        );
    """)

    connection.commit()
    print("Datenbank und Tabellen wurden erstellt!")
    return connection

def remove_db_file():
    db_file = "rezepte.db"
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Die Datei '{db_file}' wurde gelöscht.")
    else:
        print(f"Die Datei '{db_file}' existiert nicht.")

remove_db_file()

sammlung_suss = RecipeCollection("süs")
sammlung_brot = RecipeCollection("brot")

rezept_brot = Recipe("Brot", sammlung_brot)
rezept_brot.add_ingridient(Zutat("Mehl", 500, "g", Category.MEHL))
rezept_brot.add_ingridient(Zutat("Hefe", 0.1, "g", Category.BACKTRIEBMITTEL))


rezept_zopf = Recipe("Zopf", sammlung_suss)
rezept_zopf.add_ingridient(Zutat("Zucker", 100, "g", Category.SUESS))
rezept_zopf.add_ingridient(Zutat("Mehl", 100, "g", Category.MEHL))

rezept_nudeln = Recipe("Nudeln mit Tomatensoße", sammlung_brot)
rezept_nudeln.add_ingridient(Zutat("Nudeln", 200, "g", Category.MEHL))
con = create_db()
rezept_nudeln.add_recipe_to_db(con)
rezept_zopf.add_recipe_to_db(con)
rezept_brot.add_recipe_to_db(con)
rezept_nudeln.add_ingridients_to_db(con)
rezept_brot.add_ingridients_to_db(con)
rezept_zopf.add_ingridients_to_db(con)

my_mp = MealPlanner()
my_mp.hinzufügen_rezept("Montag",rezept_zopf)
my_mp.hinzufügen_rezept("Dienstag", rezept_brot)
my_mp.hinzufügen_rezept("Dienstag", rezept_nudeln)
my_mp.add_meal_plan_to_db(con)

con.close()

