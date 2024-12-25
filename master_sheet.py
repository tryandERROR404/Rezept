
import rezeptsammlung as rs
import rezept as r
import zutat as z
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget



print("hello world")

myRezeptSammlung = rs.RezeptSammlung("süß")
myRezept = r.Rezept("Nusszopf")
salz = z.Zutat("Salz", 10, "g", "nicht zu viel")
myRezept.add_zutat(salz)
print(myRezept)