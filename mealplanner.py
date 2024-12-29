from typing import Dict, List
from recipe import Recipe

class MealPlanner:
    def __init__(self):
        self.tage: Dict[str, List[Recipe]] = {tag: [] for tag in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]}
        self.mp_list = []

    def hinzufügen_rezept(self, tag: str, rezept: Recipe):
        if tag in self.tage:
            self.tage[tag].append(rezept)

    def skalieren(self, faktor: float):
        for tag, rezepte in self.tage.items():
            for rezept in rezepte:
                for zutat in rezept.zutaten:
                    zutat.menge *= faktor

    def add_meal_plan_to_db(self,con):
        cursor = con.cursor()
        for tag, rezepte in self.tage.items():
            for rezept in rezepte:
                    
                # Daten in die Tabelle einfügen
                cursor.execute("""
                    INSERT INTO wochenplan (tag, rezept_id)
                    VALUES (?, ?)
                """, (tag, rezept.recipe_id))
        con.commit()  

    def __repr__(self):
        return f"Wochenplan({', '.join([f'{tag}: {len(rezepte)} Rezepte' for tag, rezepte in self.tage.items()])})"

