from rezept import Rezept
class RezeptSammlung:
    def __init__(self, name: str):
        """
        Erstellt eine neue Rezeptsammlung.
        
        :param name: Der Name des Rezepts (z.B. "Vollkornbaguette").
        """
        self.name = name
        self.rezept = []  # Liste von Rezpten
    
    def setPropertyRezeptsammlung(self, rezeptsammlung):
            self.rezeptsammlung = RezeptSammlung(rezeptsammlung)

    def add_Rezept(self, rezept: Rezept):
        """
        Fügt dem Rezeptsammlung ein Rezept hinzu.
        
        :param rezept: Das Rezept-Objekt, das hinzugefügt werden soll.
        """
        self.rezept.append(rezept)

    # def add_Rezeptsammlung(self, rezeptsammlung: RezeptSammlung):
    #     """
    #     Fügt der Rezeptsammlung eine RezeptSammlung hinzu.
        
    #     :param Rezeptsammlung: Die Rezeptsammlung, die hinzugefügt werden soll.
    #     """
    #     self.rezeptsammlung.append(rezeptsammlung)

    def __str__(self):
        """
        Gibt eine lesbare Beschreibung des Rezepts zurück.
        """
        rezept_liste = "\n".join(str(z) for z in self.rezept)
        rezeptsammlung_liste = "\n".join(f"{i+1}. {s}" for i, s in enumerate(self.RezeptSammlung))
        return f"Rezept: {self.name}\n\nRezeptsammlung:\n{rezept_liste}\n\nSchritte:\n{rezeptsammlung_liste}"