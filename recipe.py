from zutat import Zutat
from rezeptsammlung import RecipeCollection



class Recipe:
    def __init__(self, name: str, sammlung: RecipeCollection):
        """
        Erstellt ein neues Rezept.
        
        :param name: Der Name des Rezepts (z.B. "Vollkornbaguette").
        """
        self.name = name
        self.sammlung = sammlung
        self.zutaten = []  # Liste von Zutat-Objekten
        self.schritte = []  # Liste von Zubereitungsschritten (Strings)
        self.recipe_id = 0


        

    def add_ingridient(self, ingridient: Zutat):
        """
        Fügt dem Rezept eine Zutat hinzu.
        
        :param zutat: Das Zutat-Objekt, das hinzugefügt werden soll.
        """
        self.zutaten.append(ingridient)

    def add_schritt(self, schritt: str):
        """
        Fügt dem Rezept einen Zubereitungsschritt hinzu.
        
        :param schritt: Der Schritt, der hinzugefügt werden soll.
        """
        self.schritte.append(schritt)

    def add_sammlung(self, sammlung: RecipeCollection):
        self.sammlung = sammlung

    

    def add_recipe_to_db(self, con):
        cursor = con.cursor()
        cursor.execute("""INSERT INTO recipes (name, collection)
                       VALUES (?,?)
                       """, (self.name, self.sammlung.name))
        self.recipe_id = cursor.lastrowid
        con.commit()

    def add_ingridients_to_db(self, con):
        cursor = con.cursor()
        for ing in self.zutaten:
            cursor.execute("""INSERT INTO ingredients (rezept_id, name, menge, einheit, kategorie)
                       VALUES (?,?,?,?,?)
                       """, (self.recipe_id, ing.name, ing.menge, ing.einheit, ing.category.name))
        con.commit()    




    def __str__(self):
        """
        Gibt eine lesbare Beschreibung des Rezepts zurück.
        """
        zutaten_liste = "\n".join(str(z) for z in self.zutaten)
        schritte_liste = "\n".join(f"{i+1}. {s}" for i, s in enumerate(self.schritte))
        return f"Rezept: {self.name}\n\nZutaten:\n{zutaten_liste}\n\nSchritte:\n{schritte_liste}"