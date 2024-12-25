class Zutat:
    def __init__(self, name: str, menge: float, einheit: str, beschreibung: str = ""):
        """
        Erstellt eine Zutat für ein Rezept.
        
        :param name: Name der Zutat (z.B. "Weizenmehl").
        :param menge: Die Menge der Zutat (z.B. 500 für 500 g).
        :param einheit: Die Einheit der Zutat (z.B. "g", "ml").
        :param beschreibung: Optionale Beschreibung der Zutat (z.B. "zum Bestreuen", "kaltes Wasser").
        """
        self.name = name
        self.menge = menge
        self.einheit = einheit
        self.beschreibung = beschreibung

    def __str__(self):
        """
        Gibt eine lesbare Beschreibung der Zutat zurück.
        """
        beschreibung = f" ({self.beschreibung})" if self.beschreibung else ""
        return f"{self.menge} {self.einheit} {self.name}{beschreibung}"

    def skaliere(self, faktor: float):
        """
        Skaliert die Menge der Zutat.
        
        :param faktor: Der Skalierungsfaktor (z.B. 2 für die doppelte Menge).
        """
        self.menge *= faktor