from zutat import Zutat
from mealplanner import MealPlanner

class Einkaufsliste:
    def __init__(self):
        """
        Erstellt eine leere Einkaufsliste.
        """
        self.zutaten = {}

    def add_zutat(self, zutat):
        """
        Fügt eine Zutat zur Einkaufsliste hinzu. Wenn die Zutat bereits vorhanden ist, wird die Menge addiert.
        
        :param zutat: Ein Zutat-Objekt.
        """
        key = (zutat.name, zutat.einheit)  # Schlüssel: (Name, Einheit)
        if key in self.zutaten:
            self.zutaten[key].menge += zutat.menge
        else:
            self.zutaten[key] = Zutat(zutat.name, zutat.menge, zutat.einheit, zutat.beschreibung)

    def zusammenfassen(self, rezepte):
        """
        Fasst die Zutaten aus mehreren Rezepten zusammen.
        
        :param rezepte: Eine Liste von Rezept-Objekten.
        """
        for rezept in rezepte:
            for zutat in rezept.zutaten:
                self.add_zutat(zutat)

    def gen_from_wochenplan(self, wp: MealPlanner):
        
                
    def anzeigen(self):
        """
        Gibt die Einkaufsliste sortiert nach Zutatenname aus.
        """
        print("Einkaufsliste:")
        for zutat in sorted(self.zutaten.values(), key=lambda z: z.name):
            print(f"{zutat.menge:.2f} {zutat.einheit} {zutat.name}")