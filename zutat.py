from enum import Enum

class Category(Enum):
    GEMUESEOBST = 1
    EIER = 2
    MILCHPRODUKTE = 3
    FLEISCHWAREN = 4
    BACKTRIEBMITTEL = 5
    MEHL = 6
    SAMEN = 7
    GEWÜRZE = 8
    WASSER = 9
    OEl = 10
    SUESS = 11
    SONSTIGES = 12

class Availability(Enum):
    EINKAUFEN = 1
    ZUHAUSE = 2
    NASCHAUEN = 3
    SPEZIALGESCHÄFT = 4
    WEGLASSEN = 5

class Zutat:
    def __init__(self, name: str, menge: float, einheit: str, category: Category, beschreibung: str = ""):
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
        self.category = category
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