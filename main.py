from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import kivy

kivy.require('1.0.7')


class MyApp(App):
    def build(self):
        # Erstellen eines BoxLayouts, das die Widgets enthält
        layout = BoxLayout(orientation='vertical')

        # Erstellen eines Labels
        self.label = Label()
        
        # Erstellen eines Buttons
        button = Button(text="Klick mich!")

        # Füge den Button und das Label zum Layout hinzu
        layout.add_widget(self.label)
        layout.add_widget(button)

        # Definiere, was beim Klick auf den Button passieren soll
        button.bind(on_press=self.on_button_click)

        return layout

    def on_button_click(self, instance):
        # Ändere den Text des Labels
        self.label.text = "Button wurde geklickt!"

if __name__ == "__main__":
    MyApp().run()