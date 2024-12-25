from zutat import Zutat
class Rezept:
    def __init__(self, name: str):
        """
        Erstellt ein neues Rezept.
        
        :param name: Der Name des Rezepts (z.B. "Vollkornbaguette").
        """
        self.name = name
        self.zutaten = []  # Liste von Zutat-Objekten
        self.schritte = []  # Liste von Zubereitungsschritten (Strings)

    def add_zutat(self, zutat: Zutat):
        """
        Fügt dem Rezept eine Zutat hinzu.
        
        :param zutat: Das Zutat-Objekt, das hinzugefügt werden soll.
        """
        self.zutaten.append(zutat)

    def add_schritt(self, schritt: str):
        """
        Fügt dem Rezept einen Zubereitungsschritt hinzu.
        
        :param schritt: Der Schritt, der hinzugefügt werden soll.
        """
        self.schritte.append(schritt)

    def __str__(self):
        """
        Gibt eine lesbare Beschreibung des Rezepts zurück.
        """
        zutaten_liste = "\n".join(str(z) for z in self.zutaten)
        schritte_liste = "\n".join(f"{i+1}. {s}" for i, s in enumerate(self.schritte))
        return f"Rezept: {self.name}\n\nZutaten:\n{zutaten_liste}\n\nSchritte:\n{schritte_liste}"