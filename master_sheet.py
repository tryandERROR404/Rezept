
import rezeptsammlung as rs
import recipe as r
import zutat as z
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget



print("hello world")

myRezeptSammlung = rs.RecipeCollection("süß")
myRezept = r.Recipe("Nusszopf")
salz = z.Zutat("Salz", 10, "g", "nicht zu viel")
myRezept.add_ingridient(salz)
print(myRezept)